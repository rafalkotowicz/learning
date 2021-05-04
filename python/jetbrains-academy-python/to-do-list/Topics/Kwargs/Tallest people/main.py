import collections


def tallest_people(**people):
    tallest = max(people.values())
    filtered = {}
    for person, height in people.items():
        if height == tallest:
            filtered[person] = height
    filtered = collections.OrderedDict(sorted(filtered.items()))
    for person, height in filtered.items():
        print(f"{person} : {height}")
