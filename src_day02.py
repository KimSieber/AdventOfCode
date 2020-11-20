################################
##### AdventOfCode
#####
##### Day 2 - erster IntCode-Computer
#####
##### @author  Kim Sieber
##### @date    15.11.2020
##################################

### Testausgaben
def printHeadLine(iC, text):
	i = 0
	txt = text
	while i < len(iC):
		txt = txt + ("     " + str(i))[len(str(i)):] + "#"
		i = i + 1
	print txt

def printIntCode(iC, text):
	txt = text
	for val in iC:
		txt = txt + ("     " + str(val))[len(str(val)):] + ","
	print txt

### IntCode-Programm aus Datei einlesen
def readIntCodeFile(fileName):
	import csv 
	inputFile = open(fileName, "r")
	csv_reader = csv.reader(inputFile, delimiter=",")
	intCode = []
	for row in csv_reader:
		for val in row:
			intCode.append(int(val))
	inputFile.close()
	return intCode

#### IntCodeComputer starten und durchlaufen
def intCodeComputer(intCode):
	pos = 0
	opcode = int(intCode[pos])
	while opcode <> 99:
		if opcode == 1:
			intCode[intCode[pos+3]] = intCode[intCode[pos+1]] + intCode[intCode[pos+2]]
			pos = pos + 4
		elif opcode == 2:
			intCode[intCode[pos+3]] = intCode[intCode[pos+1]] * intCode[intCode[pos+2]]
			pos = pos + 4
		else:
			print "ERROR in IntCodeComputer - opcode == " + str(opcode)
			print "ERROR in IntCodeComputer - pos    == " + str(pos)
			print "ERROR - cancel while-loop"
			break
		opcode = int(intCode[pos])
	return intCode


intCode = readIntCodeFile("input_03.txt")

###########################################
### PART I: Manipulation der ersten Werte
intCode[1] = 12
intCode[2] = 2
print "#############################################"
print "PART I  ==> puzzle answer = " + str(intCodeComputer(intCode[:])[0])
print

####################################################
### PART II: Werte fuer bestimmtes Ergebnis suchen
i = 0
stop = False
while i < 100:
	j = 0
	while j < 100:
		intCode[1] = i
		intCode[2] = j
		if intCodeComputer(intCode[:])[0] == 19690720:
			stop = True
			break
		j += 1
	if stop:
		break
	i += 1
print "#############################################"
print "PART II ==> puzzle answer = " + str((i * 100) + j)
print
