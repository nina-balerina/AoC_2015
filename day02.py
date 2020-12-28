# -*- coding: utf-8 -*-
"""
@author: nina
"""

import time
start_time = time.time()

f = open('day02.txt', 'r')
txt = f.readlines()

box_dimensions = []
for line in txt:
    dimensions = line.strip().split('x')
    dimensions_number = []
    for dimension in dimensions:
        dimensions_number.append(int(dimension))
    box_dimensions.append(sorted(dimensions_number))

total_paper_area = 0    
for box in box_dimensions:
    paper_per_box = 3*(box[0]*box[1]) + 2*(box[1]*box[2]) + 2*(box[2]*box[0])
    total_paper_area += paper_per_box

print(f"party 1: {total_paper_area}") #1598415

total_ribbon_length = 0
for box in box_dimensions:
    ribbon_per_box = 2*(box[0]+box[1]) + box[0]*box[1]*box[2]
    total_ribbon_length += ribbon_per_box
    
print(f"party 2: {total_ribbon_length}") #3812909
print(f"---{time.time()-start_time} seconds---")