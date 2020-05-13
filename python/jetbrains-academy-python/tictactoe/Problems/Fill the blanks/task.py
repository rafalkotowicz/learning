# for a in x:
#     for el in a:
#         if el > 0:
#             els.append(el)
els = [el for a in x for el in a if el > 0]
