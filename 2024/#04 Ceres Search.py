#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
--- Advent of Code 2024                    ---
--- Day 04 - Ceres Search                  ---
----------------------------------------------

Created: Wed Dec  4 20:54:39 2024
Author : Kim Sieber

Types of variables:
    field[0..n]    (str) = line with Characters, e.g.  "MMMSXXMASM"
          +----> y-dimension
                            +----> x-dimension
     
"""
import itertools
 
field = open("#04 Puzzle.txt", "r").read().splitlines()

def check_xmas(field: list, x: int, y: int) -> int:
    def check_direction(add: list) -> bool:
        if (x+(add[0]*3)) >= len(field[0]): return False
        if (x+(add[0]*3)) <  0            : return False
        if (y+(add[1]*3)) >= len(field)   : return False
        if (y+(add[1]*3)) <  0            : return False
        
        if field[y           ][x           ] +            \
           field[y+ add[1]   ][x+ add[0]   ] +            \
           field[y+(add[1]*2)][x+(add[0]*2)] +            \
           field[y+(add[1]*3)][x+(add[0]*3)] == "XMAS":
            return True
        else:
            return False
        
    combinations = list(itertools.product([-1,0,1], [-1,0,1]))
    xmas_count = 0
    for combination in combinations:
        if check_direction(combination) : xmas_count += 1
    return xmas_count
        

################ PART  I #####################
xmas_count = 0
for y in range(len(field)):
    find_x = [x for x in range(len(field[y])) if field[y][x]=="X"]
    for x in find_x:
        xmas_count += check_xmas(field, x, y)
        
print (f"PART  I: How many times does XMAS appear?  : {xmas_count}")
        

################ PART II #####################

def check_X_mas(field: list, x: int, y: int) -> bool:
    if (x+1) >= len(field[0]): return False
    if (x-1) <  0            : return False
    if (y+1) >= len(field)   : return False
    if (y-1) <  0            : return False
    
    if field[y+1][x+1] + field[y  ][x  ] + field[y-1][x-1] in ("MAS", "SAM")   and  \
       field[y+1][x-1] + field[y  ][x  ] + field[y-1][x+1] in ("MAS", "SAM") :
        return True
    else:
        return False
        

mas_count = 0
for y in range(len(field)):
    find_x = [x for x in range(len(field[y])) if field[y][x]=="A"]
    for x in find_x:
        mas_count += 1 if check_X_mas(field, x, y) else 0
    #print(f"check_X_mas(field, {x}, {y}): {check_X_mas(field, x, y)}")
        
print (f"PART II: How many times does X-MAS appear? : {mas_count}")