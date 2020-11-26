###################################################
##### AdventOfCode
#####
##### Day 11 - Space Police
#####
##### @author  Kim Sieber
##### @date    25.11.2020
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

class Computer:
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


### Klasse Map
class Robot:
	### Initialisierung
	### @size         : Erzeugt eine Karte mit Range x Range-Feldern (range initial = 50)
	### @startX/startY: Startposition des Roboters auf dem Feld, sollte 1/2 von Size sein
	def __init__ (self, sizeX=50, sizeY=50, startX=25, startY=25):
		self.Map = self.buildMap(sizeX, sizeY)
		self.pos = [startX, startY]                #pos[0]=x  pos[1]=y  :ist die aktuelle Position des Roboters, verhaendert sich im Ablauf
		self.dir = 0							   #dir = Richtung des Roboters, 0=Nord, 1=Ost, 2=Sued, 3=West
		self.listPainted = []

	### Erzeugt eine Karte
	### @size     : Erzeugt eine Karte mit Range x Range-Feldern
	def buildMap(self, sizeX, sizeY):
		Map = []
		for y in range(0,sizeY):
			tempMap = []
			for x in range (0,sizeX):
				tempMap.append(0)
			Map.append(tempMap)
		return Map

	### Druckt Map mit . fuer 0=schwarz und # fuer 1=weiss
	def printMap(self, signWight=".", signBlack="#"):
		#print "***** Map *****"
		for x in self.Map:
			line = ""
			for y in x:
				line = line + str([signWight,signBlack][y])
			print line

		return
		### Koordinaten drehen fuer richtige Anzeige
		printMap = self.buildMap(len(self.Map), len(self.Map[0]))
		for i in range(len(self.Map)):
			for j in range(len(self.Map)):
				printMap[i][j] = str([signWight,signBlack][self.Map[j][i]])
		print "***** Map *****"
		for x in printMap:
			line = ""
			for y in x:
				line = line + y
			print line

	### Gibt die Farbe der aktuellen Position zurueck
	def getColor(self):
		#print "Map:getColor - pos[x/y]: " + str(self.pos[0]) + " / " + str(self.pos[1])
		return self.Map[self.pos[1]][self.pos[0]]

	### Malt Farbe auf Board an aktueller Position
	### @color  : Farbe zu malen, 0=schwarz, 1=weiss
	def paint(self, color):
		if color == None: 
			print "ERROR Map.paint(color=None)"
			exit(0)

		self.Map[self.pos[1]][self.pos[0]] = color
		self.listPainted.append(self.pos[1]*1000 + self.pos[0])

	### Bewegt Roboter auf neue Position
	def move(self, direction):
		### Richtung aendern
		if direction == 0:
			self.dir -= 1
			if self.dir < 0:
				self.dir = 3
		else:   #direction=1
			self.dir += 1
			if self.dir > 3:
				self.dir = 0

		### Roboter bewegen: Position aendern
		if self.dir == 0:
			self.pos[1] -= 1
		elif self.dir == 1:
			self.pos[0] += 1
		elif self.dir == 2:
			self.pos[1] += 1
		elif self.dir == 3:
			self.pos[0] -= 1
		else:
			print "Map:move() ### ERROR ### dir=" + str(self.dir)



debug = False
intCode = readIntCodeFile("input.txt")

#####################################################
### PART I
#####################################################

panelColor = 0		# 0=black, 1=white
paintColor = 0
direction = 0
computer = Computer(intCode[:], panelColor, debug)
robot = Robot(130, 100, 35, 60)
loop = True
i = 0
while loop:
	panelColor = robot.getColor()
	paintColor = computer.runComputer(panelColor)
	direction  = computer.runComputer(panelColor)
#	print "loop: " + str(i) + " panelColor:" + str(panelColor) + " / paintColor:" + str(paintColor) + " / direction:" + str(direction) + \
#	           " / Map.dir:" + str(robot.dir) + " / pos x.y:" + str(robot.pos[0]) + "." + str(robot.pos[1])
	if paintColor == None or direction == None:
		loop = False
		break
	robot.paint(paintColor)
	robot.move(direction)
	i+=1

if debug: robot.printMap()

##### Auflistung der gedruckten Panel redundanzfrei zaehlen
i = n = 0
for li in robot.listPainted:
	tmp = li
	robot.listPainted[i] = 0
	if tmp not in robot.listPainted:
		n += 1
	i += 1

print "#########################################################################################"
print "# PART I  ==> number of panels painted:   " + str(n) + "  (right answer: 2392)"
print "#"
print


#####################################################
### PART II
#####################################################

panelColor = 1		# 0=black, 1=white
paintColor = 0
direction = 0
computer = Computer(intCode[:], panelColor, debug)
robot = Robot(50, 10, 2, 2)
loop = True
while loop:
	panelColor = robot.getColor()
	paintColor = computer.runComputer(panelColor)
	direction  = computer.runComputer(panelColor)
	if paintColor == None or direction == None:
		loop = False
		break
	robot.paint(paintColor)
	robot.move(direction)
	i+=1

print "#########################################################################################"
print "# PART II ==> registration ID:                  (right answer: EGBHLEUE)"
print "#             Hull-Painting: "
robot.printMap(" ", "#")
print
