#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
--- Advent of Code 2024                    ---
--- Day 14: Restroom Redoubt               ---
----------------------------------------------

Created: Sat Dec 14 06:40:56 2024
Author : Kim Sieber

Types of variables:
    robots[0..n]     = class robot with:
                           (px, py) = position
                           (vx, vy) = velosity
                           (sx, sy) = space - len of grid
     
"""
import time

Puzzle = "#14 Puzzle.txt"
space  = (101,103)
#Puzzle = "#14 Test.txt"
#space  = (11,7)

lines = open(Puzzle, "r").read().splitlines()


class robot():
    def __init__(self, _line: str, _space: tuple[int,int]):
        self.px, self.py, self.vx, self.vy = self.extract_robot(_line) 
        self.sx, self.sy                   = _space
        
    def extract_robot(self, _line:str) -> tuple[int,int,int,int]:
        rob = ([[int(v) for v in p.strip("pv=").split(",")] for p in _line.split(" ")])
        return rob[0][0], rob[0][1], rob[1][0], rob[1][1]
    
    def print_robot(self):
        print(f"Robot: p=({self.px},{self.py}) v=({self.vx},{self.vy}) space=({self.sx},{self.sy}))")
        
    def move(self, _repetitions: int):
        self.px += self.vx * _repetitions
        self.py += self.vy * _repetitions
        self.px = self.px % self.sx
        self.py = self.py % self.sy
        
    def quadrant(self):
        if self.px < int(self.sx/2) and self.py < int(self.sy/2): return [1,0,0,0]
        if self.px > int(self.sx/2) and self.py < int(self.sy/2): return [0,1,0,0]
        if self.px < int(self.sx/2) and self.py > int(self.sy/2): return [0,0,1,0]
        if self.px > int(self.sx/2) and self.py > int(self.sy/2): return [0,0,0,1]
        else: return [0,0,0,0]
        

############### PART  I ##################
start_time = time.time()
robots     = [robot(line, space) for line in lines]
for r in robots: r.move(100)
quadrants = [0,0,0,0]
for r in robots:
    q = r.quadrant()
    for i in range(4):
        quadrants[i] += q[i]

safty_factor = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
print(f"PART  I: ({(time.time()-start_time):.10f}s): {safty_factor}")


############### PART II ##################
##### Print Grids/spaces with accumulation of robots
##### search visual by your eyes for the easter egg.
def print_grid(_robots, _space):
    grid = [['.' for _ in range(space[0])] for _ in range(space[1])]
    #print(f"grid:{grid}")
    for r in _robots:
        #print (f"(px,py):({r.px},{r.py})")
        if grid[r.py][r.px] == '.':
            grid[r.py][r.px]  = '1'
        else:
            grid[r.py][r.px] = str(int(grid[r.py][r.px]) + 1)
    print("="*space[0])
    for line in grid:
        #print(f"line:{line}")
        pl = "".join(line)
        print(f"{pl}")
    

start_time = time.time()
robots2    = [robot(line, space) for line in lines]

for i in range (10000):
    pos_all = []
    for r in robots2:  
        r.move(1)
        pos_all.append((r.px, r.py))
        
    ### look for robots with direkt neighbors
    neighbors = 0
    for r in robots2:
        if (r.px+1, r.py) in pos_all or \
           (r.px-1, r.py) in pos_all or \
           (r.px, r.py+1) in pos_all or \
           (r.px, r.py-1) in pos_all        :
            neighbors += 1
    if neighbors > len(robots)*0.4:       # try with different shares
        print_grid(robots, space)
        print(f"neighbors:{neighbors} i:{i}")
    

print(f"PART II: ({(time.time()-start_time):.10f}s): 7916") 