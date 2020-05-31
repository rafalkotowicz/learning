max_name = ""
max_cat_no = 0
while True:
    user_input = input().strip()
    if user_input == "MEOW":
        break
    cafe_name, cats_no = user_input.split()
    if int(cats_no) > max_cat_no:
        max_cat_no = int(cats_no)
        max_name = cafe_name
print(max_name)
