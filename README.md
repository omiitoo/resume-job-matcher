# resume-job-matcher

AI-powered Resume and Job Description similarity analyzer using NLP (TF-IDF & Cosine Similarity).

## Features
- Calculates a match score (0–100%)
- Shows a match level (Low / Moderate / Strong)
- Extracts top overlapping keywords

## How to run

```bash
git clone https://github.com/omiitoo/resume-job-matcher.git
cd resume-job-matcher

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
python app.py
