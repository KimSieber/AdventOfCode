#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
--- Advent of Code 2024                    ---
--- Day 13: Claw Contraption               ---
----------------------------------------------

Created: Fri Dec 13 08:38:43 2024
Author : Kim Sieber

Types of variables:
    maschines[0..n][<button/prize>] = tuple[int,int]
                   ['A']            = (x-shift, y-shift)
                   ['B']            = (x-shift, y-shift)
                   ['P']            = (x-coordinate, y-coordinate) =>Prize
"""
import time

X, Y    = 0, 1
A, B, P = 0, 1, 2

Puzzle = "#13 Puzzle.txt"
#Puzzle = "#13 Test.txt"


def get_claw_maschines(_Puzzle: str) -> list[dict[tuple[int,int]]]:
    data = [d.split("\n") for d in open(_Puzzle, "r").read().split("\n\n")]
    maschines = []
    for m in data:
        maschine = {}
        ### A-Button
        a = m[A].split(" ")
        a[2] = int(a[2].strip(" ,X"))
        a[3] = int(a[3].strip(" ,Y"))
        maschine['A'] = (a[2],a[3])
        ### B-Button
        a = m[B].split(" ")
        a[2] = int(a[2].strip(" ,X"))
        a[3] = int(a[3].strip(" ,Y"))
        maschine['B'] = (a[2],a[3])
        ### Prize
        a = m[P].split(" ")
        a[1] = int(a[1].strip(" =,X"))
        a[2] = int(a[2].strip(" =,Y"))
        maschine['P'] = (a[1],a[2])
        ###
        maschines.append(maschine)        
    return maschines


def get_list_of_ways(_maschine: dict[tuple[int,int]]) -> list[tuple[int,int]]:
    ways = []
    for A in range(int(_maschine['P'][X] / _maschine['A'][X]+1)):    # +1 importent, do not forget the highest factor
        ######### X
        rest = _maschine['P'][X] - (_maschine['A'][X] * A)
        B    = rest / _maschine['B'][X]
        if B == int(B):
            ########## Y
            if (_maschine['A'][Y] * A) + (_maschine['B'][Y] * B) == _maschine['P'][Y]:
                ways.append((A,int(B)))
    return ways
        

def get_minimum_token(_ways: list[tuple[int,int]]) -> int:
    tokens = []
    for way in _ways:
        tokens.append((way[A]*3) + (way[B]*1))
    return min(tokens)


def win_all_prizes(_maschines: list[dict[tuple[int,int]]]) -> int:
    sum_price = 0
    for maschine in maschines:
        ways = get_list_of_ways(maschine)
        if len(ways) > 0:
            sum_price += get_minimum_token(ways)
    return sum_price


################# START ####################
maschines = get_claw_maschines(Puzzle)

############### PART  I ##################
start_time = time.time()
sum_price = win_all_prizes(maschines)

print(f"PART  I: ({(time.time()-start_time):.10f}s): {sum_price}")  # 36838


############### PART II ##################
"""
It takes tooooo much time, so I need another way:
Do some mathematics:
    We are looking for two unknown variables, A and B (both counting pushes on the button)
    So the formulas are:
        A * AX + B * BX = PX
        A * AY + B * BY = PY
    We are now isolating A in the first formula:
        A = (PX - B * BX) / AX
    Now we isolating B in the second formular by using isolated A (without intermediate steps)
        B = (AX * PY - PX * AY) / (AX * BY - BX * AY)

    ==> let it try !
    
    e.g. : get_token_ii({'A': [(94, 34), (22, 67), (8400, 5400) })
"""
def get_token_ii(_maschine: dict[tuple[int,int]]) -> int:
    AX, AY = _maschine['A']
    BX, BY = _maschine['B']
    PX, PY = _maschine['P']
    PX += 10000000000000
    PY += 10000000000000
    B = (AX * PY - PX * AY) / (AX * BY - BX * AY)
    if int(B) != B: return 0
    A = (PX - B * BX) / AX
    if int(A) != A: return 0
    return int(A)*3 + int(B)*1


start_time = time.time()
sum_token_ii = 0
for maschine in maschines:
    sum_token_ii += get_token_ii(maschine)

print(f"PART II: ({(time.time()-start_time):.10f}s): {sum_token_ii}")