# The following line creates a dictionary from the input. Do not modify it, please
import json

test_dict = json.loads(input())
# test_dict = {"a": 43, "b": 1233, "c": 8}

# Work with the 'test_dict'
minimum = ("", float("inf"))
maximum = ("", float("-inf"))
for key, value in test_dict.items():
    if minimum[1] > value:
        minimum = (key, value)
    elif maximum[1] < value:
        maximum = (key, value)
print(f"min: {minimum[0]}")
print(f"max: {maximum[0]}")
