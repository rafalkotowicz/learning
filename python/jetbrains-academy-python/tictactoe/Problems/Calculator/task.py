import sys

first = float(input().strip())
second = float(input().strip())
operation = input().strip()

operations = ["+", "-", "/", "*", "mod", "pow", "div"]
if operation not in operations:
    print("You need to pick operation from the list: +, -, /, *, mod, pow, div")
second_zero_forbidden = ["/", "mod", "div"]
if operation in second_zero_forbidden and second == 0:
    print("Division by 0!")
    sys.exit(0)

if operation == "div":
    print(first // second)
if operation == "/":
    print(first / second)
elif operation == "mod":
    print(first % second)
elif operation == "pow":
    print(first ** second)
elif operation == "+":
    print(first + second)
elif operation == "-":
    print(first - second)
elif operation == "*":
    print(first * second)
