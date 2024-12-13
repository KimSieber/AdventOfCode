#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
--- Advent of Code 2024                    ---
--- Day 12: Garden Groups                  ---
----------------------------------------------

Created: Thu Dec 12 16:53:06 2024
Author : Kim Sieber

Types of variables:
    grid[0..n][0..n]      (str) = Area-Letter
         +----------------------> y-axis
               +----------------> x-axis
    grid_done[0..n][0..n] (str) = "." if not done, Garden-Letter, if done
    gardens[0..n][0..3]            = List of found gardens
                 +->[0]      (str) -> Garden-Name/Letter, e.g. "A", "B", ...
                 +->[1]      (int) -> Size of area with number of plants in it
                 +->[2]      (int) -> PART I: number of needed perimeters
                 +->[3][0..n]      = List of plants with coordinates in a tuple (x,y)
     
"""
import time

Puzzle = "#12 Puzzle.txt"
#Puzzle = "#12 Test3.txt"

grid      = [list(line) for line in open(Puzzle, "r").read().splitlines()]
grid_done = [list("."*len(grid[0])) for _ in range(len(grid))]
neighbors = ((0,-1),(+1,0),(0,+1),(-1,0))     # x/y-shift


def detect_garden(_pos: tuple[int,int], depth: int) -> tuple[str, int, int, list[tuple[int,int]]]:
    global grid, grid_done

    def check_neighbor(_name: str, x: int, y: int, depth: int) -> tuple[str, int, int, list[tuple[int,int]]]:
        global grid, grid_done
        if x<0 or y<0 or x>= len(grid[0]) or y>=len(grid):  return ("oom", 0, 1, [])    # out of map
        if grid[y][x] == _name:
            if grid_done[y][x] == ".":                      return detect_garden((x,y), depth+1)
            else:                                           return ("", 0, 0, [])
        else:  # foreign neighbor
            if grid_done[y][x] == ".":                      return ("", 0, 1, [])
            else:                                           return ("", 0, 1, [])
            
    x, y            = _pos
    _name           = grid[y][x]
    _area, _peri    = 1, 0
    _xy             = [_pos]
    grid_done[y][x] = _name
    ### check every border
    for shift in neighbors:
        n, a, p, xy = check_neighbor(_name, x+shift[0], y+shift[1], depth)
        _area  += a
        _peri  += p
        _xy.extend(xy)    
    return (_name, _area, _peri, _xy)
    
    
def get_list_of_gardens() -> list[tuple[str, int, int, list[tuple[int,int]]]]:
    global grid, grid_done
    _gardens = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid_done[y][x] == ".":
                _gardens.append(detect_garden((x,y),1))
    return _gardens
    
    
def get_price_of_fences(_gardens: list[tuple[str, int, int, list[tuple[int,int]]]]) -> int:
    _price = 0
    for garden in _gardens:
        _price += garden[1] * garden[2]
    return _price
    
    
#################### PART  I ##################
start_time = time.time()
gardens = get_list_of_gardens()
print(f"PART  I: ({(time.time()-start_time):.10f}s): {get_price_of_fences(gardens)}")


#################### PART II ##################
"""
Thank's to @Korred at Github for the idea to count the corners !
    Outer Corners:           Inner Corners:
    (X = corner, # = plant)  (X = corner, # = plant)

    1)  X.     2)  .X        5)  ##     6)  ##
        .#         #.            #X         X#

    3)  .#     4)  #.        7)  ##     8)  ##
        X.         .X            X#         #X
"""
start_time = time.time()

def cound_corners(_garden: tuple[str, int, int, list[tuple[int,int]]]) -> int:
    
    def _grid(x:int, y:int) -> str:
        if x<0 or y<0 or x==len(grid[0]) or y==len(grid): return ""
        else:                                             return grid[y][x]
        
    global grid
    corner = 0
    for x, y in _garden[3]:
        plant = _garden[0]
        diff = [(1,1),(-1,-1),(-1,1),(1,-1)]
        for sx, sy in diff:
            ### Outer corners
            if _grid(x,y+sy) != plant and _grid(x+sx,y) != plant:
                corner += 1
            ### Inner corners
            if _grid(x,y+sy) == plant and _grid(x+sx,y) == plant and _grid(x+sx,y+sy) != plant:
                corner += 1
    return corner


def get_price_of_fences_ii(_gardens: list[tuple[str, int, int, list[tuple[int,int]]]]) -> int:
    _price = 0
    for garden in _gardens:
        #print()
        number_of_sides = cound_corners(garden)
        #print (f"+--> garden:{garden} -> number_of_sides: {number_of_sides}")
        _price += garden[1] * number_of_sides
    return _price


print(f"PART II: ({(time.time()-start_time):.10f}s): {get_price_of_fences_ii(gardens)}")

    