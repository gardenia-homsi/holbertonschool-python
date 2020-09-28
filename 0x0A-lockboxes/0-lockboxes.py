#!/usr/bin/python3
def canUnlockAll(boxes):
    list = [0]
    for i in boxes[0]:
        list.append(i)
    for key in list:
        list.append(Diff(list, boxes[key])
        list=RemoveDup(list)
    if length(list) == lenght(boxes):
        return True
    else:
        return False

                    
def Diff(li1, li2): 
    li_dif=[i for i in li1 + li2 if i not in li1 or i not in li2] 
    return li_dif

def RemoveDup(test_list):
    res=[] 
    for i in test_list: 
        if i not in res: 
            res.append(i) 
    return res
