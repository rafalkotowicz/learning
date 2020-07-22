# read sums.txt
my_file = open('sums.txt', mode='r')
for line in my_file:
    numbers = line.split(' ')
    print(int(numbers[0]) + int(numbers[1]))
my_file.close()
