#################################################
##### AdventOfCode 2020
#####
##### Day 12 - Rain Risk
#####
##### @author  Kim Sieber
##### @date    13.12.2020
###################################################
### Parameter
FILENAME = "input.txt"

### Globale Variable fuer Navigations-Anweisungen
###  nav[0..n]['act']	= (str) Aktions-Anweisung (N,S,E,W,L,R,F)
###           ['val']	= (int) Wert für die Aktionsanweisung
###      +--------------- Zaehler Aktionen
nav = []

### Globale Variable fuer Schiffs-Position und Richtung
### ship['x']			= X-Position (West-Ost), Start = 0
###	    ['y']			= Y-Position (Nord-Sued), Start = 0
### ship['face']		= Richtung des Schiffs in Grad, beginnend bei Ost = 90
###     ['xWP']			= relative X-Position (West-Ost) des WayPoints, Start = 10 West
###	    ['yWP']			= relative Y-Position (Nord-Sued)des WayPoints, Start =  1 Nord
ship = {'x': 0, 'y': 0, 'face': 90, 'xWP': 10, 'yWP': -1}

### Liest Datei ein und erzeugt Navigations-Anweisungs-Liste
def readInputFile():
	global nav
	nav = []
	navLine = {}
	inputFile = open(FILENAME, "r")
	for line in inputFile:
		navLine = {}
		nav.append({'act': line[:1], 'val': int(line[1:])})
	inputFile.close()

### Reise starten und durchfuehren
### @return	:	(int) Manhattan distance an Zielposition
def startJourney():
	for inst in nav:
		if   inst['act'] == "N"			or (inst['act'] == "F"  and  ship['face'] == 0):
			ship['y'] -= inst['val']
		elif inst['act'] == "S"			or (inst['act'] == "F"  and  ship['face'] == 180):
			ship['y'] += inst['val']
		elif inst['act'] == "E"			or (inst['act'] == "F"  and  ship['face'] == 90):
			ship['x'] += inst['val']
		elif inst['act'] == "W"			or (inst['act'] == "F"  and  ship['face'] == 270):
			ship['x'] -= inst['val']
		elif inst['act'] == "L":
			ship['face'] -= inst['val']
		elif inst['act'] == "R":
			ship['face'] += inst['val']
		if ship['face'] < 0		:  ship['face'] += 360
		if ship['face'] >=360	:  ship['face'] -= 360
	return (abs(ship['x'])+abs(ship['y']))


readInputFile()

print()
print("PART I  : The Manhattan distance between location and ship's starting position: ", startJourney())
print()

### Reise starten und durchfuehren fuer PART II (waypoint-Regeln)
### @return	:	(int) Manhattan distance an Zielposition
def startJourney2():
	for inst in nav:
		if   inst['act'] == "N":
			ship['yWP'] -= inst['val']
		elif inst['act'] == "S":
			ship['yWP'] += inst['val']
		elif inst['act'] == "E":
			ship['xWP'] += inst['val']
		elif inst['act'] == "W":
			ship['xWP'] -= inst['val']
		elif inst['act'] == "L":
			ship['face'] -= inst['val']
			for i in range(0,int(inst['val']/90)):
				xWP = ship['xWP']
				ship['xWP'] = ship['yWP'] 
				ship['yWP'] = xWP * -1
		elif inst['act'] == "R":
			for i in range(0,int(inst['val']/90)):
				xWP = ship['xWP']
				ship['xWP'] = ship['yWP'] * -1
				ship['yWP'] = xWP
		elif inst['act'] == "F":
			ship['x'] = ship['x'] + ship['xWP'] * inst['val']
			ship['y'] = ship['y'] + ship['yWP'] * inst['val']
	return (abs(ship['x'])+abs(ship['y']))


### Reset der Schiffs-Ausgangswerte
ship = {'x': 0, 'y': 0, 'face': 90, 'xWP': 10, 'yWP': -1}
print()
print("PART II : The Manhattan distance between location and ship's starting position: ", startJourney2())
print()


