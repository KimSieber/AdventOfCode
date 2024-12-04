#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
--- Advent of Code 2023                    ---
--- Day 5: If You Give A Seed A Fertilizer ---
----------------------------------------------

Created: Sat Nov  2 19:03:32 2024
@author: Kim Sieber

Datentypen:
    seeds(0..n)        = Tuple der Seed-Nr.
    maps(0..n)         = Tuple der Maps          
      +-> map          = Tuple der Map-Einträge
        +-> map-Eintrag = Tuple der drei Werte je Eintrag (Ziel, Quelle, Länge)
      ==>  ( tuple( tuple(int,int,int), ...), ... )
"""

###########################
### Daten auslesen
###    Liest Inputdatei aus und gibt die Inhalte formatiert in 2 Variablen zurück
def readData(InputFile: str) -> (tuple, tuple(tuple(tuple(int,int,int)))):
    InputLines = open(InputFile, "r").read().splitlines()    
    InputLines.append("")            # Damit Ende gefunden wird und nicht abbricht
    seeds      = tuple([int(s) for s in InputLines[0][7:].split(" ")])
    maps       = []
    maps.append(getMap(InputLines, "seed-to-soil map:"))
    maps.append(getMap(InputLines, "soil-to-fertilizer map:"))
    maps.append(getMap(InputLines, "fertilizer-to-water map:"))
    maps.append(getMap(InputLines, "water-to-light map:"))
    maps.append(getMap(InputLines, "light-to-temperature map:"))
    maps.append(getMap(InputLines, "temperature-to-humidity map:"))
    maps.append(getMap(InputLines, "humidity-to-location map:"))     
    return seeds, tuple(maps)


##################
### Funktion zum Auslesen einer Map
###    Sucht nach Map in Datei und gibt eine Liste der Map-Daten aus. Eine Map-Data ist ein Tuple
def getMap(InputLines: str, mapName: str) -> tuple(tuple[int,int,int]):
    mapData = []
    start = InputLines.index(mapName) + 1
    end   = InputLines.index("",start)
    for i in range(start, end):
        mapData.append(tuple([int(n) for n in InputLines[i].split(" ")]))
    return tuple(mapData)
    

###################
### Seed-Liste konvertieren und kleinste Locations zurückgeben
###    Nimmt Seed-Nr entgegen und gibt Location-Nr. zurück
def getLocationFromSeed(SeedNo: int, maps: tuple) -> int:
    Num = SeedNo
    for map in maps:
        for Rule in map:
            if Num >= Rule[1] and Num <= (Rule[1]+Rule[2]):
                Num = Rule[0] + Num - Rule[1]
                break
    return Num
                

############################ START ##########################
### Daten aus Datei auslesen
#seeds, maps = readData("#05 Test.txt")
seeds, maps = readData("#05 Puzzle.txt")


############################ PART I #########################
minLocation = 99999999999999999
for seed in seeds:
    Loc         = getLocationFromSeed(seed, maps)
    minLocation = Loc if Loc < minLocation else minLocation

print (f"PART I : The lowest location number is    : {minLocation}     (test=35)")


############################ PART II #########################
### Liste Seed-Intervalle erzeugen mit Start- und End-Zahl
seed_intervals = [(seeds[i], seeds[i]+seeds[i+1]) for i in range(0,len(seeds),2)]

minLocationII = 999999999999999
for seed_interval in seed_intervals:
    for seed in range(seed_interval[0], seed_interval[1]):
        Loc           = getLocationFromSeed(seed, maps)
        minLocationII = Loc if Loc < minLocationII else minLocationII
    print (f"seed_interval fertig: {seed_interval} -> minLocationII: {minLocationII}")

print (f"PART II: The new lowest location number is: {minLocationII}     (test=46)")



""" Liste der Sets aus dem Puzzle
 104847962   3583832 
1212568077 114894281 
3890048781 333451605 
1520059863 217361990 
 310308287  12785610 
3492562455 292968049 
1901414562 516150861 
2474299950 152867148 
3394639029  59690410 
 862612782 176128197

"""