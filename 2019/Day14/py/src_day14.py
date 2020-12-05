###################################################
##### AdventOfCode 2019
#####
##### Day 14 - Space Stoichiometry
#####
##### @author  Kim Sieber
##### @date    05.12.2020 - alternative try
##### (after inspiration of https://0xdf.gitlab.io/adventofcode2019/14)
###################################################
from collections import defaultdict
### Parameter
FILENAME = "input.txt"

### Set Reaktionen
### Aufbau der Liste:	reactions[NameOutput]['out']            = Anzahl Outputs
###                                          ['in' ][NameInput] = Anzahl Inputs
reactions = {}

### Liest Datei zeilenweise ein und befuellt das SET an Reaktionen
def readReactionsFromInputFile():
	global reactions
	reactions = {}
	inputFile = open(FILENAME, "r")
	for line in inputFile:
		part_in, part_out = line.strip().split(" => ")
		out_num, out_chem = part_out.split(" ")
		inputs = {}
		for in_var in part_in.split(", "):
			in_num, in_chem = in_var.split(" ")
			inputs[in_chem] = int(in_num)
		reactions[out_chem] = {"out": int(out_num), "in": inputs}
	inputFile.close()

### Funktion startet mit Anzahl FUEL und gibt Anzahl benoetigte ORE zurueck
### @fuel     : Anzahl FUEL benoetigt
### @return   : Anzahl benoetigte ORE fuer benoetigte FUEL
def oreRequired(fuel=1):
	### => Aufbau der Listen:	chemHave/chemNeed[NameChem] = Anzahl Chem's
	### chemische Bestandteile, die benoetigt werden, oder die im Besitz nach den Reaktionen sind
	chemNeed = defaultdict(int, {"FUEL": fuel})
	chemHave = defaultdict(int)
	numORE   = 0

	### Schleife, bis keine Chems mehr da (ORE in separatem Zaehler, wird nicht als Chem gewertet)
	while chemNeed:
		### Erste Chem aus der Liste nehmen
		item = list(chemNeed.keys())[0]
		### Pruefen, ob benoetigte Chem vorraetig ist
		if chemNeed[item] <= chemHave[item]:
			chemHave[item] -= chemNeed[item]
			del chemNeed[item]
			continue								# => naechste chemNeed, Schleife von vorne

		### Anzahl benoetigte chem berechnen, indem evt. vorhandene chem im chemHave abgezogen wird
		### anschliessend chem aus Need und Have entfernen
		### und Anzahl chem aus Reaktion ermitteln
		numNeed = chemNeed[item] - chemHave[item]
		del chemNeed[item]
		del chemHave[item]
		numProduced = reactions[item]["out"]

		### Berechnen, wie haeufig Reaktion benoetigt wird
		### Achtung: bei Need=Produced sowie wenn Produced = 1 ist, gibt es eine Abweichung. Daher in allen diesen Faellen +1
		numReactions = numNeed // numProduced
		if (numReactions * numProduced) < numNeed:
			numReactions += 1

		### Alle nicht fuer Need benoetigten Chem in chemHave uebernehmen
		chemHave[item] += (numReactions * numProduced) - numNeed
		### ... sowie alle inputs der Reaktion in chemNeed eintragen (ORE separat zaehlen)
		for chem in list(reactions[item]["in"].keys()):
			if chem == "ORE":
				numORE += reactions[item]["in"][chem] * numReactions
			else:
				chemNeed[chem] += reactions[item]["in"][chem] * numReactions

	return numORE

### PART II - Vorgehen: so lange Versuchen, bis maxFuel ermittelt mit 1000000000000 ORE
###                     dabei Range immer halbieren und in Haelfte suchen
###                     Start-Range eingrenzen: MIN: Zahl durch Anzahl ORE fuer 1 FUEL
###                                             MAX: Doppelte von MIN
### @return: Anzahl FUEL fuer gesetzte ORE-Anzahl
def numberOfFuelForTrillionORE():
	OREHOLD = 1000000000000
	Min = OREHOLD // oreRequired(1)
	Max = Min * 2

	while Min < Max - 1:
		Mid = (Min + Max) // 2
		oreNeed = oreRequired(Mid)
		if oreNeed < OREHOLD:
			Min = Mid
		elif oreNeed > OREHOLD:
			Max = Mid
	
	if oreRequired(Mid) > OREHOLD:
		Mid -= 1
	return Mid 


readReactionsFromInputFile()

print "PART I  : Minimum amout of ORE required to produce exactly 1 FUEL = " + str(oreRequired(1))
print
print "PART II : Maximum amout of FUEL to produce from 1 Trillion ORE    = " + str(numberOfFuelForTrillionORE())
print 

