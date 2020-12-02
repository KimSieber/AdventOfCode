###################################################
##### AdventOfCode 2020
#####
##### Day 02 - Password Philosophy
#####
##### @author  Kim Sieber
##### @date    02.12.2020
###################################################

### Liest Datei zeilenweise ein und gibt Liste von Zeilen zurueck
### @fileName:		Dateiname der Input-Datei im gleichen Verzeichnis
### @return  :      lines[]
def readInputFile(fileName):
	inputFile = open(fileName, "r")
	lines = []
	for line in inputFile:
		lines.append(line.rstrip())
	inputFile.close()
	return lines


### Klasse fuer Passwort-Handling
class password:
	### Initialisierung
	### Erzeugt Variablen und stoesst Verarbeitung an
	def __init__ (self, line):
		self.range_from = 0
		self.range_to   = 0
		self.letter     = ""
		self.password   = []
		self.valid1     = False
		self.valid2     = False
		self.devideLine(line)
		self.checkValid1()
		self.checkValid2()

	### Teilt Zeile und befuellt Variablen mit Teilen
	### Bsp-Zeile:    18-19 x: qxxwxsxxxzprvwxxdvxx
	def devideLine(self, line):
		lineSplit       = line.split(" ")
		rangeSplit       = lineSplit[0].split("-")
		self.range_from   = int(rangeSplit[0])
		self.range_to     = int(rangeSplit[1])
		self.letter      = lineSplit[1].split(":")[0]
		self.password    = list(lineSplit[2])

	### prueft, ob Passwort gueltig nach Policy 1
	def checkValid1(self):
		cnt = self.password.count(self.letter)
		if cnt >= self.range_from and \
		   cnt <= self.range_to         :
		    self.valid1 = True

	### prueft, ob Passwort gueltig nach Policy 2
	def checkValid2(self):
		ltr1 = self.password[self.range_from-1]
		ltr2 = self.password[self.range_to-1]
		if (ltr1 == self.letter and ltr2 != self.letter) or \
		   (ltr1 != self.letter and ltr2 == self.letter)      :
		    self.valid2 = True

	### druckt alle Variablen zur Pruefung aus
	def printVar(self):
		print "#####################################################################"
		print "Range           = " + str(self.range_from) + "-" + str(self.range_to)
		print "Letter:Password = " + self.letter + " : " + str(self.password)
		print "Valid 1 / 2     = " + str(self.valid1) + " / " + str(self.valid2)


#####################################################
### PART I + II
#####################################################
lines = readInputFile("input.txt")
pwds = []
for pwd in lines:        
	pwds.append(password(pwd))

cntValid1 = cntValid2 = 0
for pwd in pwds:
	#pwd.printVar()
	if pwd.valid1:       
		cntValid1 += 1
	if pwd.valid2:       
		cntValid2 += 1

print
print "#############################################################################################################"
print "# PART I   ==> Count valid passwords with password-policy 1:   " + str(cntValid1) + "             (right answer: 456)"
print "#"
print

print
print "#############################################################################################################"
print "# PART II  ==> Count valid passwords with password-policy 2:   " + str(cntValid2) + "             (right answer: 308)"
print "#"
print



