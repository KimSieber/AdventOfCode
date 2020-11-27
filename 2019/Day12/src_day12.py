###################################################
##### AdventOfCode
#####
##### Day 12 - The N-Body Problem
#####
##### @author  Kim Sieber
##### @date    26.11.2020
###################################################

### Input-Puzzle
# Io         =>  pos= <x= -6, y=  2, z= -9> vel= <x=0, y=0, z=0>
# Europa     =>  pos= <x= 12, y=-14, z= -4> vel= <x=0, y=0, z=0>
# Ganymede   =>  pos= <x=  9, y=  5, z= -6> vel= <x=0, y=0, z=0>
# Callisto   =>  pos= <x= -1, y= -4, z=  9> vel= <x=0, y=0, z=0>

### Konstanten
x = 0
y = 1
z = 2

### Mond-Klasse
class Moon:
	### Initialisierung
	### @pos   : Position in den Koordinaten x,y,z   mit pos[x]=x, pos[y]=y, pos[z]=z
	def __init__ (self, name, pos):
		self.name = name
		self.pos = pos
		self.vel = [0,0,0]
		self.timeStap = 0
		self.moonState = []               # List mit Stati zum Ausdruck
		self.setMoonState()

	### Setzt die Status-Daten in eine Protokoll-Liste
	def setMoonState(self):
		self.moonState.append( \
				      "=> " + ("            " + str(self.timeStap))[len("            "+str(self.timeStap))-12:] + "  " + \
		              (self.name+"       ")[0:8] + "  " + \
		              "pos = <x=" + ("   "+str(self.pos[x]))[len("   "+str(self.pos[x]))-4:] + ", " + \
		                   "y=" + ("   "+str(self.pos[y]))[len("   "+str(self.pos[y]))-4:] + ", " + \
		                   "z=" + ("   "+str(self.pos[z]))[len("   "+str(self.pos[z]))-4:] + ">    " + \
		              "vel = <x=" + ("   "+str(self.vel[x]))[len("   "+str(self.vel[x]))-4:] + ", " + \
		                   "y=" + ("   "+str(self.vel[y]))[len("   "+str(self.vel[y]))-4:] + ", " + \
		                   "z=" + ("   "+str(self.vel[z]))[len("   "+str(self.vel[z]))-4:] + ">")

	### Druckt Stati aus Protokollliste
	def printMoonStates(self):
		for n in self.moonState:
			print n

	### Druckt letzten Status-Eintrag der Protokollliste
	def printLastMoonState(self):
		print (self.moonState[len(self.moonState)-1])

	### Veraendert Geschwindigkeit auf Basis mitgegebenem Mond
	def applyGravity(self, moon):
#		print "applyGravity: self.pos[x,y,z]=" + str(self.pos[x]) + "," + str(self.pos[y]) + "," + str(self.pos[z])
#		print "applyGravity: moon.pos[x,y,z]=" + str(moon.pos[x]) + "," + str(moon.pos[y]) + "," + str(moon.pos[z])
		if self.pos[x] > moon.pos[x]:
			self.vel[x] -= 1
		elif self.pos[x] < moon.pos[x]:
			self.vel[x] += 1

		if self.pos[y] > moon.pos[y]:
			self.vel[y] -= 1
		elif self.pos[y] < moon.pos[y]:
			self.vel[y] += 1

		if self.pos[z] > moon.pos[z]:
			self.vel[z] -= 1
		elif self.pos[z] < moon.pos[z]:
			self.vel[z] += 1
#		print "applyGravity: self.vel[x,y,z]=" + str(self.vel[x]) + "," + str(self.vel[y]) + "," + str(self.vel[z])

	### Positionen veraendern, auf Basis Geschwindigkeit
	def applyPosition(self):
		self.pos[x] += self.vel[x]
		self.pos[y] += self.vel[y]
		self.pos[z] += self.vel[z]

		self.timeStap += 1
		self.setMoonState()

	### Berechnet die Gesamt-Energie des Mondes
	def getTotalEnergy(self):
		return  sum(abs(i) for i in self.pos) * sum(abs(j) for j in self.vel)

#instruction = ("0000" + instruction)[len("0000" + instruction)-5:]

