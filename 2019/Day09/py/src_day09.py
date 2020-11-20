###################################################
##### AdventOfCode
#####
##### Day 9 - Sensor Boost with IntCode-Computer
#####
##### @author  Kim Sieber
##### @date    20.11.2020
###################################################

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

class computer:
	### Initialisierung mit Festlegung Parameter
	def __init__(self, intCode, seq, debug = False):
		self.intCode = intCode
		self.pos = 0
		self.seq = seq
		self.firstInput = True
		self.done = False
		self.debug = debug
		self.relativeBase = 0

	#### Position im IntCode mode-abhaengig zurueckgeben
	def getPos(self, posIdx, mode):
		if mode == 0:
			idx = self.intCode[posIdx]
		elif mode == 1:
			idx = posIdx
		elif mode == 2:
			idx = self.intCode[posIdx] + self.relativeBase
		else:
			print "### ERROR ### getValue(posIdx=" + str(posIdx) + ", mode=" + str(mode) + ")  ==> unknown mode"
			exit()
		return idx


	#### Daten lesen aus intCode
	#### @posIdx:  Position im IntCode zu lesen, muss noch in zu lesenden Parameter geaendert werden
	#### @mode  :  Lese-Modus - 0 = relativ, 1 = position, 2 = relativ + relativBase
	#### @return:  Wert aus Postition, Rueckgabe=0, wenn out-of-range
	def getValue(self, posIdx, mode):
		idx = self.getPos(posIdx, mode)
		if (len(self.intCode)-1) < idx:
			return 0
		else:
			return self.intCode[idx]

	#### Daten schreiben intCode, intCode-erweitern, wenn out-of-range
	#### @posIdx:  Position im IntCode angegeben, muss noch in zu schreibenden Parameter geaendert werden
	#### @mode  :  Lese-Modus - 0 = relativ, 1 = position, 2 = relativ + relativBase
	#### @value :  Zu schreibender Integer-Wert (+/-)
	#### @return:  True, nachdem geschrieben
	def setValue(self, posIdx, mode, value):
		idx = self.getPos(posIdx, mode)
		if (len(self.intCode)-1) < idx:
			count = idx - (len(self.intCode) - 1)
			while count > 0:
				if self.debug: print "append idx=" + str(idx)
				self.intCode.append(0)
				count -= 1
			self.intCode[idx] = value
		else:
			self.intCode[idx] = value
		return True


	#### Instructionen auslesen
	#### @return instruction[opcode, mode1, mode2, mode3
	def readInstruction(self, instruction):
		instruction = ("0000" + instruction)[len("0000" + instruction)-5:]
		return [int(instruction[3:]), int(instruction[2:3]),  int(instruction[1:2]), int(instruction[0:1])]

	#### IntCodeComputer starten und durchlaufen
	def runComputer(self, signal):
		if self.debug: print "runComputer:start (seq=" + str(self.seq) + " and signal=" + str(signal) + ")"
		output = 0
		inst = self.readInstruction(str(self.intCode[self.pos]))
		opcode = inst[0]
		mode1  = inst[1]
		mode2  = inst[2]
		mode3  = inst[3]

		while True:
			if self.debug: print "runComputer:start new while-loop: pos=" + str(self.pos) + "  opcode=" + str(opcode)

			if opcode == 1:
				self.setValue(self.pos+3, mode3, self.getValue(self.pos+1, mode1) + self.getValue(self.pos+2, mode2))
				self.pos += 4
			elif opcode == 2:
				self.setValue(self.pos+3, mode3, self.getValue(self.pos+1, mode1) * self.getValue(self.pos+2, mode2))
				self.pos += 4
			elif opcode == 3:
				if self.firstInput == True:
					self.setValue(self.pos+1, mode1, self.seq)
					self.firstInput = False
				else:
					self.setValue(self.pos+1, mode1, signal)
				if self.debug: print "self.intCodeComputer:input <- " + str(self.getValue(self.pos+1, mode1))
				self.pos += 2
			elif opcode == 4:
				if self.debug: print "self.intCodeComputer:output     -> " + str(self.getValue(self.pos+1, mode1))
				output = self.getValue(self.pos+1, mode1)
				self.pos += 2
				return output
			elif opcode == 5:
				if self.getValue(self.pos+1, mode1) != 0:
					self.pos = self.getValue(self.pos+2, mode2)
				else:
					self.pos += 3
			elif opcode == 6:
				if self.getValue(self.pos+1, mode1) == 0:
					self.pos = self.getValue(self.pos+2, mode2)
				else:
					self.pos += 3
			elif opcode == 7:
				if self.getValue(self.pos+1, mode1) < self.getValue(self.pos+2, mode2):
					self.setValue(self.pos+3, mode3, 1)
				else:
					self.setValue(self.pos+3, mode3, 0)
				self.pos += 4
			elif opcode == 8:
				if self.getValue(self.pos+1, mode1) == self.getValue(self.pos+2, mode2):
					self.setValue(self.pos+3, mode3, 1)
				else:
					self.setValue(self.pos+3, mode3, 0)
				self.pos += 4
			elif opcode == 9:
				self.relativeBase += self.getValue(self.pos+1, mode1)
				if self.debug: print "opcode=9: relativeBase changed: " + str(self.relativeBase)

				self.pos += 2
			elif opcode == 99:
				if self.debug: print "opcode = 99 - return ======================================"
				self.done = True
				return None
			else:
				print "ERROR in intCodeComputer - opcode == " + str(opcode)
				print "ERROR in intCodeComputer - pos    == " + str(self.pos)
				print "ERROR - cancel while-loop"
				break

			inst = self.readInstruction(str(self.intCode[self.pos]))
			opcode = inst[0]
			mode1  = inst[1]
			mode2  = inst[2]
			mode3  = inst[3]

		return output


intCode = readIntCodeFile("input.txt")

def run(intCode, input, debug=False):
	allReturnCodes = []
	comp = computer(intCode[:], input, debug)
	while not comp.done:
		returnCode = comp.runComputer(input)
		if returnCode != None:
			allReturnCodes.append(returnCode)
	return allReturnCodes

#####################################################
### PART I
#####################################################
debug = False

allReturnCodes = run(intCode[:], 1, debug)

print "#########################################################################################"
print "PART I  ==> puzzle answer:  " + str(allReturnCodes[0]) + "         (right answer: 2427443564)"
print "            allReturnCodes: " + str(allReturnCodes)
print 

#####################################################
### PART II
#####################################################
debug = False

allReturnCodes = run(intCode[:], 2, debug)


print "#########################################################################################"
print "PART II ==> puzzle answer:  " + str(allReturnCodes[0]) + "              (right answer: 87221)"
print "            allReturnCodes: " + str(allReturnCodes)
print 

