#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
--- Advent of Code 2024                    ---
--- Day 11: Plutonian Pebbles              ---
----------------------------------------------

Created: Wed Dec 11 07:00:56 2024
Author : Kim Sieber

Variables:
    stone = {Number : CountOfNumber, Number: CountOfNumber, ...}
     
"""
import time

Puzzle = "#11 Puzzle.txt"
#Puzzle = "#11 Test.txt"


def get_dict_for_stones(_stones: list[int]) -> dict:
    count_nums = {}
    for stone in _stones:
        if stone in count_nums.keys():
            count_nums[stone] += 1
        else:
            count_nums[stone]  = 1
    return count_nums


def change_stone(stone: int) -> list[int]:
    if stone == 0: return [1]
    len_stone = len(str(stone))
    if (len_stone % 2) == 0:
        return [int(str(stone)[:int(len_stone/2)]),int(str(stone)[int(len_stone/2):])]
    return [stone*2024]
        

def blink_one_time(_stones: dict) -> dict:
    dict_stones_new = {}
    for num in _stones.keys():
        list_new_nums         = change_stone(num)
        for new_num in list_new_nums:
            if new_num in dict_stones_new.keys():
                dict_stones_new[new_num] += 1 * _stones[num]
            else:
                dict_stones_new[new_num] = 1 * _stones[num]
    return dict(dict_stones_new)

def count_stones(_stones: dict) -> int:
    sum_stones = 0
    for value in _stones.values():
        sum_stones += value
    return sum_stones


###################### START   #####################
stones      = [int(stone) for stone in open(Puzzle, "r").read().split(" ")]
dict_stones = get_dict_for_stones(stones[:])


###################### PART  I #####################
start_time = time.time()
dict_stones_part_i = dict(dict_stones)
for i in range(25):
    dict_stones_part_i = blink_one_time(dict(dict_stones_part_i))

print(f"PART  I ({(time.time()-start_time):.10f}s): {count_stones(dict_stones_part_i)}")
print(f">       Count of different numbers: {len(dict_stones_part_i.keys())}")
print()
###################### PART II #####################
start_time = time.time()
dict_stones_part_ii = dict(dict_stones)
for i in range(75):
    dict_stones_part_ii = blink_one_time(dict(dict_stones_part_ii))

print(f"PART II ({(time.time()-start_time):.10f}s): {count_stones(dict_stones_part_ii)}")
print(f">       Count of different numbers: {len(dict_stones_part_ii.keys())}")

        

""" #################### OLD PART I need to long (83 sec.) ########
def blink(stones: list[int]):
    for i in range(len(stones))[::-1]:
        new_stones = change_stone(stones[i])
        end_stone_line = stones[i+1:]
        stones = stones[:i]
        stones.extend(new_stones)
        stones.extend(end_stone_line)
    return stones
        
        
###################### PART  I #####################
start_time = time.time()
blinked_stones = stones[:]
for _ in range(25):
    blinked_stones = blink(blinked_stones[:])

print(f"PART  I ({(time.time()-start_time):.10f}s): {len(blinked_stones)}")
print ()

###################### PART  I  not possible with this running time #######

"""