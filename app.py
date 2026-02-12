from utils import calculate_similarity, extract_common_keywords, get_match_level


def get_multiline_input(prompt: str) -> str:
    print(prompt)
    print("(Type END on a new line to finish)\n")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    return "\n".join(lines)


print("=== Resume Job Matcher ===")

resume = get_multiline_input("Paste your resume text:")
job = get_multiline_input("Paste job description:")

score = calculate_similarity(resume, job)
level = get_match_level(score)
keywords = extract_common_keywords(resume, job, top_n=10)

print("\n==========================")
print(f"Match Score: {score}%")
print(f"Level: {level}")

if keywords:
    print("\nTop matching keywords:")
    for w, c in keywords:
        print(f"- {w}")
else:
    print("\nTop matching keywords: (none found)")
print("==========================\n")
