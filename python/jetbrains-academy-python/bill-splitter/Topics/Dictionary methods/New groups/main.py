# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

kids_dict = dict.fromkeys(groups)
fill_no_groups = int(input())
for i in range(0, fill_no_groups):
    kids_dict[groups[i]] = int(input())

print(kids_dict)
