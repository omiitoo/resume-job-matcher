import streamlit as st
from utils import calculate_similarity, extract_common_keywords, get_match_level

st.set_page_config(page_title="Resume Job Matcher", page_icon="🧠", layout="centered")

st.title("🧠 Resume–Job Match Analyzer")
st.write("Paste your resume and a job description to get a match score + keywords.")

resume = st.text_area("Resume text", height=220, placeholder="Paste your resume here...")
job = st.text_area("Job description", height=220, placeholder="Paste the job description here...")

col1, col2 = st.columns(2)

with col1:
    top_n = st.slider("Top keywords", min_value=5, max_value=20, value=10, step=1)

with col2:
    show_keywords = st.checkbox("Show keywords", value=True)

if st.button("Calculate match"):
    if not resume.strip() or not job.strip():
        st.warning("Please paste both resume text and job description.")
    else:
        score = calculate_similarity(resume, job)
        level = get_match_level(score)

        st.subheader("Result")
        st.metric("Match Score", f"{score}%")
        st.write(f"**Level:** {level}")

        if show_keywords:
            keywords = extract_common_keywords(resume, job, top_n=top_n)
            st.write("**Top matching keywords:**")
            if keywords:
                st.write(", ".join([w for w, _ in keywords]))
            else:
                st.write("(none found)")
