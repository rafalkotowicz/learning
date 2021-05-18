import re

template = r'... Jude'
result = re.match(template, input())
if result:
    print(result.group())
else:
    print('None')
