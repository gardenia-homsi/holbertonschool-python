#!/usr/bin/python3
def canUnlockAll(boxes):
    list = []
    for i in boxes[0]:
        list.append(i)
    for key in list:
        for j in boxes[key]:
            list.append(j)
        list = RemoveDup(list)
    if length(list) == lenght(boxes) - 1:
        return True
    else:
        return False


def RemoveDup(test_list):
    res = []
    for i in test_list:
        if i not in res:
            res.append(i)
    return res
