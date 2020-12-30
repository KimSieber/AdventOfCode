###################################################
##### AdventOfCode 2019
#####
##### Day 15 - Oxygen System
#####
##### @author  Kim Sieber
##### @date    05.12.2020 
###################################################
from random import *
### Konstanten
FILENAME = "input.txt"

### IntCode-Programm aus Datei einlesen
### @file_name					= (str) Dateiname
### @return 	int_code[0..n]	= (int) Programmschritte im IntCode
def readInput(file_name):
	input_file = open(FILENAME, "r")
	int_code_str = input_file.read().split(",")
	int_code_int = [int(i) for i in int_code_str]
	input_file.close()
	return int_code_int

class Computer:
	### Initialisierung mit Festlegung Parameter
	def __init__(self, intCode):
		self.intCode = intCode
		self.pos = 0
		self.input = None
		self.done = False
		self.relativeBase = 0

	#### Position im IntCode mode-abhaengig zurueckgeben
	def getPos(self, posIdx, mode):
		if   mode == 0:		return self.intCode[posIdx]
		elif mode == 1:		return posIdx
		elif mode == 2:		return self.intCode[posIdx] + self.relativeBase

		print("### ERROR ### getValue(posIdx=" + str(posIdx) + \
			  ", mode=" + str(mode) + ")  ==> unknown mode")
		exit()

	#### Daten lesen aus intCode
	#### @posIdx:  Position im IntCode zu lesen, muss noch in zu lesenden Parameter geaendert werden
	#### @mode  :  Lese-Modus - 0 = relativ, 1 = position, 2 = relativ + relativBase
	#### @return:  Wert aus Postition, Rueckgabe=0, wenn out-of-range
	def getValue(self, posIdx, mode):
		idx = self.getPos(posIdx, mode)
		if (len(self.intCode)-1) < idx:		return 0
		else:								return self.intCode[idx]

	#### Daten schreiben intCode, intCode-erweitern, wenn out-of-range
	#### @posIdx:  Position im IntCode angegeben, muss noch in zu schreibenden Parameter geaendert werden
	#### @mode  :  Lese-Modus - 0 = relativ, 1 = position, 2 = relativ + relativBase
	#### @value :  Zu schreibender Integer-Wert (+/-)
	def setValue(self, posIdx, mode, value):
		idx = self.getPos(posIdx, mode)
		if (len(self.intCode)-1) < idx:
			count = idx - (len(self.intCode) - 1)
			while count > 0:
				if DEBUG: print("append idx=" + str(idx))
				self.intCode.append(0)
				count -= 1
		self.intCode[idx] = value

	#### Instructionen auslesen
	#### @return instruction[opcode, mode1, mode2, mode3
	def readInstruction(self, instruction):
		instruction = ("0000" + instruction)[len("0000" + instruction)-5:]
		return [int(instruction[3:]), int(instruction[2:3]),  int(instruction[1:2]), int(instruction[0:1])]

	#### IntCodeComputer starten und durchlaufen
	#### @return:	->None, wenn Programm mit 99 beendet ist
	####            ->Integer-Wert, wenn IntComputer Wert ausgibt
	####            ->'input needed' wenn Eingabewert erforderlich
	####              (Programm hat gestoppt, ueber def setInput ist Wert zu setzen und anschl. 
	####			   runComputer() wieder auszufuehren)
	def runComputer(self):
		#output = 0
		opcode, mode1, mode2, mode3 = self.readInstruction(str(self.intCode[self.pos]))

		while True:
			#print "runComputer:start new while-loop: pos=" + str(self.pos) + "  opcode=" + str(opcode)

			if opcode == 1:
				self.setValue(self.pos+3, mode3, self.getValue(self.pos+1, mode1) + \
					                             self.getValue(self.pos+2, mode2))
				self.pos += 4
			elif opcode == 2:
				self.setValue(self.pos+3, mode3, self.getValue(self.pos+1, mode1) * \
					                             self.getValue(self.pos+2, mode2))
				self.pos += 4
			elif opcode == 3:
				if self.input == None:
					return "input needed"		
				else:
					self.setValue(self.pos+1, mode1, self.input)    #self.readInput())
					self.input = None
					#print "self.intCodeComputer:input <- " + str(self.getValue(self.pos+1, mode1))
					self.pos += 2
			elif opcode == 4:
				#print "self.intCodeComputer:output     -> " + str(self.getValue(self.pos+1, mode1))
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
				#print "opcode=9: relativeBase changed: " + str(self.relativeBase)
				self.pos += 2
			elif opcode == 99:
				#print "opcode = 99 - return ======================================"
				self.done = True
				return None
			else:
				print("ERROR in intCodeComputer - opcode == " + str(opcode))
				print("ERROR in intCodeComputer - pos    == " + str(self.pos))
				print("ERROR - cancel while-loop")
				exit()

			opcode, mode1, mode2, mode3 = self.readInstruction(str(self.intCode[self.pos]))


