sequence = input()
sequence = sequence.split()
for i in range(len(sequence)):
    print(sequence[-1 - i], end=" ")
