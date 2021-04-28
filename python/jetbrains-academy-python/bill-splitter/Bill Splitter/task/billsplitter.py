print("Enter the number of friends joining (including you):")
no_participants = int(input())
if no_participants < 1:
    print("No one is joining for the party")
    exit("invalid number of people")

participants_list = []
print("Enter the name of every friend (including you), each on a new line:")
for i in range(0, no_participants):
    participants_list.append(input())

participants_dict: dict[str, int] = dict.fromkeys(participants_list, 0)

print("Enter the total bill value: ")
bill_total = int(input())
for participant in participants_dict:
    participants_dict[participant] = round(bill_total / len(
        participants_list), 2)

print(participants_dict)
