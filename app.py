from utils import calculate_similarity

print("=== Resume Job Matcher ===")

resume = input("Paste your resume text:\n")
job = input("Paste job description:\n")

score = calculate_similarity(resume, job)

print(f"\nMatch Score: {score}%")
