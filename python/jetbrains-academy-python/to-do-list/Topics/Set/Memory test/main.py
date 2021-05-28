numbers = input().split()
answers = input().split()

numbers_set = set(numbers)
answers_set = set(answers)

if set(numbers) == set(answers):
    print("True")
else:
    print("False")
