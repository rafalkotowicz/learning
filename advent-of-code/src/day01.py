with open('../test/resources/day01.txt') as f:
    lines = f.readlines()

    elf_calories = []
    sum = 0
    for line in lines:
        if line == '\n':
            elf_calories.append(sum)
            sum = 0
        else:
            sum += int(line.replace('\n',''))

    first = max(elf_calories)
    elf_calories.remove(first)
    second = max(elf_calories)
    elf_calories.remove(second)
    third = max(elf_calories)
    print(first + second + third)



