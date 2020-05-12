camel_case = input().strip()

for c in camel_case:
    if c.isupper():
        print("_" + c.lower(), end="")
    else:
        print(c, end="")
