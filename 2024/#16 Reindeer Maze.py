#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
--- Advent of Code 2024                    ---
--- Day 16: Reindeer Maze                  ---
----------------------------------------------

Created: Thu Dec 19 21:49:30 2024
Author : Kim Sieber

Types of variables:
    grid[0..n][0..n]    = (str), .=Place, #=Wall, S=Start, E=End
         +--------------> Y-coordinate
               +--------> X-coordinate
    Start               = tuple(int,int)  -> (x,y)
    targets[0..n]       = (int) Score
     
"""
import time

direction = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
dir_next  = ('^', '>', 'v', '<', '^')
X, Y      = L, R  = (0, 1)

routes_per_score = []    # [0..n][score, [(x,y), (x,y)]]
targets          = []
pos_score        = {}

Puzzle = "#16 Puzzle.txt"
#Puzzle = "#16 Test2.txt"


grid = [list(line) for line in open(Puzzle, "r").read().splitlines()]
for y, line in enumerate(grid):
    for x, val in enumerate(line):
        if val == "S": Start = (x,y)


def print_grid(grid):
    print("     0         1        2")
    print("     01234567890123456790")
    for i in range(len(grid)):
        num = ("  " + str(i))[-3:]
        print(f"{num}: {''.join(grid[i])}")


def fNext  (_pos, _nav): return (_pos[X]+direction[_nav][X], _pos[Y]+direction[_nav][Y])
def fGet   (_pos):       return grid[_pos[Y]][_pos[X]]
def fRotate(_nav):       return dir_next[dir_next.index(_nav   )+1]
def fRotRev(_nav):       return dir_next[dir_next.index(_nav, 1)-1]


def move(visited: list[tuple[int,int]], pos: tuple[int,int], nav: str, score: int, dep=1) -> bool:
    global grid, targets, pos_score
    visited.append(pos)
    
    ### Look for most short way for every point, otherwise skip
    if pos in pos_score.keys():
        ### add 1000 to compensate another direction before turning 
        if score < pos_score[pos]+1001:   pos_score[pos] = score
        else:                             return False
    else:                             pos_score[pos] = score

    if fGet(pos) == 'E':   
        targets.append(score)
        routes_per_score.append([score, visited])    # for PART II    
        return True
    
    ### Check every direction
    if fGet(fNext(pos, nav)) in ['.', 'E']:
        move(visited[:], fNext(pos, nav), nav, score+1, dep+1)
    if fGet(fNext(pos, fRotate(nav))) in ['.', 'E']:
        move(visited[:], fNext(pos, fRotate(nav)), fRotate(nav), score+1001, dep+1)
    if fGet(fNext(pos, fRotRev(nav))) in ['.', 'E']:
        move(visited[:], fNext(pos, fRotRev(nav)), fRotRev(nav), score+1001, dep+1)
    return False


############### PART  I ##################
start_time = time.time()
#print_grid(grid)
move([], Start[:], '>', 0)
#print_grid(grid)

print(f"PART  I: ({(time.time()-start_time):.10f}s): {min(targets)}")  


############### PART II ##################
start_time = time.time()

all_pos_best_routes = []
for route in routes_per_score:
    if route[0] == min(targets):
        all_pos_best_routes.extend(route[1])
all_pos_best_routes_unique = list(set(all_pos_best_routes))

print(f"PART II: ({(time.time()-start_time):.10f}s): {len(all_pos_best_routes_unique)}")  


# PART  I: (19.0162382126s): 92432
# PART II: (0.2274560928s): 458