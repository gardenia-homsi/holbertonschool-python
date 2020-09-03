#!/usr/bin/python3
import hidden_4
import re
for line in hidden_4:
    for word in line.split():
        if word != re.findall(r'[__]\w+', word):
            print(word)
        
