#################################################
##### AdventOfCode 2020
#####
##### Day 15 - Rambunctious Recitation
#####
##### @author  Kim Sieber
##### @date    15.12.2020
###################################################
### Liste Nummern, initialisiert mit Start-Nummern
### nums[0..n]	= (int) Nummern gesprochen
nums = [6,4,12,1,20,0,16]					# => Input-Puzzle
#nums = [0,3,6]								# => Test 1
#nums = [1,3,2]								# => Test 2
#nums = [2,1,3]								# => Test 3
#nums = [1,2,3]								# => Test 4
#nums = [2,3,1]								# => Test 5
#nums = [3,2,1]								# => Test 6
#nums = [3,1,2]								# => Test 7

import time

### Spielt das Memory-Game 
### HINWEIS: In der ersten Version des Programms wurde die Liste nums[] je Runde ergaenzt
###          und anschliessend in dieser gesucht (letztes Mal gesprochen, Anzahl nums, usw.)
###          Dies hat eine enorme Laufzeit fuer PART II ergeben, so dass ein anderer Ansatz 
###          gesucht wurde. Statt mir der Liste num[] zu arbeiten, wurde zur Performance-Optimierung 
###          die Speicherung der letzten Position in einer eigenen dict gewaehlt
### 		 lastSpoken[Num] = ID
###          		    +----------- Nummer, die gesprochen wurde
###                   		   +---- Letzter ID/Turn, an dem die Nummer gesprochen wurde
### @turns	:	(int) Anzahl der Runden
### @return	:	(int) Letzte gesprochene Zahl
def startGame(turns):
	print("START-TIME: ",time.ctime())
	### Neu hinzugefuegte/gesprochene Zahl aus letzter Runde -> initialisiert mit letzter Vorgabe-Zahl
	newNum = nums[-1]
	### Initialisiere lastSpoken mit Vorgabe-Zahlen
	lastSpoken = {}
	for k, v in enumerate(nums):  		
		lastSpoken[v] = k
	### Schleife fuer alle Turns 
	for turn in range(len(nums),turns):
		lastNum = newNum 
		if lastNum not in lastSpoken:
			newNum = 0
		else:
			newNum = (turn-1)-lastSpoken[lastNum]
		lastSpoken[lastNum] = turn-1

		if turn%10000000==0: print("      ->  : ", time.ctime(), " - TURN: ", turn, " - lastNum:", lastNum, " - newNum:", newNum)
	print("END-TIME  : ", time.ctime())
	print()
	return newNum

print()
print("PART I  : the 2020th spoken number is    : ", startGame(2020))
print()

print("PART II : the 30000000th spoken number is: ", startGame(30000000))
print()
