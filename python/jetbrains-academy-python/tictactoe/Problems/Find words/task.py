words = input().split()
print("_".join([word for word in words if word.endswith("s")]))
