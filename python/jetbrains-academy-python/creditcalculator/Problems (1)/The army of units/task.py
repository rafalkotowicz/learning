army_in = int(input())
if army_in < 1:
    print("no army")
elif 1 <= army_in <= 9:
    print("few")
elif 10 <= army_in <= 49:
    print("pack")
elif 50 <= army_in <= 499:
    print("horde")
elif 500 <= army_in <= 999:
    print("swarm")
elif army_in >= 1000:
    print("legion")
