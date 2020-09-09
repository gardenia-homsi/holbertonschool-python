#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_val = max(a_dictionary.values())
        for key, value in a_dictionary.items():
            if max_val == value:
                return key

    return None
