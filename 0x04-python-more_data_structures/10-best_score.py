#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None

    a = a_dictionary[0]
    for key in a_dictionary:
        if a_dictionary[key + 1] > a:
            a = a_dictionary[key + 1]
            k = key + 1

    return(k)
