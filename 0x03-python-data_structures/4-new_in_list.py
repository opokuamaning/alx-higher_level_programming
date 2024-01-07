def new_in_list(my_list, idx, element):
    copy_of_list = my_list.copy()
    if idx > 0 and idx < len(my_list):
        copy_of_list[idx] = element
    return copy_of_list
