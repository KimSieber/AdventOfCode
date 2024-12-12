#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
--- Advent of Code 2024                    ---
--- Day 10: Hoof It                        ---
----------------------------------------------

Created: Tue Dec 10 07:10:51 2024
Author : Kim Sieber

Types of variables:
    hiking_trails{(x,y): [(x,y), (x,y), ...], ...}  = trailheads with list of reached peaks
                   +--------------------------------> coordinate of trailhead
                           +------------------------> list of reached peaks (9-height-positions)
     
"""
Puzzle = "#10 Puzzle.txt"
#Puzzle = "#10 Test.txt"


mapp = [[int(height) if height.isdigit() else -1 for height in list(line)] for line in open(Puzzle, "r").read().splitlines()]


def get_all_trailheads(_map: list[list[int]]) -> list[tuple[int,int]]:
    _trailheads = []
    for y, line in enumerate(_map):
        _trailheads.extend([(x,y) for x, height in enumerate(line) if height==0])
    return _trailheads


def get_peak_list_of_trailhead(_map: list[list[int]], _pos: tuple[int, int]) -> list[tuple[int,int]]:
    x,y = _pos
    height = _map[y][x]
    if height == 9: return [(x,y)]
    next_steps = []
    if y+1 < len(_map)   : 
        if _map[y+1][x  ] == height+1: next_steps.append((x  ,y+1))
    if y   > 0           : 
        if _map[y-1][x  ] == height+1: next_steps.append((x  ,y-1))
    if x+1 < len(_map[0]): 
        if _map[y  ][x+1] == height+1: next_steps.append((x+1,y  ))
    if x   > 0           : 
        if _map[y  ][x-1] == height+1: next_steps.append((x-1,y  ))
    if len(next_steps) == 0: return []
    peak_list = []
    for next_step in next_steps:
        peak_list.extend(get_peak_list_of_trailhead(_map[:], next_step[:]))
    return peak_list


################### START ######################
trailheads           = get_all_trailheads(mapp[:])
hiking_trails        = {}
hiking_trails_unique = {}

for trailhead in trailheads:           
    hiking_trails[trailhead]        = get_peak_list_of_trailhead(mapp[:], trailhead[:])
    hiking_trails_unique[trailhead] = list(set(hiking_trails[trailhead[:]]))

score    = sum([len(hiking_trails_unique[key]) for key in hiking_trails_unique])
print(f"PART  I: {score}")

score_ii = sum([len(hiking_trails[key]) for key in hiking_trails])
print(f"PART II: {score_ii}")