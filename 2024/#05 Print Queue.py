#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
--- Advent of Code 2024                    ---
--- Day 05: Print Queue                    ---
----------------------------------------------

Created: Thu Dec  5 12:07:12 2024
Author : Kim Sieber

Types of variables:
     
"""

rules_block, updates_block = open("#05 Puzzle.txt", "r").read().split("\n\n")


def format_rules(rules_block: str) -> dict:
    rules_tmp = [[int(page) for page in rule.split("|")] for rule in rules_block.split("\n")]
    rules = {}
    for rule in rules_tmp:
        if rule[0] in rules.keys():
            rules[rule[0]].append(rule[1])
        else:
            rules[rule[0]] = [rule[1]]
    return rules


rules     = format_rules(rules_block)

updates   = [[int(page) for page in update.split(",")] for update in updates_block.split("\n")]


def check_valid_update(update: list, rules: dict) -> bool:
    for key, page in enumerate(update):
        if page in rules:
            if any(r in update[0:key] for r in rules[page]):
                return False
    return True
        

def correction_update(update: list, rules: dict) -> list:
    while not check_valid_update(update, rules):
        for key, page in enumerate(update):
            if page in rules:
                for rule in rules[page]:
                    if rule in update[0:key]:
                        update.insert(update.index(rule), update.pop(key))
                        break
    return update

    
sum_page_numbers                   = 0
sum_page_numbers_correctet_updates = 0
for update in updates:
    if check_valid_update(update, rules):
        mid               = int((len(update)+0.9)/2)
        sum_page_numbers += update[mid]
    else:
        update_corrected                    = correction_update(update.copy(), rules)
        mid                                 = int((len(update_corrected)+0.9)/2)
        sum_page_numbers_correctet_updates += update_corrected[mid]
        

print (f"PART  I: Sum of middle page number of correctly-ordered updates is: {sum_page_numbers}") # 6242
    
print (f"PART II: Sum of middle page number of corrected-ordered updates is: {sum_page_numbers_correctet_updates}") # 5169
    
    
    