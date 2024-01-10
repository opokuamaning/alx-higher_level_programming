#!/usr/bin/python3
def best_score(a_dictionary):
    # loop
    if a_dictionary:
        return(max(a_dictionary, key=a_dictionary.get))
