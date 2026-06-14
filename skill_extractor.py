import json

def extract_skills(text):

    with open("data/skills.json") as f:

        skills_data = json.load(f)

    found_skills = []

    text = text.lower()

    for skill in skills_data["skills"]:

        if skill.lower() in text:

            found_skills.append(skill)

    return found_skills