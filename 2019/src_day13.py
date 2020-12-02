###################################################
##### AdventOfCode
#####
##### Day 13 - Care Package
#####
##### @author  Kim Sieber
##### @date    27.11.2020
###################################################

# TODO
# Computer umbauen, damit ich den Bidlschirm ausgeben kann und er dann auf Joystick-Eingabe wartet

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
		self.valueInput = None
		self.newInput = False
		self.done = False
		self.debug = debug
		self.relativeBase = 0

	#### Setzt Input-Wert fuer naechsten Input (Seq-Nr. 3)
	def setInput(self, Input):
		self.valueInput = Input
		self.newInput = True

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

	### Input aus Datei lesen
	### @return:	Wert fuer -1=links, 0=nichts, 1 = rechts
#	def readInput(self):
#		FILENAME = "cmd.txt"
#		file = open(FILENAME, "r")
#		cmd = [0, -1, 0, 1]					# => Eingabe 1 2 3, da besser auf Tastatur als -1 0 1
#		return cmd[int(file.read())]

	#### IntCodeComputer starten und durchlaufen
	#### @return:	->None, wenn Programm mit 99 beendet ist
	####            ->Integer-Wert, wenn IntComputer Wert ausgibt
	####            ->'input needed' wenn Eingabewert erforderlich
	####              (Programm hat gestoppt, ueber def setInput ist Wert zu setzen und anschl. runComputer() wieder auszufuehren)
	def runComputer(self):
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
				if self.newInput:
					self.setValue(self.pos+1, mode1, self.valueInput)    #self.readInput())
					self.newInput = False
					if self.debug: print "self.intCodeComputer:input <- " + str(self.getValue(self.pos+1, mode1))
					self.pos += 2
				else:
					return "input needed"		
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

### Kachel (tile)-Definitionen
### The tile id is interpreted as follows:
## 0 is an empty tile. No game object appears in this tile.
## 1 is a wall tile. Walls are indestructible barriers.
## 2 is a block tile. Blocks can be broken by the ball.
## 3 is a horizontal paddle tile. The paddle is indestructible.
## 4 is a ball tile. The ball moves diagonally and bounces off objects.
name = 0
sign = 1
tile = [["empty",             " "], \
        ["wall",              "="], \
 		["block",             "#"], \
		["horizontal paddle", "-"], \
		["ball",              "O"]    ]

### Klasse Arcade-Spiel
class Arcade:
	### Initialisierung
	### @intCode      : IntCode-Programm als Array
	### @sizeX / Y    : Erzeugt einen Monitor mit X-Range x Y-Range-Feldern (range initial je 50)
	def __init__ (self, intCode, sizeX=50, sizeY=50):
		self.Monitor = self.buildMonitor(sizeX, sizeY)		# im Format Monitor[y][x]
		self.Computer = Computer(intCode[:], 0)
		self.countBlocks = 0
		self.score = 0
		

	### Erzeugt einen Bildschirm
	### @size     : Erzeugt einen Bildschirm  mit x-Range x y-Range-Feldern
	def buildMonitor(self, sizeX, sizeY):
		Monitor = []
		for y in range(0,sizeY):
			tempMap = []
			for x in range (0,sizeX):
				tempMap.append(0)
			Monitor.append(tempMap)
		return Monitor

	### Laesst Computer 3x laufen, und Schreibt Objekt in Variable Monitor
	### @return:  1=True bei Erfolg, 0=False wenn Programm zu Ende, und -1=Input, wenn Eingabe erforderlich
	def readObject(self):
		objX = self.Computer.runComputer()
		objY = self.Computer.runComputer()
		objId = self.Computer.runComputer()
		if objId == 'input needed':
			return -1
		if objX == None or objY == None or objId == None:
			return 0
		if objId == 2:
			self.countBlocks += 1
		if objX == -1 and objY == 0:
			self.score = objId
			return 1
		self.Monitor[objY][objX] = objId
		return 1

	#### Setzt Input-Wert fuer naechsten Input 
	def setInput(self, Input):
		self.Computer.setInput(Input)

	### Ermittelt Position x-Achse von Ball
	### @objectType : Objekt-Typ mit Zahl 1-4
	### @return     : X-Position
	def getPositionX(self, objectType):
		for y in self.Monitor:
			i = 0
			for x in y:
				if x == objectType:
					return i
				i += 1

	### Druckt Monitor mit in globaler Variable tile[][] definierten Zeichen
	def printMonitor(self):
		#print "***** Map *****"
		for x in self.Monitor:
			line = ""
			for y in x:
				line = line + str(tile[y][sign])
			print line
		print "Your Score: " + str(self.score)



intCode = readIntCodeFile("input.txt")

#####################################################
### PART I
#####################################################
arc = Arcade(intCode[:], 42, 23)
while arc.readObject():
	True

arc.printMonitor()
print
print "#########################################################################################"
print "# PART I  ==> count block-tiles in Screen :  " + str(arc.countBlocks) + "     (right answer: 277)"
print "#"
print


#####################################################
### PART II
#####################################################
import time
playMode    = 1 			# playMode 0 = manuelle Steuerung Paddel, 1 = automatischer Ablauf
playSleep   = 0.0			# Bei playMode = 1, Wartezeit in Sekunden, bis neue Eingabe, damit visuell nachvollziehbar 
playVisible = False			# Ob Spielfeld/Monitor angezeigt werden soll oder nicht
intCode[0]  = 2				# Coin input, 2 = pay for free
arc = Arcade(intCode[:], 42, 23)

#### Fuehrt Input aus und gibt Wert zurueck
#### @return: Wert -1, 0, 1
def getInput():
	ret = raw_input("Bitte Steuerungswert eingeben (4=Links, 5=Bleiben, 6=Rechts, exit=Ende): ")
	if ret == '4':
		return -1
	if ret == '6':
		return 1
	if ret == 'exit':
		exit()
	return 0

##### Bildet Input-Wert auf Basis der Differenz der X-Achsen von Paddel und Ball
##### @arc    = Arcode-Objekt
##### @ret    = Input-Wert in -1, 0, 1
def buildInput(arc):
	xBall   = arc.getPositionX(4)
	xPaddel = arc.getPositionX(3)
	if xBall < xPaddel:
		return -1
	if xBall > xPaddel:
		return 1
	return 0

loop = True
ret = 0
i = 0
while loop:
	i += 1
	while True:
		ret = arc.readObject()
		if ret == -1:						# Input erwartet
			break
		elif ret == 0:						# Programm beendet
			loop = False
			break
	if playVisible:
		arc.printMonitor()
	if ret == -1:
		if playMode == 0:
			arc.setInput(int(getInput()))
		elif playMode == 1:
			Input = buildInput(arc)
			arc.setInput(Input)
			time.sleep(playSleep)

arc.printMonitor()
print
print "#########################################################################################"
print "# PART II ==> High-Score.                  :  " + str(arc.score) + "    (right answer: 12856)"
print "#"
print


