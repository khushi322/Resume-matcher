***📄 Resume Matcher***





🚀 Live Demo
🌐 Frontend (Netlify): Resume Matcher UI

⚡ Backend API (Render): FastAPI Backend

✨ Features
Text Input → Paste resume & job description to get a score

PDF Upload → Upload your resume in PDF format

Job URL Extraction → Extract job descriptions directly from a link

Instant Match Score & Result (Weak, Moderate, Strong)

Deployed with Render (Backend) & Netlify (Frontend)

🛠️ Tech Stack
Backend: FastAPI · scikit-learn · spaCy · PyPDF2

Frontend: HTML · CSS · JavaScript

Deployment: Render · Netlify

▶️ How to Use
Open the Resume Matcher UI.

Choose one option:

Paste resume text + job description

Upload a PDF resume

Enter a job posting URL

Click Match Resume → See your score & result instantly

📌 API Documentation
👉 Swagger Docs

Example Request:

json
Copy
Edit
POST /match/
{
  "resume_text": "Experienced in Python, SQL, and Tableau.",
  "job_description": "Looking for a Data Analyst skilled in Python, SQL, and Power BI."
}
Example Response:

json
Copy
Edit
{
  "match_score": 72.5,
  "result": "Moderate"
}

👩‍💻 Author
Developed by Khushi Shukla 💡
