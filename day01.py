# -*- coding: utf-8 -*-
"""
@author: nina
"""

import time
start_time = time.time()

f = open('day01.txt', 'r')
txt = f.read()

floor = 0
for char in txt:
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1 
        
print("party 1: %s" % floor) #280

floor = 0
counter = 0
for char in txt:
    counter += 1
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1
    if floor < 0:
        break
    
print("party 2: %s" % counter) #1797
print("---%s seconds---" % (time.time()-start_time))