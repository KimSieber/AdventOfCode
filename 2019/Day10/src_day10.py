###################################################
##### AdventOfCode
#####
##### Day 10 - Monitoring Station
#####
##### @author  Kim Sieber
##### @date    20.11.2020
###################################################

class mStation:
	### Initialisierung
	### @fileName  : Dateiname der Karte im gleichen Verzeichnis
	def __init__(self, fileName, debug=False):
		self.Map = self.readMap(fileName)
		self.statX = self.statY = 0
		self.listAsteroids = self.getListAsteroids()
		self.debug = debug
		self.countDestroyed = 0

	### Druckt die Map zur Ansicht
	### @Map : Karte im Format Map[y,x]
	def printMap(self, Map):
		print "===== Total Map ====="
		for y in range(0,len(Map)):
			line = ""
			for x in range(0, len(Map[y])):
				line += str(Map[y][x])
			print line
		print

	### Karte einlesen
	### @fileName  : Dateiname der Karte im gleichen Verzeichnis
	### @return    : Karte im Format array: map[y][x]    -> .=leer  ->#=Asteroid
	def readMap(self, fileName):
		inputFile = open(fileName, "r")
		Map = []
		for line in inputFile:
			Map.append(list(line.rstrip()))
		inputFile.close()
		return Map

	### Setzen der Monitoring-Station
	### @x  : X-Koordinate von zu setzendem Asteroiden fuer Station
	### @y  : Y-Koordinate von zu setzendem Asteroiden fuer Station
	def setStation(self, x, y):
		self.statX = x
		self.statY = y

	### Asteroiden auflisten
	### zuvor Stations-Koordination mit Funktion setStation() setzen
	### @return: Liste der Asteroiden mit Koordinaten (listAsteroiden[0..n][y, x]) 
	def getListAsteroids(self):
		ret = []
		for y in range(0,len(self.Map)):
			for x in range(0, len(self.Map[y])):
				if self.Map[y][x] == '#':
					ret.append([y,x])
		return ret

	### Asteroiden auflisten, die von einer Position sichtbar sind
	### zuvor Stations-Koordination mit Funktion setStation() setzen
	### @return : Liste von Steroiden
	def getListAsteroidsVisible(self):
		listAsteroids = self.getListAsteroids()
		if listAsteroids <= 1:
			print "getListAsteroidsVisible:listAsteroids <= 0"
			return False
		astVisible = []
		for ast in listAsteroids:
			if self.checkAsteroid(ast[1], ast[0]):
				astVisible.append(ast)
		return astVisible

	### Sortiert sichtbare Asteroiden in Kreisbahn um Station herum, beginnend bei 12-Uhr
	### @return: listSortedAsteroids[[0..n][Y-Koord][X-Koord][Sortier-Wert]]
	### Bildung Sortierwert:
	def getListSortedAsteroids(self):
		listAsteroidsVisible = self.getListAsteroidsVisible()
		if len(listAsteroidsVisible) == 0: 
			return False
		listAsteroids = []
		i = 0
		sortValue = 0
		for ast in listAsteroidsVisible:
			### Ermittlung relative Position von Station
			diffX = ast[1] - self.statX + 0.0
			diffY = ast[0] - self.statY	+ 0.0	
			### Abhaengig Quadrant SortValue bilden
			if diffX == 0 and diffY < 0:
				sortValue = 8000000
			elif diffX > 0 and diffY < 0:
				sortValue = 7000000 + (diffX / diffY) * 1000
			if diffX > 0 and diffY == 0:
				sortValue = 6000000
			elif diffX > 0 and diffY > 0:
				sortValue = 5000000 + (diffX / diffY) * 1000
			if diffX == 0 and diffY > 0:
				sortValue = 4000000
			elif diffX < 0 and diffY > 0:
				sortValue = 3000000 + (diffX / diffY) * 1000
			if diffX < 0 and diffY == 0:
				sortValue = 2000000
			elif diffX < 0 and diffY < 0:
				sortValue = 1000000 + (diffX / diffY) * 1000

			listAsteroids.append([ast[0], ast[1], sortValue])
			i += 1
		listSortedAsteroids = sorted(listAsteroids, key=lambda x:x[2], reverse=True)
		return listSortedAsteroids

	### groesster gemeinsamer Teiler
	### Berechnet den ggT nach euklidschem Algorithmus	
	def ggT(self, a, b):
		while b:      
			a, b = b, a % b
		return a

	### Pruefen, ob Asteriod sichtbar von Station
	### @x      : X-Koordinate von zu pruefendem Asteroid
	### @y      : Y-Koordinate von zu pruefendem Asteroid
	### @return : True, wenn sichbar, False, wenn verdeckt
	def checkAsteroid(self, x, y):
		if self.debug:
			print
			print "### checkAsteroid:START:x/y="+str(x)+"/"+str(y)+ "  statX/statY="+str(self.statX)+"/"+str(self.statY)

		# Abbruch, wenn Station = Asteroid
		if x == self.statX and y == self.statY:
			if self.debug: print "===> checkAsteroid=False -> Exit weil Station=Asteroid"

			return False
		# Differenz zwischen Station und Asteroid ermitteln
		diffX = x - self.statX
		diffY = y - self.statY

		# Minimalster Quotient ermitteln
		ggT = abs(self.ggT(diffX, diffY))
		minX = diffX / ggT
		minY = diffY / ggT
		# Suche ab Station bis zum Asteroiden, ob ein Asteroid dazwischen ist
		posX = self.statX
		posY = self.statY
		if self.debug: print "checkAsteroid:ggT=" + str(ggT) + "  diffX/diffY="+str(diffX)+"/"+str(diffY)+"  minX/minY=" +str(minX)+"/"+str(minY)
		if self.debug: print "START: posX, posY : " + str(posX) + ", " + str(posY)
		while posX != x or posY != y:
			posX += minX
			posY += minY
			if self.debug: print "LOOP: posX, posY : " + str(posX) + ", " + str(posY)
			if posX == x and posY == y:
				if self.debug: print "===> checkAsteroid=True"
				return True
			if self.Map[posY][posX] == "#":
				if self.debug: print "===> checkAsteroid=False:diffX/diffY="+str(diffX)+"/"+str(diffY)+"  minX/minY=" +str(minX)+"/"+str(minY)
				return False

		print "ERROR: checkAsteroid: kein Asteroid gefunden, noch nicht mal gesuchter !!!"
		exit()

	### zerstoert Asteroiden auf Karte, und setzt Zaehler der Zerstoeung hoch
	### @x     : X-Koordinate des zu zerstoerenden Asteroiden
	### @x     : X-Koordinate des zu zerstoerenden Asteroiden
	### @return: True, wenn Zerstoerung erfolgreich, False, wenn kein Asteroid vorhanden war
	def destroyAsteroid(self, x, y):
		if self.Map[y][x] != "#":
			return false
		self.Map[y][x] = "."
		self.countDestroyed += 1
		if self.debug: 
			print "destroyAsteroids x/y: " + str(x) + "/" + str(y) + "  countDestroyed:" + str(self.countDestroyed)

	### Ermittlung Asteroiden im Kreis
	# 1. listAsteroidsVisible ermitteln
	# 2. dann Asteroid mit x-Koord = x-Station und y-Koord < y-Station
	# 3. 

