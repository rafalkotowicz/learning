with open('salary.txt', 'r', encoding='utf=8') as file_in, \
        open('salary_year.txt', 'w', encoding='utf=8') as file_out:
    for line in file_in:
        file_out.write(str(int(line.strip()) * 12))
        file_out.write("\n")
