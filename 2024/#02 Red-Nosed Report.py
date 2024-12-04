#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
--- Advent of Code 2024                    ---
--- Day 02: Red-Nosed Report               ---
----------------------------------------------

Created: Mon Dec  2 06:35:52 2024
Author : Kim Sieber

Types of variables:
    reports[0..n][0..n]   = (int) Level
            +-------------> report-No.
    reactors[0..n]        = (bool) true = without bad levels or only on bad level (Part II)
"""

def check_level(level: list) -> bool:
    for key in range(1,len(level)):
        if (level[0] < level[-1]):             # level ist increasing
            if (level[key] - level[key-1]) not in [1,2,3]:
                return False
        else:
            if (level[key] - level[key-1]) not in [-1,-2,-3]:
                return False
    return True

reports = [[int(level) for level in line.split(" ")] for line in open("#02 Puzzle.txt", "r").read().splitlines()]

reactors = [check_level(level) for level in reports]
        
print (f"PART  I: There are {reactors.count(True)} safe reactors.")  # 282


def check_level_part_ii(level: list) -> bool:
    if check_level(level): return True
    for key in range(1,len(level)):
        if (level[0] < level[-1]):             # level ist increasing
            if (level[key] - level[key-1]) not in [1,2,3]:
                if check_level(level[:key  ]+level[key+1:]): return True
                if check_level(level[:key-1]+level[key  :]): return True
                return False
        else:
            if (level[key] - level[key-1]) not in [-1,-2,-3]:
                if check_level(level[:key  ]+level[key+1:]): return True
                if check_level(level[:key-1]+level[key  :]): return True
                return False

reactors = [check_level_part_ii(level) for level in reports]
        
print (f"PART II: There are {reactors.count(True)} safe reactors.")  # =349   //not >331, >297, >345
        