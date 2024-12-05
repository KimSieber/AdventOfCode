#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
--- Advent of Code 2024                    ---
--- Day 03: Mull It Over                   ---
----------------------------------------------

Created: Mon Dec  2 06:35:52 2024
Author : Kim Sieber
"""
corrupt_code = open("#03 Puzzle.txt", "r").read()

def get_result_of_multiplications(corrupt_code):
    result = 0
    next_mul_pos = -1
    while True:
        next_mul_pos = corrupt_code.find("mul(", next_mul_pos + 1)
        if next_mul_pos == -1: break
        next_bracket = corrupt_code.find(")", next_mul_pos)
        if next_bracket == -1: break

        if corrupt_code[next_mul_pos++4:next_bracket].find(" ") > 0:  continue

        number_list = corrupt_code[next_mul_pos++4:next_bracket].split(",")
        if len(number_list) != 2: continue

        if not number_list[0].isdigit() or not number_list[1].isdigit(): continue

        result += int(number_list[0]) * int(number_list[1])
    return result

result = get_result_of_multiplications(corrupt_code)
print (f"PART  I: The results of adding all multiplications is {result}")

stop_disable_pos = 0
while stop_disable_pos < len(corrupt_code):
    start_disable_pos = corrupt_code.find("don't()", stop_disable_pos)
    if start_disable_pos == -1: break

    stop_disable_pos  = corrupt_code.find("do()", start_disable_pos)
    if stop_disable_pos == -1:
        stop_disable_pos = len(corrupt_code)

    #count_disabling   = corrupt_code.count("mul", start_disable_pos, stop_disable_pos)
    corrupt_code      = corrupt_code[:start_disable_pos] + corrupt_code[start_disable_pos:stop_disable_pos].replace("mul", "mux") + corrupt_code [stop_disable_pos:]

result = get_result_of_multiplications(corrupt_code)
print (f"PART II: The results of adding all multiplications is {result}")