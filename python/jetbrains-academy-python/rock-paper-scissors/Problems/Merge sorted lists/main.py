def merge_arrays(a, b):
    # "c" will contain the result of merging arrays "a" and "b"
    c = []
    # CHECK that "a" or "b" are not empty
    while a or b:
        # CHECK that "b" is empty, or that "a" and "b" are not empty and compare the elements
        if not b or a and b and a < b:
            # removing the first element from "a" and adding it to "c"
            c.append(a.pop(0))
        else:
            # removing the first element from "b" and adding it to "c"
            c.append(b.pop(0))
    return c

# if __name__ == '__main__':
#     a = [1, 2, 3]
#     b = [2, 3, 4, 4]
#     print(merge_arrays(a, b))
