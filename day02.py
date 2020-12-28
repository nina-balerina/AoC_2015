# -*- coding: utf-8 -*-
"""
@author: nina
"""

import time
start_time = time.time()

f = open('day02.txt', 'r')
txt = f.readlines()


boxes_dimensions = []
for line in txt:
    dimensions = line.strip().split('x')
    boxes_dimensions.append(sorted(int(n) for n in dimensions))


total_paper_area = 0  
total_ribbon_length = 0  
for (l,w,h) in boxes_dimensions: 
    total_paper_area += 3*(l*w) + 2*(w*h) + 2*(h*l)
    total_ribbon_length += 2*(l+w) + l*w*h


print(f"party 1: {total_paper_area}") #1598415
print(f"party 2: {total_ribbon_length}") #3812909
print(f"---{time.time()-start_time} seconds---")