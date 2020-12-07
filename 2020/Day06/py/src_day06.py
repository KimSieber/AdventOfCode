##################################################
##### AdventOfCode 2020
#####
##### Day 06 - Custom Customs
#####
##### @author  Kim Sieber
##### @date    06.12.2020
###################################################
### Parameter
FILENAME = "input.txt"

### Daten-Array
### Format:   groups[0..n]['person'  ][0..n][0..n] = 'a'..'z'
###                  +-------------------------------------- Zaehler Gruppe
###                                    +-------------------- Zaehler Person in Gruppe
###                                          +-------------- Zaehler der Fragen, auf die die Person mit 'Ja' geantwortet hat
###                                                   +----- Frage a-z, auf die die Person mit 'Ja' geantwortet hat
###           groups[0..n]['combined'][0..n] = 'a'..'z'
###                                    +-------------------- Zaehler der Fragen, auf die mind. 1 Person mit 'Ja' geantwortet hat
###                                             +----------- Frage a-z, auf die mind. eine Personen mit 'Ja' gewantwoertet haben
###           groups[0..n]['absolut' ][0..n] = 'a'..'z'
###                                    +-------------------- Zaehler der Fragen, auf die alle mit 'Ja' geantwortet haben
###                                             +----------- Frage a-z, auf die alle Personen mit 'Ja' gewantwoertet haben
groups = {}

### Zaehler-Variablen
### 1. Zaehler: Summe aller Fragen, die in einer Gruppe mit mind. 1x Ja beantwortet wurden
### 2. Zaehler: Summe aller Fragen, die von jedem in einer Gruppe mit Ja beantwortet wurden
sum1 = 0
sum2 = 0

### Liest Datei gruppen- und personenweise ein und gibt Liste zurueck
def readInputFile():
	global groups
	global sum1
	global sum2
	sum1 = sum2 = 0
	inputFile = open(FILENAME, "r")
	i = 0
	person  = []
	answers = []
	absolut = []
	for line in inputFile:
		if not line.strip():				# Next Group
			absolut = aboslutAnswers(person)
			groups[i] = {'person': person, 'combined': answers, 'absolut': absolut}
			sum1 += len(answers)
			sum2 += len(absolut)
			person  = []
			answers = []
			absolut = []
			i += 1
		else:								# New line = new person in same group
			person.append(list(line.strip()))
			answers = list(set(answers + list(line.strip())))
	absolut = aboslutAnswers(person)
	groups[i] = {'person': person, 'combined': answers, 'absolut': absolut}
	sum1 += len(answers)
	sum2 += len(absolut)
	inputFile.close()


def aboslutAnswers(persons):
	flag = True
	returnList = []
	for i in range(97,123):			# a-z
		flag = True
		for p in persons:
			if chr(i) not in p:
				flag = False
				break
		if flag:
			returnList.append(chr(i))
	return returnList


readInputFile()

print
print "PART I  : sum of counts answers over all groups, where min. one person in the group answers with 'yes':  " + str(sum1)
print
print "PART II : sum of counts answers over all groups, where everybody in the group answers with 'yes'      :  " + str(sum2)


