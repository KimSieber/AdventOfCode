#################################################
##### AdventOfCode 2020
#####
##### Day 16 - Ticket Translation
#####
##### @author  Kim Sieber
##### @date    16.12.2020
###################################################
from collections import defaultdict
### Parameter
FILENAME = "input.txt"

### Regelwerk
### rule[0..n]['name'  ]	= (str) Name der Regel, bspw "departure location"
###           ['start1']	= (int) Beginn der Range 1
###           ['end1'  ]	= (int) Ende der Range 1
###           ['start2']	= (int) Beginn der Range 2
###           ['end2'  ]	= (int) Ende der Range 2
###			  ['field' ]	= (int) Feld-ID, wenn identifiziert
rules = []

### Mein Ticket
### mytik[0..n]		= (int) Zahl aus Ticket
###       +---------- Zaehler fuer Anzahl Zahlen auf meinem Ticket
mytik = []

### Andere Tickets (nearby tickets)
### nrtik = [0..n][0..n]	= (int) Zahl aus Ticket
###          +--------------- (int) Zaehler fuer Anzahl Tickets
###                +--------- (int) Zaehler fuer Anzahl Zahlen auf Ticket
### HINWEIS: validTiks[] sind die Tickets aus nrtiks[], die gueltig sind
nrtiks = []
validTiks = []

### Listet die Regeln mit den Feld-IDs auf, fuer die die Regel passt
### validRuleToField[ruleID][fieldID] = True (initial)
###									  = False (wird gesetzt, wenn Feld in Regel gespeichert wurde)
validRuleToField = defaultdict(dict)


### Liest Puzzle Datei ein und befuellt globale Variablen
def readInputFile():
	global rules
	rules = []
	rule = {}
	global mytik
	mytik = []
	global nrtiks
	nrtiks = []
	part = 1							# Abschnitte 1=rules, 2=my ticket, 3=nearby tickets
	inputFile = open(FILENAME, "r")
	for line in inputFile:
		if line.strip() == "":
			part += 1
		else:
			if part == 1:
				rule = {}
				lineparts = line.strip().split(": ")
				rule['name'] = lineparts[0].strip()
				ranges = lineparts[1].split(" or ")
				nums = ranges[0].split("-")
				rule['start1'] = int(nums[0].strip())
				rule['end1']   = int(nums[1].strip())
				nums = ranges[1].split("-")
				rule['start2'] = int(nums[0].strip())
				rule['end2']   = int(nums[1].strip())
				rules.append(rule)
			elif part == 2:
				if line.strip() != "your ticket:":
					mytik = list(map(int, line.split(",")))
			elif part == 3:
				if line.strip() == "nearby tickets:":
					nrtiks = []
				else:
					nrtiks.append(list(map(int, line.split(","))))
	inputFile.close()


### prueft Ticket auf Gueltigkeit
### @tik[0..n]	= Liste Zahlen auf einem Ticket
### @return		= [0..n] (int) Liste von Zahlen, die keiner Regel entsprechen
###             = [], wenn Ticket gueltig ist
def checkValid(tik):
	ret = []
	for t in tik:
		valid = False
		for r in rules:
			if (t >= r['start1'] and t <= r['end1'])  or  \
			   (t >= r['start2'] and t <= r['end2'])      :
			   valid = True

		if valid == False:
			ret.append(t)
	return ret

### Erzeugt Liste der gueltigen Tickets
def generateListValidTickets():
	global nrtiks
	global validTiks
	for n in nrtiks:
		if len(checkValid(n)) == 0:
			validTiks.append(n)

### Prueft alle Tickets ab, ob die definierte Regel zum definierten Feld passt
### @ruleID 	:	(int)	ID der zu pruefenden Regel
### @fieldID	:	(int)	ID des zu pruefenden Ticket-Feldes
### @return		:	(bool)	True, wenn Regel zutreffend, False, wenn bei mind. 1 Ticket 
###							die Regel nicht passt
def checkRuleToField(ruleID, fieldID):
	global rules
	global validTiks
	global mytik
	### Eigenes Ticket pruefen
	if (mytik[fieldID] >= rules[ruleID]['start1'] and mytik[fieldID] <= rules[ruleID]['end1'])  or  \
	   (mytik[fieldID] >= rules[ruleID]['start2'] and mytik[fieldID] <= rules[ruleID]['end2'])        :
	   	True	## -> Regel passt
	else:
		return False
	### Alle anderen Tickets pruefen
	for t in validTiks:
		if (t[fieldID] >= rules[ruleID]['start1'] and t[fieldID] <= rules[ruleID]['end1'])  or  \
		   (t[fieldID] >= rules[ruleID]['start2'] and t[fieldID] <= rules[ruleID]['end2'])        :
		   	True	## -> Regel passt
		else:
			return False
	return True

### Ermittelt die gueltigen Regeln zu passenden Feldern
def generateValidRuleToField():
	global validRuleToField
	for rid, rul in enumerate(rules):
		for fid, tik in enumerate(mytik):
			if checkRuleToField(rid, fid):
				validRuleToField[rid][fid] = True

### Ermittelt eindeutige Kombinationen (Regel->Feld) aus validRuleToField,
### speichert diese zur Regel und loescht Regel und Feld aus validRuleToField
### @return:	(bool) True, wenn erfolgreich, False, wenn es keine gueltigen
###					   Schluessel mehr gibt (=Ende)
def setFieldToRule():
	global validRuleToField
	vRTF = defaultdict(dict)
	for rKey in validRuleToField.keys():
		for fKey in validRuleToField[rKey].keys():
			if validRuleToField[rKey][fKey] == True:
				vRTF[rKey][fKey] = True
	if len(vRTF) == 0:
		return False
	### Ermitteln aller eindeutiger Zuordnungen (Regel->Feld)
	for rKey in vRTF.keys():
		if len(vRTF[rKey]) == 1:
			fKey = (list(vRTF[rKey].keys()))[0]
			rules[rKey]['field'] = fKey
			validRuleToField[rKey][fKey] = False

			for rKey2 in vRTF.keys():
				if fKey in vRTF[rKey2].keys():
					validRuleToField[rKey2][fKey] = False
	return True


readInputFile()


notValidNums = []
for n in nrtiks:
	notValidNums += checkValid(n)
errorrate = 0
for N in notValidNums:
	errorrate += N
print()
print("PART I  : The ticket scanning error rate is                   : ", errorrate)
print()


generateListValidTickets()
generateValidRuleToField()
while setFieldToRule():
	True
product = 1
for r in rules:
	if r['name'][:9] == "departure":
		product *= mytik[r['field']]
print()
print("PART II : The product of the fields for the departure-rules is: ", product)
print()


