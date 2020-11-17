import random


def is_input_valid(user_choice):
    if user_choice in ['rock', 'paper', 'scissors', '!exit', '!rating']:
        return True
    else:
        print('Invalid input')
        return False


def get_points(user_choice, computer_choice):
    if (user_choice == 'rock' and computer_choice == 'paper') or \
            (user_choice == 'scissors' and computer_choice == 'rock') or \
            (user_choice == 'paper' and computer_choice == 'scissors'):
        print(f'Sorry, but the computer chose {computer_choice}')
        return 0
    elif user_choice == computer_choice:
        print(f'There is a draw ({user_choice})')
        return 50
    else:
        print(f'Well done. The computer chose {computer_choice} and failed')
        return 100


if __name__ == '__main__':
    user_name = input('Enter your name: ')
    user_score = 0
    print(f'Hello, {user_name}')
    with open('rating.txt', 'r') as rating_file:
        for line in rating_file:
            user_with_score = line.split()
            if user_with_score[0] == user_name:
                user_score = int(user_with_score[1])

    while True:
        user_input = input()
        if not is_input_valid(user_input):
            continue
        if user_input == '!exit':
            print('Bye!')
            exit(0)
        if user_input == '!rating':
            print(f'Your rating: {user_score}')
            continue
        computer_input = random.choice(['rock', 'paper', 'scissors'])
        user_score += get_points(user_input, computer_input)
