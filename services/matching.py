def find_matches(my_teach_skills, my_learn_skills, users):
    matches = []

    for user in users:
        teach_match = set(my_learn_skills) & set(user["teaches"])
        learn_match = set(my_teach_skills) & set(user["learns"])

        if teach_match and learn_match:
            matches.append({
                "name": user["name"],
                "teaches": user["teaches"],
                "learns": user["learns"],
                "match_score": 100
            })

    return matches