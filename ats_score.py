def calculate_ats(text, skills):

    score = 0

    if len(text) > 1000:
        score += 30

    score += min(len(skills) * 5, 50)

    if "education" in text.lower():
        score += 5

    if "experience" in text.lower():
        score += 5

    if "skills" in text.lower():
        score += 5

    if "project" in text.lower():
        score += 5

    return min(score, 100)