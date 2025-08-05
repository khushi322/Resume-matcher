
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import spacy

nlp = spacy.load("en_core_web_sm")

app = FastAPI()

class ResumeMatchRequest(BaseModel):
    resume_text: str
    job_description: str

def preprocess(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

@app.get("/")
def root():
    return {"message": "Resume matcher is live!"}

@app.post("/match/")
def match_resume(request: ResumeMatchRequest):
    resume = preprocess(request.resume_text)
    jd = preprocess(request.job_description)

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume, jd])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0] * 100

    return {
        "match_score": round(score, 2),
        "result": "Strong match" if score > 70 else "Moderate" if score > 40 else "Weak"
    }
