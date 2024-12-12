#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
--- Advent of Code 2024                    ---
--- Day 08: Resonant Collinearity          ---
----------------------------------------------

Created: Mon Dec  9 08:28:59 2024
Author : Kim Sieber

Types of variables:
    signals = {type: [(x,y), (x,y), ...]}
               +--------------------------> frequency
                       +-----+------------> coordinates of antennas
     
"""

Puzzle = "#08 Puzzle.txt"
#Puzzle = "#08 Test.txt"

map_source = [list(line) for line in open(Puzzle, "r").read().splitlines()]


def get_frequences_with_antennas(map_source: list) -> dict:
    signals = {}
    for y in range(len(map_source)):
        for x in range(len(map_source[0])):
            if map_source[y][x] != ".":
                if map_source[y][x] in signals:
                    signals[map_source[y][x]].append((x,y))
                else:
                    signals[map_source[y][x]] = [(x,y)]
    return signals


def check_in_map(map_source: list, coordinate: tuple) -> bool:
    if coordinate[0] < 0 or coordinate[0] >= len(map_source[0]) or \
       coordinate[1] < 0 or coordinate[1] >= len(map_source)         :
        return False
    return True


def get_antinodes_list(map_source: list, signals: dict) -> list:
    antinodes = []
    for freq in signals.keys():
        for i in range(len(signals[freq])):
            for j in range(i+1, len(signals[freq])):
                difference_x = signals[freq][i][0]-signals[freq][j][0]
                difference_y = signals[freq][i][1]-signals[freq][j][1]
                an1 = (signals[freq][i][0] + difference_x, signals[freq][i][1] + difference_y)
                an2 = (signals[freq][j][0] - difference_x, signals[freq][j][1] - difference_y)
                if check_in_map(map_source, an1): antinodes.append(an1)
                if check_in_map(map_source, an2): antinodes.append(an2)
    return antinodes   
            

def get_antinodes_list_ii(map_source: list, signals: dict) -> list:
    antinodes = []
    for freq in signals.keys():
        antinodes.extend(signals[freq])      # all antennas are antinodes, too !
        for i in range(len(signals[freq])):
            for j in range(i+1, len(signals[freq])):
                difference_x = signals[freq][i][0] - signals[freq][j][0]
                difference_y = signals[freq][i][1] - signals[freq][j][1]
                diff_x_sum = diff_y_sum = 0
                an1_oom    = an2_oom    = True
                while an1_oom or an2_oom:
                    diff_x_sum += difference_x
                    diff_y_sum += difference_y
                    an1 = (signals[freq][i][0] + diff_x_sum, signals[freq][i][1] + diff_y_sum)
                    an2 = (signals[freq][j][0] - diff_x_sum, signals[freq][j][1] - diff_y_sum)
                    an1_oom = check_in_map(map_source, an1)
                    an2_oom = check_in_map(map_source, an2)
                    if an1_oom: antinodes.append(an1)
                    if an2_oom: antinodes.append(an2)
                    if not an1_oom and not an2_oom: break
    return antinodes   


##################### START   ######################
signals = get_frequences_with_antennas(map_source)

##################### PART  I ######################
locations        = get_antinodes_list(map_source, signals)
unique_locations = list(set(locations))

print(f"Part  I: {len(unique_locations)}")

##################### PART  I ######################
locations        = get_antinodes_list_ii(map_source, signals)
unique_locations = list(set(locations))

print(f"Part II: {len(unique_locations)}")