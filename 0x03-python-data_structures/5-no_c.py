#!/usr/bin/python3
def no_c(my_string):
    str_len = len(my_string)

    j = 0;
    new_string = my_string[:]

    for i in range(str_len):
        if(my_string[i] == 'C' or my_string[i] == 'c'):
            new_string = new_string[:(i - j)] + my_string[(i + 1):]
            j += 1
    return (new_string)
