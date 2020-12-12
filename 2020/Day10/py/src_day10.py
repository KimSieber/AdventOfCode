#################################################
##### AdventOfCode 2020
#####
##### Day 10 - Adapter Array
#####
##### @author  Kim Sieber
##### @date    11.12.2020
###################################################
### Parameter
FILENAME = "input.txt"

### Liest Datei ein und erzeugt Liste mit Adaptern
### @return:	(dict) apt[val] = 0
def readInputFile():
	apt 	= {}
	inputFile = open(FILENAME, "r")
	apt[0] = 0									# Ausgangs-Spannung = 0 hinzufuegen
	for line in inputFile:
		apt[int(line)] = 0
	inputFile.close()
	apt[max(apt.keys())+3] = 0					# Geraete-Eingangsspannung Max + 3 hinzufuegen
	return apt

### Zaehlt die Voltage-Spruenge nach 1-, 2-, 3-er-Abstaenden
### @apt   :	(dict) apt[val] = 0 (oder anderen Value, egal)
### @return: 	cntV[0]	= keine Werte (immer=0)
### 			cntV[1]	= Anzahl Adapter mit 1 Volatage-Differenz/Sprung
### 			cntV[2]	= Anzahl Adapter mit 2 Volatage-Differenz/Sprung
### 			cntV[3]	= Anzahl Adapter mit 3 Volatage-Differenz/Sprung
def cntJolDiff(apt):
	cntV = [0,0,0,0]
	akt = 0
	while True:
		if (akt+1) in apt:
			akt += 1
			cntV[1] += 1
		elif (akt+2) in apt:
			akt += 2
			cntV[2] += 1
		elif (akt+3) in apt:
			akt += 3
			cntV[3] += 1
		else:
			#cntV[3] += 1
			break
	return cntV

### Ermittelt die Gesamt-Anzahl und setzt diese ins dict und gibt dieses wieder zurrueck
### @apt   :	(dict) apt[val] = 0
### @return:	(dict) apt[val] = (int) Total Options-Summierung
def setTot(apt):
	tot = 0
	for a in sorted(apt.keys()):
		tot = 0
		if a == 0:
			tot = 1
		if (a-1) in apt.keys():
			tot += apt[a-1]
		if (a-2) in apt.keys():
			tot += apt[a-2]
		if (a-3) in apt.keys():
			tot += apt[a-3]
		apt[a] = tot	
	return apt		


apt = readInputFile()

cntV = cntJolDiff(apt)
print()
print("PART I  : Number of 1-jolt differences multiplied by the number of 3-jolt differences: " + str(cntV[1]*cntV[3]))
print()

apt = setTot(apt)
print("PART II : Total number of distict ways you can arrange the adapters to connect       : " + str(apt[max(apt.keys())]))
print()



