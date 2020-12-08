##################################################
##### AdventOfCode 2020
#####
##### Day 08 - HHandheld Halting
#####
##### @author  Kim Sieber
##### @date    08.12.2020
###################################################
### Parameter
FILENAME = "input.txt"

### Datenstruktur des Programms
### prg[0..n]['cmd']    = (str)  Komando nop, acc oder jmp
###          ['val']    = (int)  Zahlenwert, mit dem gerechnet wird
###          ['flg']    = (bool) Flag, ob die Funktion schonmal ausgefuert wurde
###          ['chg']	= (bool) Flag, ob diese Funktion von nop auf jmp oder umgekehrt schonmal geaendert wurde
###                       HINWEIS: Es findet keine Veraenderung des Programms statt, sondern bei Laufzeit anders interpretiert
prg = []

### Wert des Accumulators
acc = 0

### Liest Datei ein und erzeugt regulations-Liste
def readInputFile():
	global prg
	prg = []
	cmd = {}
	inputFile = open(FILENAME, "r")
	for line in inputFile:
		cmd = {}
		parts = line.split(" ")
		cmd['cmd'] = parts[0]
		cmd['val'] = int(parts[1])
		cmd['flg'] = False
		cmd['chg'] = False
		prg.append(cmd)
	inputFile.close()

### Laesst das Programm ablaufen
### - setzt zum Start die globale Variable acc immer auf 0
### @chg	: (bool) Kennzeichen, ob ein veraendertes Programm ausprobiert werden soll
### @return : (bool) True, wenn das Programm ordungsgemaess zu Ende gelaufen ist,
###                  sonst False, wenn Programm zum 2. Mal eine Stelle erreichte 
###                  und damit abgebrochen wurde
def runPrg(chg=False):
	#rint("################## START runProg(" + str(chg) + ") ###################")
	### Global prg and reset flg=False
	global prg
	i = 0
	for cmd in prg:
		prg[i]['flg'] = False
		i += 1
	### Global acc and set acc=0
	global acc
	acc = 0
	### Local Counter for Programm-Positon
	pos = 0
	### Local Change-Flag, da in einem Durchlauf nur eine Aenderung zulässig
	chgFlag = False
	while True:
		### END, wenn Programm zu Ende = out of range
		if pos >= len(prg):
			#print("==! END  (True) : pos=" + str(pos) + " chgFlag=" + str(chgFlag) + " acc=" + str(acc))
			return True
		### STOP, wenn Stelle schonmal durchlaufen wurde
		if prg[pos]['flg'] == True:
			#print("==! END  (False): pos=" + str(pos) + " chgFlag=" + str(chgFlag) + " acc=" + str(acc))
			return False
		### Wenn Aenderungsmodus eingeschaltet (Parameter chg==True), 
		### die Aenderung waehrend dieses Laufes noch nicht angewendet wurde (chgFlag == False) und
		### die Aenderung dieser Position noch nicht versucht wurde 
		#print("==> START: pos=" + str(pos) + " chgFlag=" + str(chgFlag) + " acc=" + str(acc))
		if chg and not chgFlag  and prg[pos]['chg'] == False:				# => wenn chg gesetzt und diese Stelle noch nicht 
															#    geaendert wurde, dann nop- und jmp-Reaktion vertauschen
			#print("     ==> CHANGE - data before process : " + str(prg[pos]))
			chgFlag 		= True
			prg[pos]['chg'] = True
			prg[pos]['flg'] = True
			if   prg[pos]['cmd'] == "nop":
				pos += prg[pos]['val']										# Springe zu Position val
			elif prg[pos]['cmd'] == "jmp":
				pos += 1													# Tue nichts
			elif prg[pos]['cmd'] == "acc":
				acc += prg[pos]['val']
				pos += 1
			#print("     ==> CHANGE - data after process  : " + str(prg[pos]))

		else:
			#print("     ==> NORMAL - data before process : " + str(prg[pos]))
			prg[pos]['flg'] = True
			if   prg[pos]['cmd'] == "nop":
				pos += 1													# Tue nichts
			elif prg[pos]['cmd'] == "jmp":
				pos += prg[pos]['val']										# Springe zu Position val
			elif prg[pos]['cmd'] == "acc":
				acc += prg[pos]['val']
				pos += 1
			#print("     ==> NORMAL - data after process  : " + str(prg[pos]))



readInputFile()

runPrg()
print()
print("PART I  : Value of accumulator, before running code a second time    : " + str(acc))
print()

while not runPrg(True):
	True
print("PART II : Value of accumulator after the programm terminates regulary: " + str(acc))
print()
