wrong_name = input()
print("".join([word.capitalize() for word in wrong_name.split("_")]))
