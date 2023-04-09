def append(list1: [], list2: []) -> []:
    for element in list2:
        list1.append(element)

    return list1


def concat(lists: []) -> []:
    result = []
    for lst in lists:
        for element in lst:
            result.append(element)
    return result


def filter(function, list: []) -> []:
    result = []
    for element in list:
        if function(element):
            result.append(element)
    return result


def length(list: []) -> int:
    count: int = 0
    for _ in list:
        count += 1
    return count


def map(function, list: []) -> []:
    result = []
    for element in list:
        result.append(function(element))
    return result


def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)
    return initial


def foldr(function, list: list, initial):
    list = reverse(list)

    for item in list:
        initial = function(item, initial)
    return initial


def reverse(my_list: []) -> []:
    length = len(my_list)
    for i in range(length // 2):
        temp = my_list[i]
        my_list[i] = my_list[length - i - 1]
        my_list[length - i - 1] = temp
    return my_list
