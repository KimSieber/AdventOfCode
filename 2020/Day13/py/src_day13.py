################################################
##### AdventOfCode 2020
#####
##### Day 13 - Shuttle Search
#####
##### @author  Kim Sieber
##### @date    13.12.2020
##### With friendly support from https://dev.to/qviper/advent-of-code-2020-python-solution-day-13-24k4
###################################################
### Parameter
FILENAME = "input.txt"

### Aktuelle Zeit in Minuten seit 0
time = 0

### Liste der Eingaben
inputs = []

### Liste Busse mit Wartezeit
### bus[bus-No] = (int) Time to wait
busNext = {}

### Liest Datei ein
### Erste Zeile enthaelt aktuelle Zeit in Min ab 0
### Zweite Zeile enthaelt Liste mit x und Bus-Nummern
def readInputFile():
	global inputs
	global time
	inputs = []
	time = 0
	inputFile = open(FILENAME, "r")
	time = int(inputFile.readline())
	inputs = list(inputFile.readline().split(","))
	inputFile.close()

### Extrahiert aus den inputs die Busse und setzt diese mit Rest-Wartezeit in die Variable Bus
def extractBus():
	global inputs
	global time
	global busNext
	global busLast
	bus = {}
	for key, val in enumerate(inputs):
		if val != "x":
			busNext[int(val)] = int(val) - (time%int(val))


readInputFile()
extractBus()

busIDNext = min(busNext, key=busNext.get)
print()
print("PART I  : ID of the earliest bus multiplied by the number of minutes need to wait              : ", \
	             (busIDNext * busNext[busIDNext]))
print()


### Reihenfolge der Busse in Sequence der Position in Liste
### Listet BusNo auf mit Wert seit letzter Abfahrt
### @return	:	bus[bus-No] = (int) Time since last bus
def extractBusSeq():
	busSeq = {}
	for key, val in enumerate(inputs):
		if val != "x":
			if key == 0:
				busSeq[int(val)] = 0
			else:
				busSeq[int(val)] =  -key%int(val)
	return busSeq

### Ermittelt die Startzeit von Bus 1, damit alle anschliessenden Busse abhaengig Ihrer Position
### x-Minuten versetzt abfahren
### @busSeq	:	bus[bus-No] = (int) Time since last bus
### @return	:	(int) Time, an der Bus an Position 1 abfaehrt
def getTimeBusOneDepart(busSeq):
	buses = list(reversed(sorted(busSeq)))
	busWait   = int(busSeq[buses[0]])
	busNo = int(buses[0])
	for b in buses[1:]:
		while busWait % b != busSeq[b]:
			busWait += busNo
		busNo *= b
	return busWait

busSeq = extractBusSeq()
print()
print ("PART II : The earliest timestamp such that all busIDs depart at offsets matching their position: ", \
				  getTimeBusOneDepart(busSeq))
print()

