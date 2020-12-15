################################################
##### AdventOfCode 2020
#####
##### Day 14 - Docking Data
#####
##### @author  Kim Sieber
##### @date    14.12.2020
###################################################
### Parameter
FILENAME = "input.txt"

### Programm
### prg[0..n]['mask']				= (str) Binaerer Maskierungs-Satz mit 0,1,X
###          ['mem' ][0..n]['key']	= (int) Liste von Keys unter mem
###                        ['val']	= (int) Liste von Werten zu mem
prg = []

### Speicher
### mem[adress] = Wert decimal dieser Adresse
###     +-------- AdressPosition, bspw. 7 oder 8
mem1 = {}
mem2 = {}

### Liest Datei ein
### Erste Zeile enthaelt aktuelle Zeit in Min ab 0
### Zweite Zeile enthaelt Liste mit x und Bus-Nummern
def readInputFile():
	global prg
	prgPart = {}
	mem     = []
	inputFile = open(FILENAME, "r")
	for line in inputFile:
		### Wenn mask, dann alten Satz sichern und neuen beginnen
		line = line.strip()
		if line[0:4] == "mask":
			if len(prgPart) > 0:
				prgPart['mem'] = mem
				mem = []
				prg.append(prgPart)
				prgPart = {}
			prgPart['mask'] = line[7:]
		elif line[0:3] == "mem":
			mem.append({'key': int(line[4:line.find("]")]), \
						'val': int(line[line.find("=")+1:])     })
		else:
			print("ERROR: readInputFile() line=", line)
			exit()
	prgPart['mem'] = mem 
	prg.append(prgPart)
	inputFile.close()

### Wandelt Wert binaer um und wendet Maske an
### @mask 	:	(str) Maskierung, 36-bit, bspw. XXXXXXXX0XXXX10XXXXX01...
### @val	:	(int) Dezimal-Wert Eingabe
### @return	:	(int) Dezimal-Wert Ausgabe
def applyBitMask(mask, val):
	valNegFlag = False
	if val < 0: 
		valNegFlag = True
		val *= -1
	Bin = "%036d"%int(bin(val)[2:])
	for key, mas in enumerate(list(mask)):
		if mas != "X":
			Bin = Bin[:key] + mas + Bin[key+1:]
	ret = eval("0b"+str(int(Bin)))
	if valNegFlag:
		ret *= -1
	return ret

### Gibt Liste der moeglichen Adressen zurueck
### @mask 	:	(str) Maskierung, 36-bit, bspw. XXXXXXXX0XXXX10XXXXX01...
### @key	:	(int) Dezimal-Wert Key
### @return	:	(int[]) Liste Keys
def getListMem(mask, key):
	ret = []
	### Neue Maske bilden
	Bin = "%036d"%int(bin(key)[2:])
	for key, mas in enumerate(list(mask)):
		if mas != "X":
			if mas == "0" and Bin[key:key+1] == "1":
					mask = mask[:key] + "1" + mask[key+1:]
	### Loop fuer die Anzahl der Optionen, die abhaengig der Anzahl der X in mask sind
	xcnt = mask.count("X")
	for i in range(0,(2**xcnt)):
		### X-Belegung erzeugen
		xset = str("%036d"%int(bin(i)[2:]))
		xset = xset[len(xset)-xcnt:]
		### Loop für die Anzahl der X
		maskcopy = mask[:]
		for x in list(xset):
			xpos = maskcopy.index("X")
			maskcopy = maskcopy[:xpos] + x + maskcopy[xpos+1:]
		ret.append(eval("0b"+str(int(maskcopy))))
		maskcopy = mask[:]
	return ret


readInputFile()
#print(prg)

for p in prg:
	for m in p['mem']:
		val = applyBitMask(p['mask'], m['val'])
		mem1[m['key']] = val
		keys = getListMem(p['mask'], m['key'])
		for k in keys:
			mem2[k] = m['val']

#print (mem1)
#print (mem2)
sumVal1 = sumVal2 = 0
for key in mem1:
	sumVal1 += mem1[key]
for key in mem2:
	sumVal2 += mem2[key]

print()
print("PART I  : Sum of all values left in memory : ",sumVal1)
print()

print()
print("PART II : Sum of all values left in memory : ",sumVal2)
print()

