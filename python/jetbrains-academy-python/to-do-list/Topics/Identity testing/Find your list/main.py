def find_my_list(all_lists, my_list):
    for index, lst in enumerate(all_lists):
        if my_list is lst:
            return index
    return None
