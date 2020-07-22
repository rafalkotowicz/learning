scores = input().split()
# put your python code here
# correct = [x for x in scores if x == "C"]
# incorrect = [x for x in scores if x == "I"]

correct = 0
incorrect = 0
for score in scores:
    if score == "C":
        correct += 1
    if score == "I":
        incorrect += 1
        if incorrect >= 3:
            break

if incorrect >= 3:
    print("Game over")
    print(correct)
else:
    print("You won")
    print(correct)
