##################################################
##### AdventOfCode 2020
#####
##### Day 07 - Handy Haversacks
#####
##### @author  Kim Sieber
##### @date    07.12.2020
###################################################
### Parameter
FILENAME = "input.txt"

## Datenstruktur der Koffer-Regeln
##
## regulations['bag-color']['bag-color'] = Number of Bags
##              +-------------------------------------------- Bag-Color, that contains other bags
##                           +------------------------------- Bag-Color in the Bag
##
regulations = {}

### Liest Datei ein und erzeugt regulations-Liste
def readInputFile():
	global regulations
	regulations = {}
	containBags = {}
	inputFile = open(FILENAME, "r")
	for line in inputFile:
		bags    = line.split("bags contain")
		srcBag  = bags[0].strip()
		if bags[1].strip() == "no other bags.":
			containBags = 0
		else:
			tgtBags = bags[1].split(",")
			for bag in tgtBags:
				words = bag.strip().split(" ")
				containBags[(words[1] + " " + words[2])] = int(words[0])
		regulations[srcBag] = containBags
		containBags = {}
	inputFile.close()

### Ermittelt eine Liste von Farben, die die mitgegebene Farbe direkt oder indirekt beinhalten kann
### @color  : Vorgegebene Farbe, nach der gesucht werden soll
### @return : bags[0..n] = Farbe
def listBags(color):
	global regulations
	cnt = []
	for bagKey in regulations.keys():
		if regulations[bagKey] != 0:
			if color in regulations[bagKey]:
				cnt.append(bagKey) 
				cnt = list(set(cnt + listBags(bagKey)))
	return cnt

### Ermittelt die Anzahl der Bags, die in einem Bag enthalten sind
### @color  : Vorgegebene Farbe, nach der gesucht werden soll
### @return : (int) Anzahl Taschen gesamt
###           HINWEIS: Aufgrund der Rekursion, wird die vorgegebene Tasche mitgezaehlt.
###                    Sollte dies nicht gewuenscht werden, muss vom Ergebnis noch -1 abgezogen werden.
def countBagsNeeded(color):
	global regulations
	cnt = 1											# Diese Bag selbst ist auch mitzuzaehlen
	if regulations[color] != 0:
		for bagKey in regulations[color].keys():
			cnt += (regulations[color][bagKey] * countBagsNeeded(bagKey))
	return cnt


readInputFile()

#for reg in regulations:
#	print (str(reg)+"    ")[:12] + " : " + str(regulations[reg])
#print listBags("shiny gold")

print
print "PART I  : number of colors, that can containt at least one shiny gold bag   : " + str(len(listBags("shiny gold")))
print
print "PART II : number of individual bags required inside the singe shiny gold bag: " + str(countBagsNeeded("shiny gold")-1)
print

