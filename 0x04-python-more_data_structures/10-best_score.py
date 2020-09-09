#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None

    a = a_dictionary[0]
    for i in a_dictionary:
        if a_dictionary[i + 1] > a:
            a = a_dictionary[i+1]

    return(a)
