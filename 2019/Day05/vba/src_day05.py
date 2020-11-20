################################
##### AdventOfCode
#####
##### Day 5 - Expand the IntCode-Computer 
#####
##### @author  Kim Sieber
##### @date    16.11.2020
##################################

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

#### Instructionen auslesen
#### @return instruction[opcode, mode1, mode2, mode3
def readInstruction(instruction):
	instruction = ("0000" + instruction)[len("0000" + instruction)-5:]
	#print "instruction: " + instruction
	#print "opcode:      " + str(instruction[3:])
	#print "modes1/2/3:  " + str(instruction[2:3]) + " " + str(instruction[1:2]) + " " + str(instruction[0:1])
	return [int(instruction[3:]), int(instruction[2:3]),  int(instruction[1:2]), int(instruction[0:1])]


#### IntCodeComputer starten und durchlaufen
def intCodeComputer(intCode, inputs=[0], output=['AA']):
	pos = 0
	posInput = 0
	
	inst = readInstruction(str(intCode[pos]))
	opcode = inst[0]
	if len(intCode)-1 > pos+1:
		posParam1 = [intCode[pos+1], (pos+1)][inst[1]]
	if len(intCode)-1 > pos+2:
		posParam2 = [intCode[pos+2], (pos+2)][inst[2]]
	if len(intCode)-1 > pos+3:
		posParam3 = [intCode[pos+3], (pos+3)][inst[3]]

	while opcode <> 99:
		if opcode == 1:
			intCode[posParam3] = intCode[posParam1] + intCode[posParam2]
			pos += 4
		elif opcode == 2:
			intCode[posParam3] = intCode[posParam1] * intCode[posParam2]
			pos += 4
		elif opcode == 3:
			intCode[posParam1] = inputs[posInput]
			#print "input: " + str(inputs[posInput])
			if (len(inputs)-1) > posInput:
				posInput += 1
			pos += 2
		elif opcode == 4:
			#print "output: " + str(intCode[posParam1])
			output.append(str(intCode[posParam1]))
			pos += 2
		elif opcode == 5:
			if intCode[posParam1] != 0:
				pos = intCode[posParam2]
			else:
				pos += 3
		elif opcode == 6:
			if intCode[posParam1] == 0:
				pos = intCode[posParam2]
			else:
				pos += 3
		elif opcode == 7:
			if intCode[posParam1] < intCode[posParam2]:
				intCode[posParam3] = 1
			else:
				intCode[posParam3] = 0
			pos += 4
		elif opcode == 8:
			if intCode[posParam1] == intCode[posParam2]:
				intCode[posParam3] = 1
			else:
				intCode[posParam3] = 0
			pos += 4
		else:
			print "ERROR in IntCodeComputer - opcode == " + str(opcode)
			print "ERROR in IntCodeComputer - pos    == " + str(pos)
			print "ERROR - cancel while-loop"
			break

		inst = readInstruction(str(intCode[pos]))
		opcode = inst[0]
		if len(intCode)-1 > pos+1:
			posParam1 = [intCode[pos+1], (pos+1)][inst[1]]
		if len(intCode)-1 > pos+2:
			posParam2 = [intCode[pos+2], (pos+2)][inst[2]]
		if len(intCode)-1 > pos+3:
			posParam3 = [intCode[pos+3], (pos+3)][inst[3]]

	return intCode

intCode = readIntCodeFile("input.txt")
output = []
intCodeComputer(intCode, [1], output)

print "#################################################################"
print "PART I  ==> puzzle answer = " + output[len(output)-1] + "    (right answer=12428642)"
print 

intCode = readIntCodeFile("input.txt")
output = []
intCodeComputer(intCode, [5], output)

print "#################################################################"
print "PART II ==> puzzle answer = " + output[len(output)-1] + "    (right answer=918655)"
print 

#printIntCode(intCode, "intCode: ")
#print "output=" + str(output)

