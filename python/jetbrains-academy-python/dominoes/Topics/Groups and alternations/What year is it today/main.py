import re

# put your regex in the variable template
template = r"(\d{1,2})(/\d{1,2}/|\.\d{1,2}\.)(\d{4})"
string = input()
# compare the string and the template
result = re.match(template, string)
if result:
    print(result.group(3))
else:
    print("None")
