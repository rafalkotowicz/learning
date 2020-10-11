for i in range(1, 11):
    with open('file' + str(i) + '.txt', 'w', encoding='utf-8') as f:
        f.write(str(i))
