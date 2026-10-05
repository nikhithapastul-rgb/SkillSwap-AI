def find_matches(my_teach_skills, my_learn_skills, users):
    matches = []

    for user in users:

        # Skills you want to learn that the other person can teach
        teach_match = set(my_learn_skills) & set(user["teaches"])

        # Skills you can teach that the other person wants to learn
        learn_match = set(my_teach_skills) & set(user["learns"])

        # Calculate score
        total_possible = len(my_learn_skills) + len(my_teach_skills)
        total_matches = len(teach_match) + len(learn_match)

        if total_possible > 0:
            match_score = round((total_matches / total_possible) * 100)
        else:
            match_score = 0

        # Only show users with at least one mutual skill
        if total_matches > 0:
            matches.append({
                "name": user["name"],
                "teaches": user["teaches"],
                "learns": user["learns"],
                "matched_teach_skills": list(teach_match),
                "matched_learn_skills": list(learn_match),
                "match_score": match_score
            })

    # Highest score first
    matches.sort(key=lambda x: x["match_score"], reverse=True)

    return matches