#################################################
##### AdventOfCode 2020
#####
##### Day 17 - Conway Cubes
#####
##### @author  Kim Sieber
##### @date    18.12.2020	-> 2. Versuch, andere Herangehensweise
##### Mit freundlicher Unterstuetzung von: https://dev.to/qviper/advent-of-code-2020-python-solution-day-17-g6k
###################################################
### Parameter
FILENAME = "input.txt"

### Wuerfel-Auflistung
### cubes = {(x,y,z,w):value} 
###           +------------------- (int) Wert der X-Achse
###             +----------------- (int) Wert der Y-Achse
###               +--------------- (int) Wert der Z-Achse
###                    +---------- (str) '#' = aktiv, '.' = inaktiv
###                  +------------ (int) Wert der W-Achse, nur fuer cubes2
cubes  = {}
cubes2 = {}

### Liest Datei ein und erzeugt Navigations-Anweisungs-Liste
def readInputFile():
	global cubes
	global cubes2
	inputs = []
	inputFile = open(FILENAME, "r")
	for line in inputFile:
		inputs.append(list(line.strip()))
	inputFile.close()
	cubes = {(x,y,0):inputs[y][x]
		     for x in range(len(inputs[0]))
	    	 for y in range(len(inputs   )) }
	cubes2 = {(x,y,0,0):inputs[y][x]
		       for x in range(len(inputs[0]))
	    	   for y in range(len(inputs   )) }


### Gibt eine Liste von Nachbarfeldern zurück
### @cube[0..2/3]	: (int) zu pruefende Koordinaten x,y,z
def getNeighborsList(cube):
	if len(cube) == 3:
		return [(cube[0]+x, cube[1]+y, cube[2]+z)
				for x in range(-1, 2)
				for y in range(-1, 2)
				for z in range(-1, 2)
				if not (x==0 and y==0 and z==0)]
	elif len(cube) == 4:
		return [(cube[0]+x, cube[1]+y, cube[2]+z, cube[3]+w)
				for x in range(-1, 2)
				for y in range(-1, 2)
				for z in range(-1, 2)
				for w in range(-1, 2)
				if not (x==0 and y==0 and z==0 and w==0)]


### Zaehlt die aktiven Nachbar-Wuerfel
### @cube[0..2]	: (int) zu pruefende Koordinaten x,y,z
### @return		: (int) Anzahl der aktiven Wuerfel in der Nachbarschaft
def countActiveNeighbors(cube, cubes):
	ngh = getNeighborsList(cube)
	return len([x for x in ngh if cubes.get(x)=="#"])

### Zyklus einmal ausfuehren
### @cubes = {(x,y,z,w):value} 		-> kann 3- oder 4-dimensional sein
def runCycle(cubes):
	newCubes = {}
	### Alle vorhandenen Eintraege durchlaufen, pruefen und ggf. aendern
	for cube in cubes:
		cntN = countActiveNeighbors(cube, cubes)
		if cubes[cube] == "#":
			if cntN == 2 or cntN == 3:
				newCubes[cube] = "#"
			else:
				newCubes[cube] = "."
		elif cubes[cube] == ".":
			if cntN == 3:
				newCubes[cube] = "#"
			else:
				newCubes[cube] = "."
		### Alle Nachbarfelder pruefen und ggf. aendern
		ngh = getNeighborsList(cube)
		for n in ngh:
			if n not in cubes:		#-> sofern nicht schon vorhanden, dann oben schon geprueft
				cntN = countActiveNeighbors(n, cubes)
				if cntN == 3:
					newCubes[n] = "#"		#-> da Cube noch nicht existierte, kann er auch nicht "#" sein,
											#	daher einziger Aenderungsgrund
	return newCubes

### Zaehlt Anzahl aktive Wuerfel
### @dim 	:	(int) 3- oder 4-dimensional angeben
### @return	:	(int) Anzahl aktive (="#") Wuerfel auf dem Spielfeld
def cntActiveCubes(dim):
	if dim == 3:
		return list(cubes.values()).count("#")
	elif dim == 4:
		return list(cubes2.values()).count("#")

readInputFile()

for i in range(6):
	cubes = runCycle(cubes)
print()
print("PART I  : Number of active cubes in a 3-dimensional space after ", i+1, " cycles: ", cntActiveCubes(3))
print()

for i in range(6):
	cubes2 = runCycle(cubes2)
print()
print("PART II : Number of active cubes in a 4-dimensional space after ", i+1, " cycles: ", cntActiveCubes(4))
print()
