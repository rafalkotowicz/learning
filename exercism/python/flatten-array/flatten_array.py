def flatten(iterable):
    flatten_list:[] = []
    for item in iterable:
        if item is None:
            continue
        if isinstance(item, list):
            flatten_list.extend(item)
            flatten_list = flatten(flatten_list)
        else:
            flatten_list.append(item)
    return flatten_list
