words = input().split()
addresses = []
for word in words:
    if word.lower().startswith("https://") \
            or word.lower().startswith("http://") \
            or word.lower().startswith("www."):
        addresses.append(word)
print("\n".join(addresses))
