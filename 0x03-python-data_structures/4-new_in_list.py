def new_in_list(my_list, idx, element):
    copy_of_list = my_list.copy()
    if idx < len(my_list) and idx >= 0:
        copy_of_list[idx] = element
    return copy_of_list
