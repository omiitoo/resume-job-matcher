import re
from collections import Counter

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-zA-Z ]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def calculate_similarity(text1: str, text2: str) -> float:
    text1 = clean_text(text1)
    text2 = clean_text(text2)

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform([text1, text2])

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return round(float(similarity[0][0]) * 100, 2)


def get_match_level(score: float) -> str:
    if score < 30:
        return "Low match"
    if score < 60:
        return "Moderate match"
    return "Strong match"


def extract_common_keywords(resume_text: str, job_text: str, top_n: int = 10):
    """
    Very simple keyword overlap (after cleaning).
    Returns a list of (keyword, count_in_both).
    """
    resume = clean_text(resume_text)
    job = clean_text(job_text)

    resume_words = [w for w in resume.split() if len(w) > 2]
    job_words = [w for w in job.split() if len(w) > 2]

    resume_counts = Counter(resume_words)
    job_counts = Counter(job_words)

    common = set(resume_counts.keys()) & set(job_counts.keys())
    scored = [(w, min(resume_counts[w], job_counts[w])) for w in common]
    scored.sort(key=lambda x: (-x[1], x[0]))

    return scored[:top_n]
