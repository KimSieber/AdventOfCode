##################################################
##### AdventOfCode 2020
#####
##### Day 09 - Encoding Error
#####
##### @author  Kim Sieber
##### @date    09.12.2020
###################################################
### Parameter
FILENAME = "input.txt"
NUMCHECK = 25

### Datenstruktur des Programms
### xmas[0..n]   = (int)  List of transmitting numbers vom XMAS (eXchange-Masking Addition System)
xmas = []

### Liest Datei ein und erzeugt Liste Nummern in globaler Variablen xmas
def readInputFile():
	global xmas
	xmas = []
	inputFile = open(FILENAME, "r")
	for line in inputFile:
		xmas.append(int(line))
	inputFile.close()


### Pruefung, ob Zahl aus Summe zweier in Range bildbar ist,
### @posX	:	(int) Position der zu pruefenden Zahl
### @cntPos	:	(int) Anzahl der vorherigen Stellen, die zur Pruefung herangezogen werden sollen
### @return	:	(bool) Ob Summe gebildet werden konnte (TRUE) oder nicht (FALSE)
def checkSumPossible(posX, cntPos):
	### Start-Position
	pos = cntPos
	rng = [posX-cntPos, posX-1]
	for r1 in range(rng[0], rng[1]+1):
		val1 = xmas[r1]
		for r2 in range(rng[0], rng[1]+1):
			val2 = xmas[r2]
			if val1 != val2   and   val1+val2 == xmas[posX]:
				return True
	return False

### Sucht die Range (von-bis) von Zahlen, die ab Position x-abwaerts zusammen die Summe an Position x ergibt
### @posX	:	(int) Position der zu pruefenden Zahl
### @return : 	[0..n](int)	Liste an Zahlen, die in Summe den Wert auf Position x ergeben
def getNumsThatSum(posX):
	posStart = posX
	ret = []
	while True:
		posStart -= 1
		sumVal = 0
		ret = []
		for x in range(posStart-1, 0, -1):
			ret.append(xmas[x])
			sumVal += xmas[x]
			if sumVal == xmas[posX]:
				return ret


readInputFile()

posX = cntPos = NUMCHECK
while checkSumPossible(posX, cntPos):
	posX +=1
print()
print("PART I  : The first number that does not hove the proberty of the sum of two numbers of the last " + str(cntPos) + " numbers is: " + str(xmas[posX]))
print()

ret = getNumsThatSum(posX)
print("PART II : The encryption weakness in the XMAS-encrypted list of numbers is                                    : " + str(min(ret) + max(ret)))
print()

