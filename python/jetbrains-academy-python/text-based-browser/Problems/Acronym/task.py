# read test.txt
my_file = open('test.txt', mode='r')
for line in my_file:
    line_chars = list(line)
    print(line_chars[0])
my_file.close()
