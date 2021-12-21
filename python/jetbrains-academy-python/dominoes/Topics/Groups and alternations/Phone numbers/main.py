import re

template = r"\+(\d)[- ]*(\d{3})[- ]*(\d{3}[- ]*\d{2}[- ]*\d{2})"


def is_no_match(full_number):
    return re.match(template, full_number) is None


def analyze_phone_number(full_number):
    if is_no_match(full_number):
        print("No match ")
        return

    country_code = re.match(template, full_number).group(1)
    area_code = re.match(template, full_number).group(2)
    number = re.match(template, full_number).group(3)

    print(f"Full number: {full_number}")
    print(f"Country code: {country_code}")
    print(f"Area code: {area_code}")
    print(f"Number: {number}")


analyze_phone_number(input())
