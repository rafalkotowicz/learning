import random


def validate_input(user_choice):
    if user_choice in ['rock', 'paper', 'scissors', '!exit']:
        return True
    else:
        print('Invalid input')
        return False


def print_result(user_choice, computer_choice):
    if (user_choice == 'rock' and computer_choice == 'paper') or \
            (user_choice == 'scissors' and computer_choice == 'rock') or \
            (user_choice == 'paper' and computer_choice == 'scissors'):
        print(f'Sorry, but the computer chose {computer_choice}')
    elif user_choice == computer_choice:
        print(f'There is a draw ({user_choice})')
    else:
        print(f'Well done. The computer chose {computer_choice} and failed')


if __name__ == '__main__':
    while True:
        user_input = input().strip()
        if not validate_input(user_input):
            continue
        if user_input == '!exit':
            exit(0)
        computer_input = random.choice(['rock', 'paper', 'scissors'])
        print_result(user_input, computer_input)
