num_sequence = input().split()
to_find = input().strip()
indices = []

j = 0
for i in num_sequence:
    if i == to_find:
        indices.append(j)
    j += 1

if len(indices) == 0:
    print("not found")
else:
    print(" ".join([str(n) for n in indices]))
