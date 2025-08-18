# 📄 Resume Matcher  

[![Frontend](https://img.shields.io/badge/Frontend-Live%20on%20Netlify-brightgreen?logo=netlify)](https://unrivaled-parfait-0f4139.netlify.app/)  
[![Backend](https://img.shields.io/badge/Backend-Live%20on%20Render-blueviolet?logo=render)](https://resume-matcher-auwj.onrender.com)  
![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)  
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-success?logo=fastapi)  
![NLP](https://img.shields.io/badge/NLP-spaCy%20%7C%20scikit--learn-orange)  

---

## 🚀 Live Demo  

- 🌐 **Frontend (Netlify):** [Resume Matcher UI](https://unrivaled-parfait-0f4139.netlify.app/)  
- ⚡ **Backend API (Render):** [FastAPI Backend](https://resume-matcher-auwj.onrender.com)  

---

## ✨ Features  

- 📝 **Text Input** → Paste resume & job description to get a score  
- 📄 **PDF Upload** → Upload your resume in PDF format  
- 🔗 **Job URL Extraction** → Extract job descriptions directly from a link  
- 📊 **Instant Match Score & Result** (`Weak`, `Moderate`, `Strong`)  
- ☁️ **Deployed** with Render (Backend) & Netlify (Frontend)  

---

## 🛠️ Tech Stack  

- **Backend:** FastAPI · scikit-learn · spaCy · PyPDF2  
- **Frontend:** HTML · CSS · JavaScript  
- **Deployment:** Render · Netlify  

---

## ▶️ How to Use  

1️⃣ Open the [Resume Matcher UI](https://unrivaled-parfait-0f4139.netlify.app/)  
2️⃣ Choose one option:  
   - Paste resume text + job description  
   - Upload a PDF resume  
   - Enter a job posting URL  
3️⃣ Click **Match Resume** → See your **score & result instantly**  

---

## 📌 API Documentation  

📍 Available at 👉 [Swagger Docs](https://resume-matcher-auwj.onrender.com/docs)  

**Example Request:**  

```json
POST /match/
{
  "resume_text": "Experienced in Python, SQL, and Tableau.",
  "job_description": "Looking for a Data Analyst skilled in Python, SQL, and Power BI."
}

**Example Response:**
{
  "match_score": 72.5,
  "result": "Moderate"
}

