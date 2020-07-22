# read test_file.txt
my_file = open('test_file.txt', mode='r', encoding='utf-16')
print(my_file.readline())
my_file.close()
