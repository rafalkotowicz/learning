import re

template = r'are you ready??.?.?'
result = re.match(template, input())
if result:
    print(len(result.group()))
else:
    print(0)
