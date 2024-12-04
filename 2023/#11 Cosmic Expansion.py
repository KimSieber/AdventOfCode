#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
--- Advent of Code 2023                    ---
--- Day 11: Cosmic Expansion               ---
----------------------------------------------

Created: Sun Nov 17 18:55:59 2024
@author: Kim Sieber

Types of variables:
    Cosmic[0..n][0..n]  = (->str) "." (Space)or "#" (Galaxy)
           +------------> y-Coordinate
                 #------> x-Coordinate
    Galaxies[0..n]      = [x,y] (->int,int), Coordinate of Galaxy
    Combinations[0..n]  = [1st, 2nd, PathWidth]
                           +----+--------------> ID of Galaxies-List
                                     +---------> Shortest Path between these Galaxies
     
"""

class CosmicExpansion:
    
    def __init__ (self, FileName: str, ExpensionWith = 1):
        self.Cosmic           = [list(s) for s in open(FileName, "r").read().splitlines()]
        self.ExpensionWidth   = ExpensionWith
        self.Galaxies         = self.getGalaxyList()
        self.EmptyLines       = self.getEmptyLines()
        self.Combinations     = [[i, j] for i in range(len(self.Galaxies)) \
                                        for j in range(i, len(self.Galaxies)) \
                                        if i != j]
        self.addPathOnCombinations()   
        
        
    def getEmptyLines(self) -> list:
        Columns = []
        Rows    = []
        ### Columns
        for x in range(len(self.Cosmic[0])-1,-1,-1):
            if all ( [Line[x]=="." for Line in self.Cosmic] ):
                Columns.append(x)
        ### Rows
        for y in range(len(self.Cosmic)-1,-1,-1):
            if all( [v=="." for v in  self.Cosmic[y] ]):
                Rows.append(y)
        return {'rows': Rows, 'columns': Columns}


    def getGalaxyList(self) -> list:
        Galaxies = []
        for y in range(len(self.Cosmic)):
            for x in range(len(self.Cosmic[y])):
                if self.Cosmic[y][x] == "#":    
                    Galaxies.append([x,y])
        return Galaxies


    def addPathOnCombinations(self):
        for i, Comb in enumerate(self.Combinations):
            DiffX  = abs(self.Galaxies[Comb[0]][0] - self.Galaxies[Comb[1]][0])
            DiffX += self.ExpensionWidth * self.getQuantityEmptyLinesOfRange('column',     \
                                               self.Galaxies[Comb[0]][0], self.Galaxies[Comb[1]][0])
            DiffY  = abs(self.Galaxies[Comb[0]][1] - self.Galaxies[Comb[1]][1])
            DiffY += self.ExpensionWidth * self.getQuantityEmptyLinesOfRange('row',  \
                                               self.Galaxies[Comb[0]][1], self.Galaxies[Comb[1]][1])
            self.Combinations[i].append(DiffX + DiffY)


    def getQuantityEmptyLinesOfRange(self, Type: str, RangeBegin: int, RangeEnd: int) -> int:
        Cnt = 0
        if RangeBegin > RangeEnd:
            temp_begin = RangeBegin
            RangeBegin = RangeEnd
            RangeEnd   = temp_begin
        for c in range(RangeBegin, RangeEnd, 1):
            if Type == 'row':
                if c in self.EmptyLines['rows']:
                    Cnt += 1
            if Type == 'column':
                if c in self.EmptyLines['columns']:
                    Cnt += 1
        return Cnt
    

    def getSumOfPath(self):
        return int(sum([c[2] for c in self.Combinations]))


################## S T A R T ####################
import datetime
print (f"Starttime: {datetime.datetime.now()}")
#CE = CosmicExpansion(("#11 Test.txt"))
CE = CosmicExpansion("#11 Puzzle.txt")
print (f"PART I : Sum of all length of every pair of galaxies: {CE.getSumOfPath()}")

#CE = CosmicExpansion(("#11 Test.txt", 99))
CE2 = CosmicExpansion("#11 Puzzle.txt", 999999)
   ### 10-times expansions need parameter = 9 (times-1), besause 1st Row/Column exists,
   ### so you need only to add x-times - 1
print (f"PART II: Sum of all length of every pair of galaxies: {CE2.getSumOfPath()}")
print (f"Endtime  : {datetime.datetime.now()}")