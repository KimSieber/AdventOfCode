#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
--- Advent of Code 2024                    ---
--- Day 01: Historian Hysteria             ---
----------------------------------------------

Created: Sun Dec  1 21:06:14 2024
Author : Kim Sieber
"""

file_data          = [line.split("   ") for line in open("#01 Puzzle.txt", "r").read().splitlines()]
left_location_ids  = [int(i[0]) for i in file_data]
right_location_ids = [int(i[1]) for i in file_data]
left_location_ids.sort()
right_location_ids.sort()

########## P A R T   I #########################
sum_distances      = 0
for key, value in enumerate(left_location_ids):
    sum_distances += abs(value - right_location_ids[key])
    
print(f"PART I : The total distance between the list are {sum_distances}")

########## P A R T  II #########################
sum_score          = 0
for value in left_location_ids:
    sum_score += value * right_location_ids.count(value)

print (f"PART II: The similarity score of the two lists is {sum_score}")