### Gibt Index des zu suchenden Wertes aus
def getIdxOfListitem(list, item):
	i = 0
	for value in list:
		if value == item:
			return i
		i += 1

#####################################################
### PART I
#####################################################
debug = False

STAT = mStation("input.txt", debug)

listResult = [0] * len(STAT.listAsteroids)
i = 0
for Station in STAT.listAsteroids:
	STAT.setStation(Station[1], Station[0])
	listResult[i] = len(STAT.getListAsteroidsVisible())
	i += 1

if debug:
	STAT.printMap(STAT.Map)
	print str(STAT.listAsteroids)
	print str(listResult)
	print

print "#########################################################################################"
print "PART I  ==> most asteroids viewing   :  " + str(max(listResult)) + "      (right answer: 299)"
print "            on Asteroid-Position x/y :  " + str(STAT.listAsteroids[getIdxOfListitem(listResult, max(listResult))][1]) + "," + \
                                                   str(STAT.listAsteroids[getIdxOfListitem(listResult, max(listResult))][0]) + \
                                                   "    (right answer: 26,29)"
print 

#####################################################
### PART II
#####################################################
debug = False

STAT = mStation("input.txt", debug)

STAT.setStation(STAT.listAsteroids[getIdxOfListitem(listResult, max(listResult))][1], \
	            STAT.listAsteroids[getIdxOfListitem(listResult, max(listResult))][0]    )

loop = True
while loop:
	listSortedAsteroids = STAT.getListSortedAsteroids()
	if listSortedAsteroids == False:
		break
	for ast in listSortedAsteroids:
		STAT.destroyAsteroid(ast[1], ast[0])
		if STAT.countDestroyed == 200:
			loop = False
			break


print "#########################################################################################"
print "PART II ==> The 200th asteroid to be vaporized :  " + str((ast[1]*100) + ast[0]) + "     (right answer: 1419)"
print "            on Asteroid-Position x/y           :  " + str(ast[1]) + "," + str(ast[0]) +  "    (right answer: 14,19)"
print 
