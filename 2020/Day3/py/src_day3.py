###################################################
##### AdventOfCode 2020
#####
##### Day 03 - Toboggan Trajectory
#####
##### @author  Kim Sieber
##### @date    03.12.2020
###################################################

class Toboggan:
	### Initialisierung
	### @inputFile:   Dateiname der Input-Datei mit Karten-Daten
	def __init__ (self, inputFile):
		self.map = self.readMap(inputFile)

	### Karte einlesen
	### @fileName  : Dateiname der Karte im gleichen Verzeichnis
	### @return    : Karte im Format array: map[y][x]    -> .=leer  ->#=Asteroid
	def readMap(self, fileName):
		inputFile = open(fileName, "r")
		Map = []
		for line in inputFile:
			Map.append(list(line.strip()))
		inputFile.close()
		return Map

	### Reise beginnen mit x/y-Differenz
	### @x     : Wert, wie viele Spalten er nach rechts gehen soll
	### @y     : Wert, wie viele Zeilen er nach unten gehen soll
	### @return: Anzahl kollidierte Baeume
	def travel(self, moveX, moveY):
		posX = posY = 0
		treeCollision = 0
		while True:
			posX += moveX
			if posX >= len(self.map[0]):
				posX = posX - len(self.map[0])

			posY += moveY
			if posY >= len(self.map):
				return treeCollision
			
			if self.map[posY][posX] == "#":
				treeCollision += 1


tob = Toboggan("input.txt")

#####################################################
### PART I
#####################################################
print
print "#############################################################################################################"
print "# PART I     ==> count of tree-collision during journey:   " + str(tob.travel(3,1)) + "              (right answer: 211)"
print "#"
print

#####################################################
### PART II
#####################################################
sloopProduct = tob.travel(1,1) * tob.travel(3,1) * tob.travel(5,1) * tob.travel(7,1) * tob.travel(1,2)
print
print "#############################################################################################################"
print "# PART II    ==> product of the 5 sloops-returns       :   " + str(sloopProduct) + "       (right answer: 3584591857)"
print "#"
print
