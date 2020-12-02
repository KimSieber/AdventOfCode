###################################################
##### AdventOfCode 2020
#####
##### Day 01 - Report Repair
#####
##### @author  Kim Sieber
##### @date    01.12.2020
###################################################

### Liest Datei und gibt Liste mit Eintraegen zurueck
### @fileName:		Dateiname der Input-Datei im gleichen Verzeichnis
### @return  :      entries[] - Liste von Integer-Werten
def readInputFile(fileName):
	inputFile = open(fileName, "r")
	entries = []
	for line in inputFile:
		entries.append(int(line.rstrip()))
	inputFile.close()
	return entries


entries = readInputFile("input.txt")

#####################################################
### PART I
#####################################################
result = []
for i in entries:
	for j in entries:
		if (i + j) == 2020:
			if not [i, j] in result  and \
			   not [j, i] in result :
				result.append([i, j])

print
print "#########################################################################################"
print "# PART I  ==> Product of two entries:    " + str(result[0][0] * result[0][1]) + "              (right answer: 960075)"
print "#             entries:                   " + str(result)
print


#####################################################
### PART II
#####################################################
def checkEntry(entries, val1, val2, val3):
	for e in entries:
		if val1 in e and val2 in e and val3 in e:
			return True
	return False

result = []
for i in entries:
	for j in entries:
		for k in entries:
			if (i + j + k) == 2020:
				if not checkEntry(result, i, j, k):
					result.append([i, j, k])

print
print "#########################################################################################"
print "# PART II ==> Product of three entries:  " + str(result[0][0] * result[0][1] * result[0][2]) + "           (right answer: 212900130)"
print "#             entries:                   " + str(result)
print

