
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import spacy
import PyPDF2
import requests
from bs4 import BeautifulSoup
import re
import io

nlp = spacy.load("en_core_web_sm")

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class ResumeMatchRequest(BaseModel):
    resume_text: str
    job_description: str

def preprocess(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

def extract_text_from_pdf(pdf_file: UploadFile):
    """Extract text from uploaded PDF file"""
    try:
        pdf_content = pdf_file.file.read()
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_content))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        return text.strip()
    except Exception as e:
        raise Exception(f"Error reading PDF: {str(e)}")

def fetch_job_description_from_url(url: str):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=12)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "lxml")

        candidates = soup.find_all(['p','li','div','span','h1','h2','h3'])
        texts = []
        for el in candidates:
            t = el.get_text(separator=" ", strip=True)
            if t and len(t.split()) > 3:
                texts.append(t)

        text = " ".join(texts)
        irrelevant_patterns = r'\b(cookie|privacy|policy|linkedin|sign|agree|agreement|email|jobid|jobs|apply|footer|copyright|career|posting|terms|conditions|equal opportunity|company|team|about us)\b|http[s]?://\S+|www\.\S+|\d{4,}'
        text = re.sub(irrelevant_patterns, '', text, flags=re.IGNORECASE)
        text = re.sub(r'\s+', ' ', text).strip()

        if len(text.split()) < 50:
            raise Exception("URL content too short or not a job description")
        return text
    except Exception as e:
        raise Exception(f"Error fetching URL {url}: {str(e)}")


@app.get("/")
def root():
    return {"message": "Resume matcher is live!"}

@app.post("/match/")
def match_resume(request: ResumeMatchRequest):
    try:
        # Validate input
        if not request.resume_text.strip() or not request.job_description.strip():
            return {
                "error": "Both resume_text and job_description must not be empty",
                "match_score": 0,
                "result": "Error"
            }
        
        resume = preprocess(request.resume_text)
        jd = preprocess(request.job_description)
        
        # Check if preprocessing resulted in empty strings
        if not resume or not jd:
            return {
                "error": "Unable to process text. Please ensure both inputs contain meaningful text.",
                "match_score": 0,
                "result": "Error"
            }

        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([resume, jd])
        score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0] * 100

        return {
            "match_score": round(score, 2),
            "result": "Strong match" if score > 70 else "Moderate" if score > 40 else "Weak"
        }
    except Exception as e:
        return {
            "error": f"An error occurred: {str(e)}",
            "match_score": 0,
            "result": "Error"
        }

@app.post("/match-pdf/")
async def match_resume_pdf(
    resume_pdf: UploadFile = File(...),
    job_description: str = Form(...)
):
    try:
        # Validate file type
        if not resume_pdf.filename.lower().endswith('.pdf'):
            return {
                "error": "Please upload a PDF file",
                "match_score": 0,
                "result": "Error"
            }
        
        # Extract text from PDF
        resume_text = extract_text_from_pdf(resume_pdf)
        if not resume_text.strip():
            return {
                "error": "Could not extract text from PDF. Please ensure it's a text-based PDF.",
                "match_score": 0,
                "result": "Error"
            }
        
        # Process job description
        if not job_description.strip():
            return {
                "error": "Job description must not be empty",
                "match_score": 0,
                "result": "Error"
            }
        
        resume = preprocess(resume_text)
        jd = preprocess(job_description)
        
        if not resume or not jd:
            return {
                "error": "Unable to process text. Please ensure both inputs contain meaningful text.",
                "match_score": 0,
                "result": "Error"
            }

        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([resume, jd])
        score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0] * 100

        return {
            "match_score": round(score, 2),
            "result": "Strong match" if score > 70 else "Moderate" if score > 40 else "Weak",
            "extracted_resume": resume_text[:500] + "..." if len(resume_text) > 500 else resume_text
        }
    except Exception as e:
        return {
            "error": f"An error occurred: {str(e)}",
            "match_score": 0,
            "result": "Error"
        }

@app.post("/match-url/")
async def match_resume_url(
    resume_text: str = Form(...),
    job_url: str = Form(...)
):
    try:
        # Validate inputs
        if not resume_text.strip():
            return {
                "error": "Resume text must not be empty",
                "match_score": 0,
                "result": "Error"
            }
        
        if not job_url.strip():
            return {
                "error": "Job URL must not be empty",
                "match_score": 0,
                "result": "Error"
            }
        
        # Fetch job description from URL
        job_description = fetch_job_description_from_url(job_url)
        
        resume = preprocess(resume_text)
        jd = preprocess(job_description)
        
        if not resume or not jd:
            return {
                "error": "Unable to process text. Please ensure both inputs contain meaningful text.",
                "match_score": 0,
                "result": "Error"
            }

        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([resume, jd])
        score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0] * 100

        return {
            "match_score": round(score, 2),
            "result": "Strong match" if score > 70 else "Moderate" if score > 40 else "Weak",
            "extracted_job_description": job_description[:500] + "..." if len(job_description) > 500 else job_description
        }
    except Exception as e:
        return {
            "error": f"An error occurred: {str(e)}",
            "match_score": 0,
            "result": "Error"
        }