### Koordinaten der Aussenhuelle
### grid[(x,y)] = (str) '#' = Mauer (Wall)
###                     '.' = Huelle 
###                     'o' = Sauerstoff-Tank (oxygen-system)
grid = {}

### Werte der Richtungen
NORTH = 1
SOUTH = 2
WEST  = 3
EAST  = 4
### The repair droid can reply with any of the following status codes:
### 0: The repair droid hit a wall. Its position has not changed.
### 1: The repair droid has moved one step in the requested direction.
### 2: The repair droid has moved one step in the requested direction; 
###    its new position is the location of the oxygen system.
HITWALL  = 0
MOVED    = 1
MOVEDOXY = 2

### ZielKoordinate abhaengig Direction zurueckgebnen
### @pos 			: (x,y) Tuple, aktuelle Position
### @direction 		: (int) Richtung
### @return 		: (x,y) Tuple, mit neuer Position
def getNewPosition(pos, direction):
	if   direction == NORTH:		return (pos[0], pos[1]-1)
	elif direction == SOUTH:		return (pos[0], pos[1]+1)
	elif direction == WEST:			return (pos[0]-1, pos[1])
	elif direction == EAST:			return (pos[0]+1, pos[1])

### Laeuft von Start-Position so lange, bis Pfad gefunden, der noch nicht begangen
### und folgt diesem bis zum Ende, bis kein neuer Pfad mehr am Ende moeglich
### Gibt ergaenztes Grid, Anzahl Schritte und ob Oxygen-Systdm gefunden wurde zurueck
### @grid[(x,y)] 			= (str) Karte => '#', '.', 'o'
### @cmp 					= (object) instanziertes Objekt der Klasse Computer
### @method 				= (str) Methode, 'rightHand' oder 'findOxy'
### @return  grid[(x,y)] 	= (str) Karte => '#', '.', 'o'
###          cnt_moves      = (int) Anzahl Bewegungen, die in dieser Runde ausgefuehrt wurden
###          flag_oxy       = (bool) Kennzeichen, wenn Oxygen-System gefunden wurde
def runAnotherNewWay(grid, cmp, method='findOxy'):
	cnt_moves     = 0
	pos 	      = (0,0)
	dir_last_move = SOUTH

	### Prueft und gibt optimale Richtung zurueck, False, wenn Gegenrichtung = Sackgasse
	### @pos 			: (x,y) Tuple, aktuelle Position
	### @direction 		: (int) Letzte Richtung, die bewegt wurde und keine Mauer war
	### @return 		: (int) Neue Richtung
	def checkDir(pos, direction):
		### Ermittle Gegenrichtung
		opp_dir = lambda a : a-1 if a in (2,4) else a+1 if a in (1,3) else a
		dir_opp = opp_dir(direction)
		### Ermittle alle Richtungen ob bekannt und was dahinter
		dir_list = {}
		for nxt_dir in range(1,5):
			nxt_pos = getNewPosition(pos, nxt_dir)
			if nxt_pos not in grid.keys():
				dir_list[nxt_dir] = {'new': True}
			else:
				if nxt_dir == dir_opp:
					dir_list[nxt_dir] = {'new': False, 'opp': True, 'val': grid[nxt_pos]}
				else:
					dir_list[nxt_dir] = {'new': False, 'opp': False, 'val': grid[nxt_pos]}
		### Wenn Richtung neu, dann belassen
		if dir_list[direction]['new'] == True : 		return direction
		### Suche, welche Richtung neu ist, die erste zurueck geben
		for new_dir in dir_list:
			if dir_list[new_dir]['new'] == True:		return new_dir
		### Gebe Richtung zurueck, die nicht Gegenrichtung ist,
		### dabei wechselseitig vor oder zurueck-drehen im Kreis, damit nicht immer in gleiche Sackgasse
		if randint(0,1) == 0: rnd = [4,0,-1]
		else:		          rnd = [1,5,+1] 
		for new_dir in range(rnd[0],rnd[1],rnd[2]):
			if new_dir != dir_opp and dir_list[new_dir]['val'] != '#':
				return new_dir
		### Wenn Gegenrichtung, dann in Sackgasse = abbrechen
		return False

	### Prueft und gibt optimale Richtung zurueck, False, wenn Gegenrichtung = Sackgasse
	### @pos 			: (x,y) Tuple, aktuelle Position
	### @direction 		: (int) Letzte Richtung, die bewegt wurde und keine Mauer war
	### @return 		: (int) Neue Richtung oder False, wenn am Start zurueck
	def rightHandDir(pos, direction):
		### Ermittle Richtung rechte Hand
		right_hand_dir = lambda a: 4 if a==1 else 3 if a==2 else 1 if a==3 else 2
		dir_right_hand = right_hand_dir(direction)
		### Ermittle Richtung linke Hand
		left_hand_dir = lambda a: 3 if a==1 else 4 if a==2 else 2 if a==3 else 1
		dir_left_hand = left_hand_dir(direction)
		### Ermittle Gegenrichtung
		opp_dir = lambda a : a-1 if a in (2,4) else a+1 if a in (1,3) else a
		dir_opp = opp_dir(direction)
		### Pruefen ob Grid an rechter Hand bekannt
		rgh_pos = getNewPosition(pos, dir_right_hand)
		if rgh_pos not in grid.keys():
			return dir_right_hand
		if grid[rgh_pos] == 'X':  return False
		if grid[rgh_pos] != '#':
			return dir_right_hand
		else:
			### Wenn rechts Mauer, dann geradeaus pruefen
			nxt_pos = getNewPosition(pos, direction)
			if nxt_pos not in grid.keys():
				return direction
			if grid[nxt_pos] == 'X':  return False
			if grid[nxt_pos] != '#':
				return direction
			else:
				### Wenn gerade aus eine Mauer, dann links pruefen
				lft_pos = getNewPosition(pos, dir_left_hand)
				if lft_pos not in grid.keys():
					return dir_left_hand
				if grid[lft_pos] == 'X':  return False
				if grid[lft_pos] != '#':
					return dir_left_hand
				else:
					### Wenn links eine Mauer, dann zurueck
					return dir_opp

	while True:
		### Prueft, ob irgendeine Richtung noch unbekannt ist
		if method == "findOxy":
			direction = checkDir(pos, dir_last_move)
		elif method == "rightHand":
			direction = rightHandDir(pos, dir_last_move)
		### Abbruch => in Sackgasse
		if direction == False:
			return grid, cnt_moves, False, pos
		### Computer ausfuehren und neue Richtung Ergebnis verarbeiten
		cmp.input = direction
		answer    = cmp.runComputer()
		new_pos   = getNewPosition(pos, direction)
		if answer == HITWALL:
			grid[new_pos] = '#'
		elif answer == MOVED:
			pos = new_pos
			grid[new_pos] = '.'
			dir_last_move = direction
			cnt_moves += 1
		elif answer == MOVEDOXY:
			grid[new_pos] = 'o'
			pos = new_pos
			cnt_moves += 1
			if method == "findOxy": 	return grid, cnt_moves, True, pos

