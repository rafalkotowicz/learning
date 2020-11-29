def xor(a, b):
    # Write your code here
    if a and b or (not a and not b):
        return False
    else:
        return a or b


# if __name__ == '__main__':
#     a1 = 0
#     a2 = []
#     print(f'Test A: {xor(a1, a2)}')
#
#     b1 = 1
#     b2 = 1, 1j
#     print(f'Test B: {xor(b1, b2)}')
#
#     c1 = 'cytrynka'
#     c2 = 0
#     print(f'Test C: {xor(c1, c2)}')
#
#     d1 = 0
#     d2 = 'dupa'
#     print(f'Test D: {xor(d1, d2)}')
