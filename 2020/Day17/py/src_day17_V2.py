#################################################
##### AdventOfCode 2020
#####
##### Day 17 - Conway Cubes
#####
##### @author  Kim Sieber
##### @date    17.12.2020
##### HINWEIS: Nicht optimierter Code -> lange Laufzeit
#####          Probleme mit dynamischem dict, daher auf statische mehrdimensionale Liste gewechselt
#####          Funktionen von PART I und II muessten zusammengelegt und Laufzeit-optimiert werden
###################################################
### Parameter
FILENAME = "input.txt"
GRIDDIMENSION = [20,40,40,20]
STARTPOS = [10,15,15,10]

### Spielfeld
### grid[ z ][ y ][ x ][ w ]	= (str) '#' = aktiv, '.' = inaktiv
###       +---------------------- (int) Wert der Z-Achse
###            +----------------- (int) Wert der Y-Achse
###                 +------------ (int) Wert der X-Achse
###                      +------- (int) Wert der W-Achse  (bei grid2)
#grid = [[[0] * GRIDDIMENSION[2]] * GRIDDIMENSION[1]] * GRIDDIMENSION[0]
#grid = [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]]
#grid = [[['.']*3 for _ in range(3)] for _ in range(3)]
grid = []
grid2 = []

### erzeugt Spielfeld mit Initial-Zeichen
def buildGrid():
	global grid
	global grid2
	grid = [[['.']*GRIDDIMENSION[2] for _ in range(GRIDDIMENSION[1])] for _ in range(GRIDDIMENSION[0])]
	grid2 = [[[['.']*GRIDDIMENSION[3] for _ in range(GRIDDIMENSION[2])] for _ in range(GRIDDIMENSION[1])] \
																		for _ in range(GRIDDIMENSION[0])]


### Liest Datei ein und erzeugt Navigations-Anweisungs-Liste
def readInputFile():
	global grid
	buildGrid()
	inputFile = open(FILENAME, "r")
	z = STARTPOS[0]
	y = STARTPOS[1]
	w = STARTPOS[3]
	for line in inputFile:
		x = STARTPOS[2]
		listLine = list(line.strip())
		for val in listLine:
			grid[z][y][x] = val
#			print("grid2[",z,"][",y,"][",x,"][",w,"]=",val)
			grid2[z][y][x][w] = val
			x += 1
		y +=1
	inputFile.close()

### Druckt das Grid zur Visualisierung der Ebenen aus
### @type	:	(int) 0 = Druck des Arrays unveraendert, nur zeilenweise
###					  1 = Druck aufbereitet
def printGrid(typ = 0, zStart = 0, zEnd = GRIDDIMENSION[0], \
					   yStart = 0, yEnd = GRIDDIMENSION[1], \
					   xStart = 0, xEnd = GRIDDIMENSION[2],   ):
	global grid
	if typ == 1:
		for z in range(zStart, zEnd):
			print("########## Ebene z= ",z," ###############")
			for y in range(yStart, yEnd):
				line = ""
				for x in range(xStart, xEnd):
					line += grid[z][y][x]
				print(line)
	elif typ == 0:
		for z in grid:
			print("New Level")
			for y in z:
				print(y)

### Ermittelt die Anzahl aktiver Cubes in der Nachbarschaft
### -> Abfrage Position, Rueckgabe Anzahl Cubes=aktiv
### @z 		: (int) Wert der Z-Achse
### @y 		: (int) Wert der Y-Achse
### @x 		: (int) Wert der X-Achse
###@return	: (int) Anzahl der aktiven Cubes in der Nachbarschaft
def cntAktCub(z, y, x):
	global grid
	cnt = 0
	for zI in range(-1, +2):
		for yI in range(-1, +2):
			for xI in range(-1, +2):
				if not (zI==0 and yI==0 and xI==0):			# -> sich selbst nicht mitzaehlen
					if grid[z-zI][y-yI][x-xI] == "#":
						cnt += 1
	return cnt

def cntAktCub2(z, y, x, w):
	global grid2
	cnt = 0
	for zI in range(-1, +2):
		for yI in range(-1, +2):
			for xI in range(-1, +2):
				for wI in range(-1, +2):
					if not (zI==0 and yI==0 and xI==0 and wI==0):			# -> sich selbst nicht mitzaehlen
						if grid2[z-zI][y-yI][x-xI][w-wI] == "#":
							cnt += 1
	return cnt

### Fuehrt einen Zyklus aus
### prueft alle Cube-Positionen, beginnend und endent eines vor/nach die Spielfeld-Ende/Beginn
### merkt sich die Veraenderungen und fuehrt diese am Ende gesamthaft aus
def prozessCycle():
	global grid
	changes = []
	for z in range(1,GRIDDIMENSION[0]-1):
		for y in range(1,GRIDDIMENSION[1]-1):
			for x in range(1,GRIDDIMENSION[2]-1):
				numActCub = cntAktCub(z,y,x)
				if grid[z][y][x] == "#":
#					print("prozessCycle(): z,y,x:",z,",",y,",",x," - numActCub=",numActCub)
					if not (numActCub == 2 or numActCub == 3):
						changes.append([z,y,x,"."])
				if grid[z][y][x] == "." and numActCub == 3:
					changes.append([z,y,x,"#"])
	for c in changes:
		grid[c[0]][c[1]][c[2]] = c[3]

def prozessCycle2():
	global grid2
	changes = []
	for z in range(1,GRIDDIMENSION[0]-1):
		for y in range(1,GRIDDIMENSION[1]-1):
			for x in range(1,GRIDDIMENSION[2]-1):
				for w in range(1,GRIDDIMENSION[3]-1):
					numActCub = cntAktCub2(z,y,x,w)
					if grid2[z][y][x][w] == "#":
	#					print("prozessCycle(): z,y,x:",z,",",y,",",x," - numActCub=",numActCub)
						if not (numActCub == 2 or numActCub == 3):
							changes.append([z,y,x,w,"."])
					if grid2[z][y][x][w] == "." and numActCub == 3:
						changes.append([z,y,x,w,"#"])
	for c in changes:
		grid2[c[0]][c[1]][c[2]][c[3]] = c[4]

### Zaehlt die aktiven Cubes auf dem Grid
def cntActOnGrib():
	cnt = 0
	for z in range(0,GRIDDIMENSION[0]):
		for y in range(0,GRIDDIMENSION[1]):
			for x in range(0,GRIDDIMENSION[2]):
				if grid[z][y][x] == "#":
					cnt += 1
	return cnt

def cntActOnGrib2():
	cnt = 0
	for z in range(0,GRIDDIMENSION[0]):
		for y in range(0,GRIDDIMENSION[1]):
			for x in range(0,GRIDDIMENSION[2]):
				for w in range(0,GRIDDIMENSION[3]):
					if grid2[z][y][x][w] == "#":
						cnt += 1
	return cnt

readInputFile()

#print()
#print("======================> Initial-Grid <====================")
#printGrid(1,5,6,8,12,8,11)

for i in range(1,7):
	print("cycle ", i)
	prozessCycle()

#print()
#print("======================> Grid after ",i," cycles <====================")
#printGrid(1)

print()
print("PART I  : Number of active cubes in a 3-dimensional space after ", i, " cycles: ", cntActOnGrib())
print()

for i in range(1,7):
	print("cycle ", i)
	prozessCycle2()

print()
print("PART II : Number of active cubes in a 4-dimensional space after ", i, " cycles: ", cntActOnGrib2())
print()
