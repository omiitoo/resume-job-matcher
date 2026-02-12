<div align="center">

# 🧠 Resume–Job Match Analyzer

AI-powered Resume & Job Description similarity analyzer  
built with **NLP (TF-IDF + Cosine Similarity)**.

CLI + Web Interface included.

</div>

---

## 📌 Overview

This project analyzes how well a resume matches a job description.

It calculates:

- ✅ Match Score (0–100%)
- ✅ Match Level (Low / Moderate / Strong)
- ✅ Top overlapping keywords
- ✅ Works in Terminal (CLI)
- ✅ Works in Web Browser (Streamlit UI)

---

## 🛠 Tech Stack

- Python 3
- scikit-learn
- nltk
- Streamlit
- TF-IDF Vectorization
- Cosine Similarity

---

# 🚀 HOW TO RUN

Below are the full steps to run the project locally.

---

## 1️⃣ Clone the repository

```bash
git clone https://github.com/omiitoo/resume-job-matcher.git
cd resume-job-matcher
```

---

## 2️⃣ Create a virtual environment (recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

To exit later:

```bash
deactivate
```

---

## 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🖥 Option A — Run in Terminal (CLI)

```bash
python app.py
```

### How it works:

1. Paste your resume text
2. Type `END` on a new line
3. Paste the job description
4. Type `END` again

Example input:

```bash
I am a Software Engineering student.
I have experience with Python and SQL.
END
Looking for a Python developer with SQL skills.
END
```

You will receive:

- Match Score
- Match Level
- Top Matching Keywords

---

# 🌐 Option B — Run Web Interface (Streamlit)

```bash
streamlit run web_app.py
```

Then open your browser:

```bash
http://localhost:8501
```

### Web Features:

- Multi-line resume input
- Multi-line job description input
- Adjustable number of keywords
- Clean UI
- Instant match calculation

---

# 🛑 Stop the Application

To stop CLI or Streamlit:

```bash
CTRL + C
```

---

# 📂 Project Structure

```bash
resume-job-matcher/
│
├── app.py              # CLI version
├── web_app.py          # Streamlit web UI
├── requirements.txt
├── utils.py            # Text processing & similarity logic
├── README.md
└── LICENSE
```

---

# 🧪 Troubleshooting

If streamlit command is not found:

```bash
pip install streamlit
```

If port 8501 is busy:

```bash
streamlit run web_app.py --server.port 8502
```

---

# 📈 Future Improvements

- PDF resume upload
- AI-powered suggestions
- Skill gap analysis
- Deployment on Streamlit Cloud
- Docker support

---

# 📜 License

MIT License

---

<div align="center">

Built with ❤️ by Yumer Mustafa

</div>
