def select_dates(potential_dates):
    matches = []
    for person in potential_dates:
        if person["age"] > 30 and person["city"] == "Berlin" and "art" in \
                person["hobbies"]:
            matches.append(person["name"])

    return ", ".join(matches)
