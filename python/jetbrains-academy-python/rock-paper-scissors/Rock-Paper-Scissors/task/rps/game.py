import random


def is_input_valid(user_choice, all_valid_symbols):
    if user_choice in ['!exit', '!rating'] + all_valid_symbols:
        return True
    else:
        print('Invalid input')
        return False


def determine_winning_symbols(user_choice, all_options):
    index = all_options.index(user_choice)
    except_user_choice = all_options[index + 1:] + all_options[:index]
    return except_user_choice[:int(len(except_user_choice) / 2)]


def get_points(user_choice, computer_choice, all_options):
    winning_set = determine_winning_symbols(user_choice, all_options)
    if computer_choice in winning_set:
        print(f'Sorry, but the computer chose {computer_choice}')
        return 0
    elif user_choice == computer_choice:
        print(f'There is a draw ({computer_choice})')
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

    list_of_options = input()
    if list_of_options == '':
        list_of_options = ['rock', 'paper', 'scissors']
    else:
        list_of_options = list_of_options.split(sep=',')

    print("Okay, let's start")

    while True:
        user_input = input()
        if not is_input_valid(user_input, list_of_options):
            continue
        if user_input == '!exit':
            print('Bye!')
            exit(0)
        if user_input == '!rating':
            print(f'Your rating: {user_score}')
            continue
        computer_input = random.choice(list_of_options)
        user_score += get_points(user_input, computer_input, list_of_options)
