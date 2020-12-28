# -*- coding: utf-8 -*-
"""
@author: nina
"""

import time
start_time = time.time()

f = open('day03.txt', 'r')
txt = f.read()

visited_addresses = {}
position = [0]*2    # x, y
for character in txt:
    if character == '>':
        position[0] += 1
    elif character == '^':
        position[1] += 1
    elif character == '<':
        position[0] -= 1
    elif character == 'v':
        position[1] -= 1
    if (position[0],position[1]) not in visited_addresses:
        visited_addresses[(position[0],position[1])] = 1

print(f"party 1: {len(visited_addresses)}") #2572

visited_addresses_total = {}
position_Santa = [0]*2    # x, y
position_RoboSanta = [0]*2
counter = 0
for character in txt:
    if counter%2 == 0:
        if character == '>':
            position_Santa[0] += 1
        elif character == '^':
            position_Santa[1] += 1
        elif character == '<':
            position_Santa[0] -= 1
        elif character == 'v':
            position_Santa[1] -= 1
        p1 = position_Santa[0]
        p2 = position_Santa[1]
        
    elif counter%2 == 1:
        if character == '>':
            position_RoboSanta[0] += 1
        elif character == '^':
            position_RoboSanta[1] += 1
        elif character == '<':
            position_RoboSanta[0] -= 1
        elif character == 'v':
            position_RoboSanta[1] -= 1
        p1 = position_RoboSanta[0]
        p2 = position_RoboSanta[1]
        
    if (p1,p2) not in visited_addresses_total:
        visited_addresses_total[(p1,p2)] = 1
    counter += 1
    
print(f"party 2: {len(visited_addresses_total)}") #2631
print(f"---{time.time()-start_time} seconds---")