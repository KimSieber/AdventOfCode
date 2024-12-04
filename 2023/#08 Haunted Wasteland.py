#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
--- Advent of Code 2023                    ---
--- Day 8: Haunted Wasteland               ---
----------------------------------------------

Created: Sun Nov 10 16:12:48 2024
@author: Kim Sieber

Types of variables:
    Commands[0..n]  = 0 (for left), 1 (for right)
    Node            = e.g. "AAA", "2A4", "ZZZ", "GHZ", "UWQ", ...
    Maps{node: [leftnode, rightNode], ...}
    
Lösungsweg PARTII:
    Sucht für jede Start-Node die Anzahl der Steps, bis Endenode mit Endung "Z"
    erstmals gefunden wird und speichert diese Anzahl Steps je Start-Node in einer Liste.
    Am Ende wird gemeinsamer Nenner (LCM) für die Liste der Steps ermittelt.
     
"""

def readFile(FileName: str) -> (list, dict):
    Lines    = open(FileName, "r").read().splitlines()
    Commands = [0 if cmd=="L" else 1 for cmd in Lines[0]]
    Maps     = {}
    for i in range(2,len(Lines)):
        Key    = Lines[i].split("=")[0].strip()
        Values = Lines[i].split("=")[1].strip(" ()").split(", ")
        Maps[Key] = Values
    return Commands, Maps

        
def exitDessertI(Commands: list, Maps: dict, StartNode: str, EndEndsWith: str) -> int:
    NextNode     = StartNode 
    LenCmdBits   = len(Commands)
    CmdPos       = 0
    Cnt          = 0
    while not NextNode.endswith(EndEndsWith): 
        NextNode    = Maps[NextNode][Commands[CmdPos % LenCmdBits]]
        Cnt        += 1
        CmdPos     += 1
    return Cnt


def exitDessertII(Commands: list, Maps: dict) -> int:
    def final_lcm(nums: list) -> int:
        import math
        fn = 1
        for num in nums:
            fn = math.lcm(fn, num)
        return fn
    
    StartNodes   = [node for node in Maps if node.endswith("A")]
    NodesSteps   = []
    for StartNode in StartNodes:
        NodesSteps.append( exitDessertI(Commands, Maps, StartNode, "Z") )
    return final_lcm(NodesSteps)


################## S T A R T ##################
Commands, Maps   = readFile("#08 Puzzle.txt")

################## P A R T  I  ####################
#Commands, Maps = readFile("#08 Test 1.txt")
StepsI           = exitDessertI(Commands, Maps, "AAA", "ZZZ")
print (f"PART I : You need {StepsI} Steps to leave the desert.")

################## P A R T  II ####################
#Commands, Maps = readFile("#08 Test 3.txt")
StepsII          = exitDessertII(Commands, Maps)
print (f"PART II: You need {StepsII} Steps to leave the desert.")

# 10241191004509