###################################################
##### AdventOfCode
#####
##### Day 7 - Thruster-Loop with the intCode-Computer
#####
##### @author  Kim Sieber
##### @date    16.11.2020 - 19.11.2020
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

	#### Instructionen auslesen
	#### @return instruction[opcode, mode1, mode2, mode3
	def readInstruction(self, instruction):
		instruction = ("0000" + instruction)[len("0000" + instruction)-5:]
		return [int(instruction[3:]), int(instruction[2:3]),  int(instruction[1:2]), int(instruction[0:1])]

	#### IntCodeComputer starten und durchlaufen
	def runComputer(self, signal):
		if self.debug == True:
			print "intCodeComputer:start with seq=" + str(self.seq) + " and signal=" + str(signal)
		output = 0
		inst = self.readInstruction(str(self.intCode[self.pos]))
		opcode = inst[0]

		while True:
			if len(self.intCode)-1 > self.pos+1:
				self.posParam1 = [self.intCode[self.pos+1], (self.pos+1)][inst[1]]
				if len(self.intCode)-1 > self.pos+2:
					self.posParam2 = [self.intCode[self.pos+2], (self.pos+2)][inst[2]]
					if len(self.intCode)-1 > self.pos+3:
						self.posParam3 = [self.intCode[self.pos+3], (self.pos+3)][inst[3]]

			if opcode == 1:
				self.intCode[self.posParam3] = self.intCode[self.posParam1] + self.intCode[self.posParam2]
				self.pos += 4
			elif opcode == 2:
				self.intCode[self.posParam3] = self.intCode[self.posParam1] * self.intCode[self.posParam2]
				self.pos += 4
			elif opcode == 3:
				if self.firstInput == True:
					self.intCode[self.posParam1] = self.seq
					self.firstInput = False
				else:
					self.intCode[self.posParam1] = signal
				if self.debug == True:
					print "self.intCodeComputer:input <- " + str(self.intCode[self.posParam1])
				self.pos += 2
			elif opcode == 4:
				if self.debug == True:
					if self.debug == True:
						print "self.intCodeComputer:output     -> " + str(self.intCode[self.posParam1])
				output = self.intCode[self.posParam1]
				self.pos += 2
				return output
			elif opcode == 5:
				if self.intCode[self.posParam1] != 0:
					self.pos = self.intCode[self.posParam2]
				else:
					self.pos += 3
			elif opcode == 6:
				if self.intCode[self.posParam1] == 0:
					self.pos = self.intCode[self.posParam2]
				else:
					self.pos += 3
			elif opcode == 7:
				if self.intCode[self.posParam1] < self.intCode[self.posParam2]:
					self.intCode[self.posParam3] = 1
				else:
					self.intCode[self.posParam3] = 0
				self.pos += 4
			elif opcode == 8:
				if self.intCode[self.posParam1] == self.intCode[self.posParam2]:
					self.intCode[self.posParam3] = 1
				else:
					self.intCode[self.posParam3] = 0
				self.pos += 4
			elif opcode == 99:
				if self.debug == True:
					print "opcode = 99 - return ======================================"
				self.done = True
				return None
			else:
				print "ERROR in intCodeComputer - opcode == " + str(opcode)
				print "ERROR in intCodeComputer - pos    == " + str(self.pos)
				print "ERROR - cancel while-loop"
				break

			inst = self.readInstruction(str(self.intCode[self.pos]))
			opcode = inst[0]

		return output

def getIdxOfListitem(list, item):
	i = 0
	for value in list:
		if value == item:
			return i
		i += 1

from itertools import permutations

#####################################################
### PART I
#####################################################

debug = False

intCode = readIntCodeFile("input.txt")

allSignals = []
sequences = list(permutations([0,1,2,3,4]))
for sequence in sequences:
	signal = 0
	for i in sequence:
		comp = computer(intCode, i, debug)
		signal = comp.runComputer(signal)
	allSignals.append(signal)

maxSignal = max(allSignals)
maxSignalIdx = getIdxOfListitem(allSignals, maxSignal)
maxSignalSeq = sequences[maxSignalIdx]

print "#########################################################################################"
print "PART I  ==> puzzle answer: thruster-signal = " + str(maxSignal) + "            (right answer=51679)"
print "                           on Index        = " + str(maxSignalIdx) + "               (right answer=55)"
print "                           on Squence      = " + str(maxSignalSeq)  + "  (right answer=[2, 1, 0, 4, 3]"
print 


#####################################################
### PART II
###
### BESONDERHEIT: AmpA bis AmpE als Objekte erzeugen.
### Jeder Amp wird bei Wiederaufruf ind er Schleife
### an dem Programmpunkt wieder aufgesetzt, an dem er
### zuvor beendet ist. Daher als Objekte wichtig
#####################################################

debug = False

intCode = readIntCodeFile("input.txt")

def runLoopWithSequence(intCode, sequence, debug = False):
	sig = 0
	lastSig = 0
	amplifier = [computer(intCode[:], phase, debug) for phase in sequence]

	while not any([amp.done for amp in amplifier]):
		for ampl in amplifier:
			sig = ampl.runComputer(sig)
			if sig is not None:
				lastSig = sig

	return lastSig
	
allSignals = []
sequences = list(permutations([9,8,7,6,5]))
for sequence in sequences:
	allSignals.append(runLoopWithSequence(intCode[:], sequence, debug))

maxSignal = max(allSignals)
maxSignalIdx = getIdxOfListitem(allSignals, maxSignal)
maxSignalSeq = sequences[maxSignalIdx]

print "#########################################################################################"
print "PART II ==> puzzle answer: thruster-signal = " + str(maxSignal) + "         (right answer=19539216)"
print "                           on Index        = " + str(maxSignalIdx) + "               (right answer=16)"
print "                           on Squence      = " + str(maxSignalSeq)  + "  (right answer=[9, 6, 5, 8, 7]"
print 