### Zeichnet das Grid
### grid[(x,y)] 	= (str) Karte => '#', '.', 'o'
def printGrid(grid):
	list_x, list_y = [key[0] for key in grid.keys()], [key[1] for key in grid.keys()]
	min_x, min_y, max_x, max_y = min(list_x), min(list_y), max(list_x), max(list_y)
	for y in range (min_y-1, max_y+2):
		line = ""
		for x in range(min_x-1, max_x+2):
			if (x,y) not in grid.keys():
				line += " "
			else:
				line += grid[(x,y)]
		print(line)



intCode = readInput(FILENAME)

### PART I  : Finde das Oxygen-System
cnt = 0
flag_oxy = False
while flag_oxy == False:
	cnt += 1
	cmp = Computer(intCode[:])
	grid, cnt_cmd, flag_oxy, last_pos = runAnotherNewWay(grid, cmp)

print()
print("GRID need ",cnt," starts to find oxygen-system:")
grid[(0,0)] = 'X'
printGrid(grid)

print()
print("PART I  : The fewest number of movements to oxygen-system : ", cnt_cmd, "  (204)")
print()

### PART II : Verfollstaendige Karte
cmp = Computer(intCode[:])
grid, cnt_cmd, flag_oxy, last_pos = runAnotherNewWay(grid, cmp, 'rightHand')

print()
print("GRID completed: ")
grid[(0,0)] = 'X'
printGrid(grid)
print()

### PART II : Fuelle mit Sauerstoff auf und Zaehle Minuten
minutes  = 0
cnt_free = 1
while cnt_free > 0:
	minutes += 1
	### Suche Position Sauerstoff-System
	list_oxy = [pos for pos in grid.keys() if grid[pos]=='o']
	### Fuer alle Sauerstoff-Teile, suche Nachbarn und lasse diese zu Sauerstoff werden, wenn keine Wand
	for oxy in list_oxy:
		for adj_dir in range(1,5):
			adj_pos = getNewPosition(oxy, adj_dir)
			if grid[adj_pos] == '.':
				grid[adj_pos] = 'o'
	cnt_free = len([pos for pos in grid.keys() if grid[pos]=='.'])

print()
print("GRID after filled with oxygen:")
grid[(0,0)] = 'X'
printGrid(grid)

print()
print("PART II : Minutes it take to fill all area with oxygen: ", minutes)
print()

