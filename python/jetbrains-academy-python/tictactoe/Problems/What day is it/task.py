offset = float(input().strip())

london_time = 10.5

if offset + london_time > 24:
    print("Wednesday")
elif 0 <= offset + london_time < 24:
    print("Tuesday")
elif offset + london_time < 0:
    print("Monday")
