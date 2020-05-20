num_sequence = input().split()
to_find = input().strip()
indices = []

for i in range(len(num_sequence)):
    if num_sequence[i] == to_find:
        indices.append(str(i))

if len(indices) == 0:
    print("not found")
else:
    print(" ".join(indices))