### Druckt letzte Stati zu allen 4 Monden aus
def printStatus():
	print
	for m in moons:
		m.printLastMoonState()

def apply():
	for m in moons:
		for n in moons:
			if m != n:
				m.applyGravity(n)
	for m in moons:
		m.applyPosition()

def totalEnergy():
	energy = 0
	for m in moons:
		energy += m.getTotalEnergy()
	return energy


from copy import deepcopy
#####################################################
### PART I
#####################################################
### ==> Puzzle-Input => Monde instanzieren
variant = 2
loops   = 1000
debug   = False
### [0] ist Example 1
### [1] ist Example 2
### [2] ist Puzzle Input
moonVariants = [ [Moon("Io",       [-1,   0,  2]),   \
                  Moon("Europa",   [ 2, -10, -7]),   \
                  Moon("Ganymede", [ 4,  -8,  8]),   \
                  Moon("Callisto", [ 3,   5, -1]) ], \
                                                     \
                 [Moon("Io",       [-8, -10,  0]),   \
                  Moon("Europa",   [ 5,   5, 10]),   \
                  Moon("Ganymede", [ 2,  -7,  3]),   \
                  Moon("Callisto", [ 9,  -8, -3]) ], \
                                                     \
                 [Moon("Io",       [-6,   2, -9]),   \
                  Moon("Europa",   [12, -14, -4]),   \
                  Moon("Ganymede", [ 9,   5, -6]),   \
                  Moon("Callisto", [-1,  -4,  9]) ] ]

moons = deepcopy(moonVariants[variant])

if debug: printStatus()
for i in range(0,loops):
	apply()
	if debug: printStatus()

print
print "#########################################################################################"
print "# PART I  ==> Sum of total energy: " + str(totalEnergy()) + "  (right answer: 14907)"
print "#"
print

#####################################################
### PART II
#####################################################
### ==> Puzzle-Input => Monde instanzieren
variant = 2
debug = False

moons = deepcopy(moonVariants[variant])
moonInitSumPos = [sum(m.pos[x] for m in moons), sum(m.pos[y] for m in moons), sum(m.pos[z] for m in moons)]
moonInitSumVel = [0,0,0]

### prueft, ob alle Vel einer Achse auf 0 stehen
### @moons  : Monde, die geprueft werden sollen
### @axis   : Achse x/y/z, die geprueft werden soll
### @return : True, wenn die Velocity bei allen Monden der angegebnen Achse vel=0 stehen, sonst False
def checkVelocityZero(moons, axis):
	for m in moons:
		if m.vel[axis] != 0:
			return False
	return True

if debug:
	print "moonInitSumPos: " + str(moonInitSumPos)
	printStatus()

xyzChecked = [False, False, False]
rememberTimeStap = []
while True:
	apply()

	
	### Pruefen, ob alle Velocity der Monde=0 und die Summe der Positionen auf einer Achse aller Monde gleich der InitialSumme ist
	### Nur einmal pruefen und ersten Wert merken
	if sum(m.pos[x] for m in moons) == moonInitSumPos[x] and checkVelocityZero(moons, x) and xyzChecked[x] == False:
				rememberTimeStap.append(moons[0].timeStap)
				xyzChecked[x] = True
				if debug: printStatus()
	elif sum(m.pos[y] for m in moons) == moonInitSumPos[y] and checkVelocityZero(moons, y) and xyzChecked[y] == False:
				rememberTimeStap.append(moons[0].timeStap)
				xyzChecked[y] = True
				if debug: printStatus()
	elif sum(m.pos[z] for m in moons) == moonInitSumPos[z] and checkVelocityZero(moons, z) and xyzChecked[z] == False:
				rememberTimeStap.append(moons[0].timeStap)
				xyzChecked[z] = True
				if debug: printStatus()

	if xyzChecked == [True, True, True]:
		break

### Ergebnisse summieren
s = 1
for r in rememberTimeStap:
	s = s * r

print
print "#########################################################################################"
print "# PART II ==> Steps to inital position: " + str(s)
print "#                                                        right answer: 467.081.194.429.464"
print "#                                                        Example I:                  2.772"
print "#                                                        Example II:  IST    7.030.162.386"
print "#                                                                     SOLL   4.686.774.924"
print





