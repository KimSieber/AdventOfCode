#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
--- Advent of Code 2024                    ---
--- Day 18: RAM Run                        ---
----------------------------------------------

Created: Sat Dec 21 21:07:30 2024
Author : Kim Sieber

Variables:
    data[0..n]       = (tuple)  -> (x,y) - coordinate
    grid[0..n][0..n] = (str)    -> value '.' or '#'
         +->Y  +->X
    fields           = { (x,y): score, ... }
"""
import time

Puzzle         = "#18 Puzzle.txt"; grid_dimension, bytes_falling = 71, 1024
#Puzzle         = "#18 Test.txt";   grid_dimension, bytes_falling = 7, 12

X, Y           = 0, 1
shifts         = ( (0,1),(0,-1),(1,0),(-1,0) ) 


data = [[int(n) for n in line.split(',')] for line in open(Puzzle, "r").read().splitlines()]
grid = [['.' for _ in range(grid_dimension)] for _ in range(grid_dimension)]

############ FUNCTIONS ##################
def print_grid():    
    print('='*grid_dimension); 
    for line in grid:     print(''.join(line))
def fSet   (pos: tuple[int,int], value: str):    grid[pos[Y]][pos[X]] = value
def fNewPos(pos: tuple[int,int], shift: tuple[int,int]) -> tuple[int,int]:
    if (pos[Y]+shift[Y] < 0 or pos[Y]+shift[Y] >= grid_dimension or \
        pos[X]+shift[X] < 0 or pos[X]+shift[X] >= grid_dimension or \
        grid[pos[Y]+shift[Y]][pos[X]+shift[X]]  == '#'                                              ):
        return pos
    else:   return (pos[X]+shift[X], pos[Y]+shift[Y])
         
fields = {}
def move(pos: tuple[int,int], score: int):
    global fields, shifts
    if pos in fields.keys() and score >= fields[pos]:  return
    fields[pos] = score
    for s in shifts:             move(fNewPos(pos, s), score+1)

          
############### PART  I ##################
start_time = time.time()
for i in range(bytes_falling): fSet(data[i], "#")
#print_grid()
move((0,0), 0)

print(f"PART  I: ({(time.time()-start_time):.10f}s): {fields[(grid_dimension-1, grid_dimension-1)]}")
# = 436

############### PART II ##################
start_time = time.time()
                              #### manual trying by half the area
for i in range(bytes_falling, 2960): fSet(data[i], "#")

pos = (0,0)
while (grid_dimension-1, grid_dimension-1)  in fields.keys():
    pos    = data[i]
    fSet(pos, "#")
    i     += 1
    fields = {}
    move((0,0),0)

print(f"PART II: ({(time.time()-start_time):.10f}s): {pos[X]},{pos[Y]}")
# =61,50