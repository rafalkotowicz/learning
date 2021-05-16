import re

# test = "<START></end>"
# first_tag = re.match(r"<\w+>", test).group()[1:-1]
# print(first_tag)
template = r'<[a-z]+>.*?</[a-z]+>'
# print(re.match(template, test))
