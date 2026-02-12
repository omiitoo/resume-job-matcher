from utils import calculate_similarity

def get_multiline_input(prompt):
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

print(f"\nMatch Score: {score}%")
