##################################################
##### AdventOfCode 2020
#####
##### Day 11 - Seating System
#####
##### @author  Kim Sieber
##### @date    12.12.2020
###################################################
### Parameter
FILENAME = "input.txt"

### Globale Variable fuer den Sitzungsplan
### plan[0..n][0..n]	= Belegung ('.', 'L', '#')
###      +--------------- Y-Achse (zeilenweise)
###            +--------- X-Achse (spaltenweise)
plan = []

### Liest Datei ein und erzeugt Sitzplan
def readInputFile():
	global plan
	plan = []
	inputFile = open(FILENAME, "r")
	for line in inputFile:
		plan.append(list(line.strip()))
	inputFile.close()

### Gibt die Anzahl der belegten Sitze in Sichtrichtung an (alle 8 Richtungen)
### @x 		: (int) Sitzreihe des zu pruefenden Sitzes
### @y 		: (int) Sitzspalte des zu pruefenden Sitzes
### @flag	: (bool) Kennzeichen, ob nur Sitze direkt daneben geprueft werden sollen (=False)
###                               oder naechster Sitz in Sichtweite (=True)
### @return	: (int) Anzahl der belegten Sitzplaetze in Sicht (oben/unten, rechts/links, diagonal)
def getOccSeats(x, y, flag=False):
	global plan
	cnt = 0
	lenY = len(plan)-1
	lenX = len(plan[0])-1
	### Alle Richtungen definieren
	direct = [[0,-1],[+1,-1],[+1,0],[+1,+1],[0,+1],[-1,+1],[-1,0],[-1,-1]]
	directDelete = []
	exp = 1
	while len(direct) > 0:
		for d in direct:
			chkX = (d[0] * exp) + x
			chkY = (d[1] * exp) + y
			if chkX < 0 or chkX > lenX or chkY < 0 or chkY > lenY:
				directDelete.append(d)
			else:
				if plan[chkY][chkX] == "#":
					cnt += 1
					directDelete.append(d)
				if plan[chkY][chkX] == "L":
					directDelete.append(d)
		if flag==False:								# Wenn nicht in Sichtweite (flag=False, dann nur eine Pruef-Runde)
			break
		for delete in directDelete:
			direct.remove(delete)
		directDelete = []
		exp += 1
	return cnt

### Fuehrt eine Runde an Regel-Umsetzung für alle Sitze durch
### @occNum	: (int)  Anzahl der Sitze, die belegt sein muessen, damit Platz wieder frei wird
### @flag	: (bool) Kennzeichen, ob nur Sitze direkt daneben geprueft werden sollen (=False)
###                               oder naechster Sitz in Sichtweite (=True)
### @return	:	(int) Anzahl Aenderungen
def runRules(occNum, flag=False):
	global plan
	chgLog = []
	### Erst alle Aenderungsbedarfe ermitteln
	for y in range(0,len(plan)):
		for x in range(0,len(plan[y])):
			occ = getOccSeats(x, y, flag)
			if plan[y][x] == "#" and occ >= occNum:
				chgLog.append({'x': x, 'y': y, 'val': "L"})
			elif plan[y][x] == "L" and occ == 0:
				chgLog.append({'x': x, 'y': y, 'val': "#"})
	### Dann Aenderungen ausfuehren
	for c in chgLog:
		plan[c['y']][c['x']] = c['val']
	return len(chgLog)

### Zaehlt belegte Sitze
### @return	:	(int) Anzahl belegte Sitzplaetze
def getNumOccSeats():
	global plan
	occ = 0
	for y in range(0,len(plan)):
		for x in range(0,len(plan[y])):
			if plan[y][x] == "#":
				occ += 1
	return occ


readInputFile()
while runRules(4, False) > 0:
	True
print()
print("PART I  : Number of seats occupied: ", getNumOccSeats())
print()


readInputFile()
while runRules(5, True) > 0:
	True
print()
print("PART II : Number of seats occupied: ", getNumOccSeats())
print()
