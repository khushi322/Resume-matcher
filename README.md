***📄 Resume Matcher***





🚀 Live Demo
🌐 Frontend (Netlify): 👉 Resume Matcher UI

⚡ Backend API (Render): 👉 FastAPI Backend

⚡ Features
✅ Paste Resume & Job Description → Get instant Match Score & Result
✅ Upload Resume PDF → Extract text automatically
✅ Job URL Extraction → Pulls job description directly from URL
✅ User-Friendly UI hosted on Netlify
✅ FastAPI Backend deployed on Render

🛠️ Tech Stack
Backend: ⚡ FastAPI, 🧠 scikit-learn, 🔍 spaCy, 📄 PyPDF2

Frontend: 🌐 HTML, CSS, JavaScript

Deployment: ☁️ Render (Backend), 🌱 Netlify (Frontend)

▶️ How to Use
1️⃣ Open the Live UI
2️⃣ Choose one of the modes:

✍️ Text Input → Paste resume & job description

📄 PDF Upload → Upload your resume in PDF format

🔗 URL Input → Enter a job posting URL
3️⃣ Click Match Resume → Instantly see Score + Result

📌 API Documentation
📍 Available at 👉 Swagger Docs

🔹 Example request:

json
Copy
Edit
POST /match/
{
  "resume_text": "Experienced in Python, SQL, and Tableau.",
  "job_description": "Looking for a Data Analyst skilled in Python, SQL, and Power BI."
}
🔹 Example response:

json
Copy
Edit
{
  "match_score": 72.5,
  "result": "Moderate"
}
👩‍💻 Author
✨ Developed with passion by Khushi Shukla 💡
