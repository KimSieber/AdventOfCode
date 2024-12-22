#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
--- Advent of Code 2024                    ---
--- Day 19: Linen Layout                   ---
----------------------------------------------

Created: Sat Dec 21 22:33:40 2024
Author : Kim Sieber

Types of variables:
    towel_pattern[0..n]    = (str) e.g. r, wr, b
    desired_designs[0..n]  = (str) e.g. rrbgbr
    cache                  = {part_of_design: count_solutions} e.g. {'brwru': 4, 'r': 2, ...}


Thank you to Historical_Big_2325 on reddit for the idea of solution
  (https://www.reddit.com/r/adventofcode/comments/1hhlb8g/2024_day_19_solutions/)
     
"""
import time

Puzzle = "#19 Puzzle.txt"
#Puzzle = "#19 Test.txt"

data            = open(Puzzle, "r").read().split('\n\n')
towel_pattern   = [p.strip() for p in data[0].split(",")]
desired_designs = data[1].split("\n")

cache = {}
def test_design(design: str, all_patterns: list[str]) -> int:
    if design in cache:         return cache[design]
    if len(design) == 0:        return 1
    patterns = [p for p in all_patterns if p in design]
    if len(patterns) == 0:
        cache[design] = 0
        return 0
    possible_starts = [p for p in patterns if design.startswith(p)]
    if possible_starts == 0:
        cache[design] = 0
        return 0
    cnt = 0
    for possible_start in possible_starts:
        cnt += test_design(design.removeprefix(possible_start)[:], all_patterns)
    cache[design] = cnt
    return cnt


############### PART  I ##################
start_time = time.time()

all_combinations = [test_design(design[:],towel_pattern) for design in desired_designs]
possible_designs = sum([1 for comb in all_combinations if comb > 0])
print(f"PART  I: ({(time.time()-start_time):.10f}s): {possible_designs}")
# =265 >206


############### PART II ##################
start_time = time.time()

possible_comb    = sum(all_combinations)
print(f"PART II: ({(time.time()-start_time):.10f}s): {possible_comb}")