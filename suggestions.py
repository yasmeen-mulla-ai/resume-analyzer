def get_suggestions(
    score,
    missing_skills
):

    suggestions = []

    if score < 60:

        suggestions.append(
            "Add more technical skills"
        )

    if len(missing_skills) > 0:

        suggestions.append(
            "Learn missing skills"
        )

    suggestions.append(
        "Use action verbs"
    )

    suggestions.append(
        "Add measurable achievements"
    )

    return suggestions