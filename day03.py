# -*- coding: utf-8 -*-
"""
@author: nina
"""

import time
start_time = time.time()

f = open('day03.txt', 'r')
txt = f.read()

def change_position(x,y,direction):
    if direction == '>': x += 1
    elif direction == '^': y += 1
    elif direction == '<': x -= 1
    elif direction == 'v': y -= 1
    return[x,y]
    

visited_addresses = set()
position = [0]*2    # x, y
for character in txt:
    [position[0], position[1]] = change_position(position[0], position[1], character)
    if (position[0],position[1]) not in visited_addresses:
        visited_addresses.add((position[0],position[1]))

print(f"party 1: {len(visited_addresses)}") #2572

visited_addresses_total = set()
position_Santa = [0]*2    # x, y
position_RoboSanta = [0]*2
counter = 0
for character in txt:
    if counter%2 == 0:
        [position_Santa[0], position_Santa[1]] = change_position(position_Santa[0], position_Santa[1], character)
        [p1, p2] = [position_Santa[0], position_Santa[1]]       
    elif counter%2 == 1:
        [position_RoboSanta[0], position_RoboSanta[1]] = change_position(position_RoboSanta[0], position_RoboSanta[1], character)
        [p1, p2] = [position_RoboSanta[0], position_RoboSanta[1]]        
    if (p1,p2) not in visited_addresses_total:
        visited_addresses_total.add((p1,p2))
    counter += 1
    
print(f"party 2: {len(visited_addresses_total)}") #2631
print(f"---{time.time()-start_time} seconds---")