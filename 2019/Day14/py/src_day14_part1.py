###################################################
##### AdventOfCode 2019
#####
##### Day 14 - Space Stoichiometry
#####
##### @author  Kim Sieber
##### @date    02.12.2020
#####
##### Problem: too slow for Part II -> see alternative try
###################################################


### Liest Datei zeilenweise ein und gibt Liste von Zeilen zurueck
### @fileName:      Dateiname der Input-Datei im gleichen Verzeichnis
### @return  :      lines[]
def readInputFile(fileName):
	inputFile = open(fileName, "r")
	lines     = []
	for line in inputFile:
		lines.append(line.rstrip())
	inputFile.close()
	return lines

#### Klasse, die eine Reaktion beschreibt in Inputs und Output
#### Klasse wird je Reaktion erzeugt
class reaction:
	#### Initialisierung
	#### @line : Zeile aus Input-Datei, die eine Reaktion beschreibt
	def __init__(self, line):
		self.output         = ""			# -> Bezeichnung
		self.quantityOutput = 0			# -> Anzahl der Outputs, die diese Reaktion hervorbringt
		self.inputs         = []			# -> Liste der noetigen Inputs, bspw 7A, 1E  => [A,A,A,A,A,A,A,E]
		self.devideLine(line)

	#### Teilt die Linie in Ihre Bestandteile und erzeugt Daten
	#### @line : Zeile aus Input-Datei, die eine Reaktion beschreibt
	def devideLine(self,line):
		part1, part2        = line.split(" => ")
		out                 = part2.split(" ")
		self.output         = out[1]
		self.quantityOutput = int(out[0])
		inpu                = part1.split(", ")
		for inp in inpu:
			In = inp.split(" ")
			for n in range(0,int(In[0])):
				self.inputs.append(In[1])

	#### Rueckgabe der Reaktion als eine Zeile
	def getReactionForPrint(self):
		return str(self.quantityOutput) + " " + self.output + " <= " + str(self.inputs)



#### Zentrale Klasse zur Verarbeitung
#### wird nur 1x erzeugt
class worker:
 	#### Initialisierung
 	#### @lines  : Liste der Zeilen aus der Input-Datei mit den Reaktionen
 	def __init__(self, lines):
 		self.fuel  = []
 		self.depot = []
 		self.ore   = 0
 		self.reac  = []
 		for line in lines:
 			self.reac.append(reaction(line))
 		self.setInputsForFuel()

 	#### Testausdruck aller Reaktionen
 	def printReactions(self):
 		for r in self.reac:
 			print r.getReactionForPrint()

 	#### Ermittlt Inputs zur Reaktion mit Ergebnis=FUEL und setzt diese in Klassenliste self.fuel[]
 	#### @num:   Anzahl Fuel, der erzeugt werden soll, Standard = 1
 	def setInputsForFuel(self):
 		for r in self.reac:
 			if r.output == "FUEL":
				self.fuel = r.inputs

 	#### Startet die Stoichiometrie
 	#### durchlaeuft alle Bestandteile von 'Fuel' und 
 	#### checked Depot, ob enthalten, wenn nicht, dann
 	#### sucht jeweils die passende Reaktion 
 	#### und fuegt Inputs der Reaktion hinzu und loescht Ausgangswert
 	#### Am Schluss Entfernung der ORE-Teile und Hinzurechnung zum ORE-Zaehler
 	def runStoichiometry(self):
 		for fu in self.fuel:
 			#print "fu: " + str(fu)
 			if self.checkDepot(fu):
 				self.fuel.remove(fu)
 			else:
 				self.fuel += self.getInputsOfReaction(fu)
 				self.fuel.remove(fu)
 			self.removeORE()
 		

 	#### ORE-Zaehler 
 	#### Ermittelt die Anzahl der ORE-Eintraege, setzt Zaehler hoch und entfernt ORE-Eintrag
 	def removeORE(self):
 		while "ORE" in self.fuel:
 			self.ore += 1
 			self.fuel.remove('ORE')

 	#### Sucht passende Reaktion fuer mitgegebenen Output
 	#### und gibt die Liste der Inputs zurueck
 	#### Die Anzahl der Outputs abzuegl. 1 wird ins Depot geschrieben
 	#### @output   : gesuchter Output
 	#### @return   : Liste der Inputs
 	def getInputsOfReaction(self, output):
 		for re in self.reac:
 			if re.output == output:
 				for i in range(0,re.quantityOutput - 1):
	 				self.depot.append(output)
 				return re.inputs

 	#### Prueft, ob input in depot vorhanden,
 	#### wenn ja, dann in depot abziehen und TRUE zurueckgeben
 	#### wenn nein, dann FALSE zurueckgeben
 	#### @Input :  Input, der im Depot gesucht werden soll
 	#### @return:  True/False
 	def checkDepot(self, Input):
 		if Input in self.depot:
 			self.depot.remove(Input)
 			return True
 		else:
 			return False


from datetime import datetime

print "Start-Time: " + str(datetime.now())
lines = readInputFile("input.txt")
work = worker(lines)
i = 0
while (len(work.fuel)>0):
#	if i % 1 == 0:
#		print str(i) + ": len(fuel) : " + str(len(work.fuel))
	i += 1
	work.runStoichiometry()
print "Anzahl ORE = " + str(work.ore)
print "End-Time  : " + str(datetime.now())

print
print "#############################################################################################################"
print "# PART I   ==> number of needed ORE for 1 FUEL:   " + str(work.ore) + "             (right answer: 220019)"
print "#"
print
