#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
--- Advent of Code 2024                    ---
--- Day 09: Disk Fragmenter                ---
----------------------------------------------

Created: Mon Dec  9 12:29:37 2024
Author : Kim Sieber

Types of variables for PART II:
    disc_stats[0..n] = list -> [Type, Size, ID]
                                 +---------------> F = File, E = Empty (.)
                                       +---------> Size / Length
                                             +---> File-ID (only if File)
"""

Puzzle = "#09 Puzzle.txt"
#Puzzle = "#09 Test.txt"

disc_map         = list(open(Puzzle, "r").read())


def get_decompressed_disc(disc_map: list[int]) -> list[str]:
    disc_decomp = []
    is_data         = True
    ID              = 0
    for s in disc_map:
        if is_data:
            disc_decomp.extend([str(ID)] * int(s))
            ID += 1
        else:
            disc_decomp.extend(["."]     * int(s))
        is_data = (is_data+1)%2                       # convert boolean
    return disc_decomp
    

def get_defragmented_disc(disc: list[str]) -> list[str]:
    disc_defrag = []
    for i in range(len(disc)):
        ### delete "." at the end of list
        while disc[-1] == ".":
            disc.pop(-1)
        if i >= len(disc): break     # because length decrease
        if disc[i] == ".":
            disc_defrag.append(disc.pop(-1))
        else:
            disc_defrag.append(disc[i])
    return disc_defrag
    

def get_checksum(disc_defrag: list[str]) -> int:
    checksum = 0
    for i in range(len(disc_defrag)):
        if disc_defrag[i] == ".": value = 0
        else:                     value = int(disc_defrag[i])
        checksum += i * value
    return checksum
    
    
##################### PART  I   ####################
disc_decompressed  = get_decompressed_disc(disc_map[:])    
disc_defragmented  = get_defragmented_disc(disc_decompressed[:])
checksum_I         = get_checksum(disc_defragmented[:])

print (f"PART  I: {checksum_I}")   # 6446899523367


### convert disc_map to static: e.g. [['F', 2, 0], ['E', 3], ['F', 3, 1], ...]
def get_defined_disc(disc_map: list[int]) -> list[list[str, int, int]]:
    disc_stats = []
    is_data    = True
    ID         = 0
    for s in disc_map:
        if is_data:
            disc_stats.append(["F", int(s), ID])
            ID += 1
        else:
            disc_stats.append(["E", int(s)])
        is_data = (is_data+1)%2                       # convert boolean
    return disc_stats


def get_defragmented_disc_II(disc_def: list[list[str, int, int]]) -> list[list[str, int, int]]:
    for e in range(len(disc_def))[::-1]:
        if disc_def[e][0] == "F":
            for b in range(e): 
                if disc_def[b][0] == "E"              and \
                   disc_def[b][1] >= disc_def[e][1]       :

                    file_to_move   = disc_def[e][:]
                    disc_def[e]    = ["E", disc_def[e][1]]
                    disc_def[b][1] = disc_def[b][1] - file_to_move[1]
                    disc_def.insert(b, file_to_move)
                    break
    return disc_def
            

def expand_disc(disc: list[list[str, int, int]]) -> list[str]:
    disc_exp = []
    for d in range(len(disc)):
        if disc[d][1] > 0:
            if disc[d][0] == "E":
                disc_exp.extend(["." for _ in range(int(disc[d][1]))])
            else:   # = "F"
                disc_exp.extend([str(disc[d][2]) for _ in range(int(disc[d][1]))])
    return disc_exp


##################### PART  II  ####################
disc_defined = get_defined_disc(disc_map[:])
disc_defragmented_II = get_defragmented_disc_II(disc_defined[:])
disc_expanded        = expand_disc(disc_defragmented_II[:])
checksum             = get_checksum(list(disc_expanded[:]))

print (f"PART II: {checksum}")   # 6478232739671