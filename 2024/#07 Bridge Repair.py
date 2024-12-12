#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
--- Advent of Code 2024                    ---
--- Day 07: Bridge Repair                  ---
----------------------------------------------

Created: Sun Dec  8 22:44:52 2024
Author : Kim Sieber

Types of variables:
     
"""
import itertools

Puzzle = "#07 Puzzle.txt"
#Puzzle = "#07 Test.txt"

def import_file(file_name: str) -> dict:
    data  = {}
    lines = open(file_name, "r").read().splitlines()
    for line in lines:
        key, value_line = line.split(":")
        values      = [int(value) for value in value_line.strip().split(" ")]
        data[int(key)] = values
    return data

def check_combination(key: int, values: list) -> bool:
    operator_combinations = list(itertools.product(["0", "1"], repeat=len(values)-1)) #Bit-Combinations, e.g. 001,010,011,...
    for operator_set in operator_combinations:
        result = values[0]
        for i in range(len(operator_set)):
            if operator_set[i] == "0":
                result += values[i+1]
            else:
                result *= values[i+1]
        if result == key:
            return True
    return False


################# S T A R T #######################
data = import_file(Puzzle)  

################# PART  I   #######################
summ = 0
for key, values in data.items():
    if check_combination(key, values):
        summ += key
    

print(f"PART  I: {summ}")
      

################# PART  II  #######################
def check_combination_II(key: int, values: list) -> bool:
    operator_combinations = list(itertools.product(["0", "1", "2"], repeat=len(values)-1)) #Bit-Combinations, e.g. 001,010,011,...
    for operator_set in operator_combinations:
        result = values[0]
        for i in range(len(operator_set)):
            if operator_set[i] == "0":
                result += values[i+1]
            elif operator_set[i] == "1":
                result *= values[i+1]
            else:
                result = int(str(result)+str(values[i+1]))
        if result == key:
            return True
    return False

summ = 0
for key, values in data.items():
    if check_combination_II(key, values):
        summ += key
        
print(f"PART II: {summ}")