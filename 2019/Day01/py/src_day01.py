################################
##### AdventOfCode
#####
##### Day 1 - Treibstoffmenge ermitteln
#####
##### @author  Kim Sieber
##### @date    15.11.2020
##################################
inputFile = open("input.txt", "r")

##### PART I
##### Bestimme fuer vorgegebene Strecken benoetigten Treibstoff und summiere ihn

### Variablen Festlegen
# Variable fuer Summe Treibstoffe
sumFuel = 0

### Benoetigte Treibstoffmenge ermitteln auf Basis bekannter Masse
def calculateFuel(mass):
	## Treibstoffmenge = Mass durch 3, abrunden und ziehe 2 ab
	return int(mass) / 3 - 2

i = 0
for line in inputFile:
#	valueLine = int(line)
	sumFuel = sumFuel + calculateFuel(line)
	i = i + 1

inputFile.close()

### Ergebnis ausgeben
print "##################################################"
print "PART I"
print "======"
print "Anzahl eingelesene Zeilen    = " + str(i)
print "Summe benoetigter Treibstoff = " + str(sumFuel)
print "##################################################"
print

##### PART II
##### Bestimme fuer vorgegebene Strecke benoetigten Treibstoff,
##### auf dieser Basis den Treibstoff fuer den Treibstoff, solange bis Resttreibstoff =< 0
##### und summiere ihn
inputFile = open("input.txt", "r")

sumFuel = 0

j = 0
for line in inputFile:
	thisFuel = calculateFuel(line)
	restFuel = calculateFuel(thisFuel)
	while restFuel > 0:
		thisFuel = thisFuel + restFuel
		restFuel = calculateFuel(restFuel)
	sumFuel = sumFuel + thisFuel
	j = j + 1

inputFile.close()

### Ergebnis ausgeben
print "##################################################"
print "PART II"
print "======="
print "Anzahl eingelesene Zeilen    = " + str(j)
print "Summe benoetigter Treibstoff = " + str(sumFuel)
print "##################################################"
print

###################################################################################
### Alternativer Versuche mit Less Code und rekursivem Funktionsaufruf
###################################################################################
### PART I
sumFuel = 0
inputFile = open("input.txt", "r")
for line in inputFile:
	sumFuel = sumFuel + int(line) / 3 - 2
inputFile.close()
print "===> PART I : Summe benoetigter Treibstoff = " + str(sumFuel)

### PART II
def calcAllFuel(mass):
	erg = int(mass) / 3 - 2
	if erg > 0:
		return erg + calcAllFuel(erg)
	else:
		return 0
sumFuel = 0
inputFile = open("input.txt", "r")
for line in inputFile:
	sumFuel = sumFuel + calcAllFuel(int(line))
inputFile.close()
print "===> PART II: Summe benoetigter Treibstoff = " + str(sumFuel)
