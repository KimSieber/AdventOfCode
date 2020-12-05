###################################################
##### AdventOfCode 2020
#####
##### Day 05 - Binary Boarding
#####
##### @author  Kim Sieber
##### @date    05.12.2020
###################################################
### Parameter
FILENAME = "input.txt"


### Liest Datei zeilenweise ein und gibt Liste von Zeilen zurueck
### @return  :      boardingPasses[0..n]['bsp'] = Binary space partitioning, e.g. FBFBBFFRLR
###                                     ['row'] = Sitzreihe ermittelt
###                                     ['col'] = Sitzspalte ermittelt
###                                     ['sid'] = Seat-ID
def readInputFile():
	inputFile = open(FILENAME, "r")
	boardingPasses = {}	
	i = 0
	for line in inputFile:
		Pass = {}
		Pass['bsp'] = line.strip()
		Pass['row'] = getSeat(Pass['bsp'][0:7], 0, 127)
		Pass['col'] = getSeat(Pass['bsp'][7:] , 0,   8)
		Pass['sid'] = (Pass['row'] * 8) + Pass['col']
		boardingPasses[i] = Pass
		i += 1
	inputFile.close()
	return boardingPasses

### Ermittelt Sitz-Reihe oder Sitz-Spalte nach Halbierungsprinzip
### @bsp     : (str) Halbierungsfolge, bei Reihen bspw: FBFBBFF, bei Spalten bspw. RLR
### @fr      : (int) Bereich VON, i.d.R. = 0
### @to      : (int) Bereich BIS, bei Reihen = 127, bei Spalten = 7
### @return  : (int) Sitzplatz
def getSeat(bsp, fr, to):
	for spec in list(bsp):
		if spec in ("B", "R"):
			fr = fr + ((to+1-fr)/2)
		else:    										# == "F" or "L"
			to = to - ((to+1-fr)/2)
	return fr


passes = readInputFile()
seats = []
sidMax = 0
for key in passes.keys():
	### PART I
	if passes[key]["sid"] > sidMax:
		sidMax = passes[key]["sid"]
	### PART II
	seats.append(passes[key]["sid"])

print
print "PART I : Highest sead ID on the boarding passes: " + str(sidMax)

### PART II
seats.sort()
sidBefore = sidEmpty = 0
for sid in seats:
	if sidBefore == 0: 
		sidBefore = sid
	else:
		if sidBefore+1 < sid:
			sidEmpty = sidBefore+1
			break
		else:
			sidBefore = sid

print
print "PART II: ID of your seat                       : " + str(sidEmpty)







