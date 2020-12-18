#################################################
##### AdventOfCode 2020
#####
##### Day 17 - Conway Cubes
#####
##### @author  Kim Sieber
##### @date    17.12.2020
###################################################
from collections import defaultdict
### Parameter
FILENAME = "input_test1.txt"

### Erzeugt dreidimenionales Grid als Dictionary
def multidim_dict(n, type):
    if n == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: multidim_dict(n-1, type))

### Spielfeld
### grid[ z ][ y ][ x ]	= (str) '#' = aktiv, '.' = inaktiv
###       +-------------- (int) Wert der Z-Achse, von negativ bis positiv
###            +--------- (int) Wert der Y-Achse, von negativ bis positiv
###                 +---- (int) Wert der X-Achse, von negativ bis positiv
grid = multidim_dict(3, list)

### Spielfeldgroesse
### gridDim['z']['min']		= (int) kleinster Wert der Achse
###             ['max']		= (int) groesster Wert der Achse
###        ['y']['min']		= (int) kleinster Wert der Achse
###             ['max']		= (int) groesster Wert der Achse
###        ['z']['min']		= (int) kleinster Wert der Achse
###             ['max']		= (int) groesster Wert der Achse
gridDim = {'z': {'min': 0, 'max': 0}, 'y': {'min': 0, 'max': 0}, 'x': {'min': 0, 'max': 0}}

### Liest Datei ein und erzeugt Navigations-Anweisungs-Liste
def readInputFile():
	global grid
	grid = None
	grid = multidim_dict(3, list)
	x = y = z = 0
	inputFile = open(FILENAME, "r")
	for line in inputFile:
		listLine = list(line.strip())
		for x, v in enumerate(listLine):
			grid[z][y][x] = v
		y += 1
	gridDim['y']['min'] = 0
	gridDim['y']['max'] = y-1
	gridDim['x']['min'] = 0
	gridDim['x']['max'] = len(line)-1
	inputFile.close()

### Druckt das Grid zur Visualisierung der Ebenen aus
def printGrid():
	global grid
	for Z in range(gridDim['z']['min'], gridDim['z']['max']+1):
		print()
		print("##### for z = ", Z, " ##############")
		for Y in range(gridDim['y']['min'], gridDim['y']['max']+1):
			line = ""
			for X in range(gridDim['x']['min'], gridDim['x']['max']+1):
				val = grid[Z][Y][X]
				if val not in (".", "#"):
					grid[Z][Y][X] = "."
				line += grid[Z][Y][X]
			print(line)
	return True
	for z, zV in sorted(grid.items()):
		print()
		print("for z = ", z, " ##############")
		for y, yV in sorted(grid[z].items()): 
			line = ""
			for x, xV in sorted(grid[z][y].items()):
				print ("z:",z,"y:",y,",x:", x, " -xV:", xV)
				line += xV #grid[z][y].get(x, ".")
			print (line)

### Ermittelt die Anzahl aktiver Cubes in der Nachbarschaft
### -> Abfrage Position, Rueckgabe Anzahl Cubes=aktiv
### @z 		: (int) Wert der Z-Achse
### @y 		: (int) Wert der Y-Achse
### @x 		: (int) Wert der X-Achse
###@return	: (int) Anzahl der aktiven Cubes in der Nachbarschaft
def cntAktCub(z, y, x):
	global grid
	cnt = 0
	for Z in range(z-1, z+2):
		if Z in grid.keys():
			for Y in range(y-1, y+2):
				if Z in grid[Z].keys():
					for X in range(x-1, x+2):
						if grid[Z][Y].get(X, ".") == "#":
							cnt += 1
	print("cntAktCub(",z,",",y,",",x,")=",cnt)
	return cnt

### Setzt Cube auf aktiv oder inaktiv
### -> Angabe Position und Wert
### @z 		: (int) Wert der Z-Achse
### @y 		: (int) Wert der Y-Achse
### @x 		: (int) Wert der X-Achse
###@val 	: (str) (str) '#' = aktiv, '.' = inaktiv
def setCube(z,y,x,val):
	#print("->setCube: ",x,",",y,",",z,":",val)
	global grid
	global gridDim
	grid[z][y][x] = val
	if z < gridDim['z']['min']: 	gridDim['z']['min'] = z
	if z > gridDim['z']['max']: 	gridDim['z']['max'] = z
	if y < gridDim['y']['min']: 	gridDim['y']['min'] = y
	if y > gridDim['y']['max']: 	gridDim['y']['max'] = y
	if x < gridDim['x']['min']: 	gridDim['x']['min'] = x
	if x > gridDim['x']['max']: 	gridDim['x']['max'] = x

### Fuehrt einen Zyklus aus
### prueft alle Cube-Positionen, beginnend und endent eines vor/nach die Spielfeld-Ende/Beginn
### merkt sich die Veraenderungen und fuehrt diese am Ende gesamthaft aus
def prozessCycle():
	global grid
	global gridDim
	changes = []
	for Z in range(gridDim['z']['min']-1, gridDim['z']['max']+2):
		for Y in range(gridDim['y']['min']-1, gridDim['y']['max']+2):
			for X in range(gridDim['x']['min']-1, gridDim['x']['max']+2):
				numActCub = cntAktCub(Z,Y,X)
				if Z in grid.keys():
					if Y in grid[Z].keys():
						if grid[Z][Y].get(X, ".") == "#" and numActCub not in (2,3):
							changes.append({'z':Z, 'y':Y, 'x':X, 'val':"."})
						if grid[Z][Y].get(X, ".") != "#" and numActCub == 3:	
							changes.append({'z':Z, 'y':Y, 'x':X, 'val':"#"})
					elif numActCub == 3:
						changes.append({'z':Z, 'y':Y, 'x':X, 'val':"#"})
				elif numActCub == 3:
					changes.append({'z':Z, 'y':Y, 'x':X, 'val':"#"})

	print("->prozessCycle()->changes:", str(changes))
	for c in changes:
		setCube(c['z'], c['y'], c['x'], c['val'])

readInputFile()
print()

#print("gridDim:  ==========================")
#print(gridDim)
#print()

print("=============> grid initial <================")
printGrid()
print()
#print(gridDim)
#print()
print("=============> PROZESS 1 <================")
#print(grid)
prozessCycle()
print("==============> grid after <==================")
#print(grid)
printGrid()
print()