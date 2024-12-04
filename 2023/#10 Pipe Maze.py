#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
--- Advent of Code 2023                    ---
--- Day 10: Pipe Maze                      ---
----------------------------------------------

Created: Sun Nov 17 00:24:53 2024
@author: Kim Sieber

Types of variables:
     Grid[0..n] = (str) a horizontal Gridline, e.g. "|-LJ7F.S ..."  
          +-->  = vertical Gridcolumn
     StartPos[0..1] = Position of Letter "S" 
             [0]    = (int) X->Line
             [1]    = (int) Y->Column
     direction[0..1] = Direction of Pipe, X and Y
                       e.g. [-1,0] or [0,1] or [1,0] ...
     PipeElements[0..n][x,y] = Position of Pipe-Element
   
     Hint for Part II:
         Look up for "Point in Polygom-Algorithm"
"""

class PipeMaze:
    Map = {"|": [[ 0,-1],[ 0, 1]], 
           "-": [[-1, 0],[ 1, 0]],
           "L": [[ 0,-1],[ 1, 0]],
           "J": [[ 0,-1],[-1, 0]],
           "7": [[-1, 0],[ 0, 1]],
           "F": [[ 1, 0],[ 0, 1]],
           "S": [[ 0, 0],[ 0, 0]],
           ".": [[ 0, 0],[ 0, 0]],
           "I": [[ 0, 0],[ 0, 0]],
           "0": [[ 0, 0],[ 0, 0]] }
    
    
    def __init__ (self, FileName: str):
        self.Grid           = [list(s) for s in open(FileName, "r").read().splitlines()]
        self.StartPos       = PipeMaze.getStartPos(self, self.Grid)
        PossibleDirections  = PipeMaze.listPossibleDirections(self, self.Grid, self.StartPos)
        self.StartDirection = PossibleDirections[0]
        ### Prepare for Part II
        self.StartTile      = [key for key in PipeMaze.Map if PipeMaze.Map[key]==PossibleDirections][0]
        self.PipeElements   = []           
        
        
    def getStartPos(self, Grid: list) -> list:
        for y in range(len(Grid[0])):
            if "S" in Grid[y]: return [Grid[y].index("S"),y]
                
                
    def listPossibleDirections(self, Grid: list, StartPos: list) -> list:
        PossibleDirections = []
        if StartPos[0] > 1:
            if Grid[StartPos[1]  ][StartPos[0]-1] in ["-","L","F"]:   # to the left
                PossibleDirections.append([-1, 0])
        if StartPos[0] < len(Grid[0]):
            if Grid[StartPos[1]  ][StartPos[0]+1] in ["-","J","7"]:   # to the right
                PossibleDirections.append([ 1, 0])
        if StartPos[1] > 1:
            if Grid[StartPos[1]-1][StartPos[0]  ] in ["|","7","F"]:   # bottom up
                PossibleDirections.append([ 0,-1])
        if StartPos[1] < len(Grid):
            if Grid[StartPos[1]+1][StartPos[0]  ] in ["|","L","J"]:   # top down
                PossibleDirections.append([ 0, 1])
        return PossibleDirections
                
    
    def countLenOfPipe(self, Grid: list, Pos: list, Direction: list) -> int:
        Steps  = 0
        OldPos = []
        while Steps==0 or Grid[Pos[1]][Pos[0]] != "S":
            OldPos  = Pos.copy()
            Pos[0] += Direction[0]
            Pos[1] += Direction[1]
            self.PipeElements.append(Pos.copy())
            Steps  += 1
            Dir1, Dir2 = PipeMaze.Map[Grid[Pos[1]][Pos[0]]]
            if OldPos == [Pos[0]+Dir1[0], Pos[1]+Dir1[1]]:
                Direction = Dir2
            else:
                Direction = Dir1
        return Steps
            
    
    def getStepsToFarthestPointinPipe(self) -> int:
        return int(self.countLenOfPipe(self.Grid, self.StartPos, self.StartDirection) / 2)
    
    ################## P A R T II ########################
    
    def changeGrid(self):
        for y in range(len(self.Grid)):
            for x in range(len(self.Grid[y])):
                if [x,y] not in self.PipeElements:
                    self.Grid[y][x] = "." 
                if self.Grid[y][x] == "S":
                    self.Grid[y][x] = self.StartTile

        for y in range(len(self.Grid)):
            for x in range(len(self.Grid[y])):
                if self.Grid[y][x] == ".":
                    if self.checkTileIfInsideLoop(self.Grid, [x,y]): 
                        self.Grid[y][x] = "I"
                    else:
                        self.Grid[y][x] = "0"
                    
    
    def checkTileIfInsideLoop(self, Grid: list, Pos: list) -> bool:
        CntPipesCrossing = 0
        Tile = ""
        for y in range(Pos[1], -1, -1):
            Tile = Grid[y][Pos[0]]
            if self.Map[Tile][0][0] == 1:
                CntPipesCrossing += 1
            if self.Map[Tile][1][0] == 1:
                CntPipesCrossing += 1
        return not CntPipesCrossing%2 == 0
        
    
    def getNumberOfTilesEnclosedByLoop(self) -> int:
        self.changeGrid()
        Cnt = 0
        for Line in self.Grid:
            for Value in Line:
                if Value == "I":
                    Cnt += 1
        return Cnt
         
        
##################### S T A R T #################
PM = PipeMaze("#10 Puzzle.txt")
#PM = PipeMaze("#10 Test6.txt")
print (f"PART I : Steps to the farthest position from start : {PM.getStepsToFarthestPointinPipe()}")
print (f"PART II: Number of tiles enclosed by the loop      : {PM.getNumberOfTilesEnclosedByLoop()}")