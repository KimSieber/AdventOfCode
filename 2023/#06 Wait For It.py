#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
--- Advent of Code 2023                    ---
--- Day 6: Wait for it                     ---
----------------------------------------------

Created: Tue Nov  5 21:44:53 2024
@author: Kim Sieber

Datentypen:
    races[0..n][0..1]  -> [0] = Dauer des Race
                          [1] = Ziel-Länge der Strecke  
    oneRaces[0..1]     -> [0] = Dauer des Race
                          [1] = Ziel-Länge der Strecke  
"""
import re

#############################
### Races auslesen
###    Ermittelt die Races mit Dauer und Ziel-Länge aus dem Puzzle und gibt diese zurück
def getRaces(FileName: str) -> list:
    InputLines = open(FileName, "r").read().splitlines() 
    times     = [int(num) for num in re.findall(r"\d+", InputLines[0])]
    distances = [int(num) for num in re.findall(r"\d+", InputLines[1])]
    races = [[times[i], distances[i]] for i in range(len(times))]    
    #PART II:
    oneRace = [int("".join([str(i) for i in times])), int("".join([str(i) for i in distances]))] # [int("".join(times)), int("".join(distances))]
    return races, oneRace


#############################
### Ermittelt Anzahl Wege in einem Rennen
###    Durchläuft jede Mögliche Kombination und ermittelt, welche die Mindestdistanz erreicht
def getNumWaysinRace(_time: int, _distance: int) -> int:
    counter = 0
    for i in range (1,_time):
        if (i * (_time-i)) > _distance:
  #          print (f"i:{i}, _time:{_time}, _distance:{_distance}, i*(_time-i):{i * (_time-i)}")
            counter += 1
    return counter
     

############## S T A R T ##########################
#races, oneRace = getRaces("#06 Test.txt")
races, oneRace = getRaces("#06 Puzzle.txt")

ProductOfWays = 1
for race in races:
    ProductOfWays *= getNumWaysinRace(race[0], race[1])

    
print (f"### PART I : Product of ways of all races is    {ProductOfWays}")

print (f"### PART II: Product of ways of one big race is {getNumWaysinRace(oneRace[0], oneRace[1])}")