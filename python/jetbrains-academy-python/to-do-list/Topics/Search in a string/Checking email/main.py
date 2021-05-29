def check_email(string):
    if " " in string:
        return False
    elif "@" not in string:
        return False
    elif "." not in string[string.find("@") + 2:]:
        return False
    else:
        return True

# print(check_email("My e-mail is: this@example.com"))
# print(check_email("good.email@example.com"))
