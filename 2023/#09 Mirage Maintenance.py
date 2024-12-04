#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
--- Advent of Code 2023                    ---
--- Day 09: Mirage Maintenance             ---
----------------------------------------------

Created: Sat Nov 16 20:53:37 2024
@author: Kim Sieber

Types of variables:
     Sensors[0..n][0..n]   = (int) History Sensor Value
     
"""

class MirageMaintenance:

    Sensors = []
    
    def readData(self, FileName: str):
        Lines                     = open(FileName, "r").read().splitlines()
        MirageMaintenance.Sensors = [[int(Val) for Val in Sensor.split(" ")] for Sensor in Lines]


    def completeSensorWithSequences(self, Sensor: list) -> list:
        Sensor     = [Sensor]
        NextValues = Sensor[0]
        ### Find Sequences until all Sequences are 0
        while not all([v==0 for v in NextValues]):
            Spaces = []
            for Key in range(len(NextValues)-1):
                Spaces.append(NextValues[Key+1] - NextValues[Key])
            NextValues = Spaces
            Sensor.append(NextValues)
        return Sensor

    def findNextValueForSensor(self, Sensor: list) -> int:
        Sensor = MirageMaintenance.completeSensorWithSequences(self, Sensor)
        ### Add the next value in the sequence, beginning at the last sequence with all are 0
        Sensor[-1].append(0)
        for Seq in range(len(Sensor)-2,-1,-1):
            Sensor[Seq].append(Sensor[Seq][-1]+Sensor[Seq+1][-1])
        return Sensor[0][-1]
            
    def addAllNextValues(self) -> int:
        Sum = 0
        for Sensor in MirageMaintenance.Sensors:
            Sum += MirageMaintenance.findNextValueForSensor(self, Sensor)
        return Sum
                    
    def findBeforeValueForSensor(self, Sensor: list) -> int:
        Sensor = MirageMaintenance.completeSensorWithSequences(self, Sensor)
        ### Add the next value in the sequence, beginning at the last sequence with all are 0
        Sensor[-1].insert(0,0)
        for Seq in range(len(Sensor)-2,-1,-1):
            Sensor[Seq].insert(0, Sensor[Seq][0]-Sensor[Seq+1][0])
        return Sensor[0][0]
        
    def addAllBeforeValues(self) -> int:
        Sum = 0
        for Sensor in MirageMaintenance.Sensors:
            Sum += MirageMaintenance.findBeforeValueForSensor(self, Sensor)
        return Sum




######################## S T A R T ###########################
MM = MirageMaintenance()

#MM.readData("#09 Test.txt")
MM.readData("#09 Puzzle.txt")

print (f"PART I : The sum of the extrapolated values is: {MM.addAllNextValues()}")
print (f"PART II: The sum of the extrapolated values is: {MM.addAllBeforeValues()}")