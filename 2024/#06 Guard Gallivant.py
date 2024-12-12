#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
--- Advent of Code 2024                    ---
--- Day 06: Guard Gallivant                ---
----------------------------------------------

Created: Fri Dec  6 07:53:34 2024
Author : Kim Sieber
"""
import time

class class_guard():
    ### turning-order: 0=up, 1=right, 2=down, 3=left, 4=up(=0)
    directions = ([ 0,-1], [ 1, 0], [ 0, 1], [-1, 0], [ 0,-1])

    def __init__(self, map_source: list):
        self.mapp        = map_source 
        self.start_pos   = self.get_guard_position()
        self.pos         = self.start_pos                  # =[x,y]
        self.direction   = [ 0,-1]                         # =[+/-x, +/-y]  (always start with up)
        self.visited     = [(self.pos, self.direction)]
        self.obstruction = ()
        
        
    def get_guard_position(self) -> list:
        for y, line in enumerate(self.mapp):
            for x, value in enumerate((line)):
                if value == "^":
                    return [x,y]
        
        
    #####################
    ## return-values: "oom"=out of map, "loop"=detected, "ok"=move successfull
    def move(self) -> str:
        ### Simulate next field
        pos_next = (self.pos[0] + self.direction[0], self.pos[1] + self.direction[1])
        if self.check_out_of_map(pos_next):       return "oom"
        ### Check next field, turning oder moving
        if self.mapp[pos_next[1]][pos_next[0]] == "#" or \
           self.obstruction == pos_next                   :
            self.turn()
        else:
            self.pos = pos_next
            if self.check_loop():                 return "loop"
            self.visited.append((self.pos, self.direction))
        return "ok"
    
            
    def turn(self):
        key = self.directions.index(self.direction)
        self.direction = self.directions[key+1]

            
    def get_visited_unique(self) -> int:
        visited_pos    = [pos[0] for pos in self.visited]
        visited_unique = []
        for v in visited_pos:
            if v not in visited_unique:
                visited_unique.append(v)
        return visited_unique
    
    
    def set_obstruction_next(self, pos_set: tuple) -> bool:
        ### check if position to set is a wall
        if self.mapp[pos_set[1]][pos_set[0]] == "#":
            return False
        ### remember additional wall
        self.obstruction = pos_set
        return True
    
    
    def check_loop(self) -> bool:
        if (self.pos, self.direction) in self.visited:
            return True
        return False
    
    
    def check_out_of_map(self, pos2check: list) -> bool:
        if pos2check[0] < 0 or pos2check[0] >= len(self.mapp[0])    or \
           pos2check[1] < 0 or pos2check[1] >= len(self.mapp):
            return True
        return False
    
    
    
Puzzle = "#06 Puzzle.txt"
#Puzzle = "#06 Test.txt"

map_source = [list(line) for line in open(Puzzle, "r").read().splitlines()]


############## PART  I #####################
start_time = time.time()
guard      = class_guard(map_source)
while guard.move() == "ok":
    pass
execution_time = time.time() - start_time
visited_unique = guard.get_visited_unique()
print(f"PART  I: The guard visit so many distinct positions ({execution_time:.10f}s): {len(visited_unique)}")  # 5531


############## PART II #####################
start_time  = time.time()
count_loops = 0
for v in visited_unique:
    guard = class_guard(map_source)
    guard.set_obstruction_next(v)
    while True:
        ret = guard.move()
        if ret == "oom":
            break
        if ret == "loop":
            count_loops += 1
            break
        
execution_time = time.time() - start_time
print(f"PART II: Different positions for an obstruction     ({execution_time:.10f}s): {count_loops}")  # 2165 