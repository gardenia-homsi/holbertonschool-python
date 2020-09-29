#!/usr/bin/python3
def canUnlockAll(boxes):
    """ function to check the unblocked boxes inside a list of boxes"""
    if len(boxes) == None:
        raise TypeError("boxes can't be NoneType")
    elif len(boxes) == 1:
        return True
    else:
        list = []
        if 0 not is list:
            list.append(0)
        """loop inside list and append new key boxes for the unchecked one"""
        for i in list:
            if i in range(len(boxes)):
                """loop inside each box of boxes list"""
                for j in range(len(boxes[i])):
                    """
                    add only the new unlocked boxes in the list
                    """
                    if boxes[i][j] not in list and boxes[i][j] < len(boxes):
                        list.append(boxes[i][j])
        if len(list) == len(boxes):
            return True
        else:
            return False
