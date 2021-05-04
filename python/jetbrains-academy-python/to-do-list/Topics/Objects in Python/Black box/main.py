# use the function blackbox(lst) that is already defined
mah_list = ["Ciekawe", "co", "robi", "blackbox(lst)"]
mah_list_id1 = id(mah_list)
mah_list = blackbox(mah_list)
mah_list_id2 = id(mah_list)
print("modifies" if mah_list_id1 == mah_list_id2 else "new")
