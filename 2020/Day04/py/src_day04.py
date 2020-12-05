###################################################
##### AdventOfCode 2020
#####
##### Day 04 - Passport Prozessing
#####
##### @author  Kim Sieber
##### @date    04.12.2020
###################################################
### Parameter
FILENAME = "input.txt"

### Passwort-Liste
### Format:    Passport[0..n]["byr".."cid"] = value
passports = {}

### Anzahl gueltige Passports nach Regeln Part I und Part II
numberValidPassportsPartI  = 0
numberValidPassportsPartII = 0

### Liest Datei zeilenweise ein und gibt Liste von Zeilen zurueck
### @fileName:      Dateiname der Input-Datei im gleichen Verzeichnis
### @return  :      lines[]
def readInputFile():
	inputFile = open(FILENAME, "r")
	i = 0
	inputs = {}
	for line in inputFile:
		if not line.strip():				# Next Passport
			passports[i] = inputs 
			inputs = {}
			i += 1
		else:								# New Line in same Passport
			args = line.strip().split(" ")
			for arg in args:
				key, value = arg.split(":")
				inputs[key] = value
	passports[i] = inputs 
	inputFile.close()

### Anzahl gueltige Paesse ermitteln
### und setzt diese in die globalen Variablen
def countValidPassports():
	global numberValidPassportsPartI
	global numberValidPassportsPartII
	for i in range(0,len(passports)):
		keys = passports[i].keys()
		### PART I: Validation only counting keys
		if ("cid"     in keys and len(keys) == 8) or \
		   ("cid" not in keys and len(keys) == 7)      :
		    numberValidPassportsPartI += 1

		    ### Part II: More Validation
		    if int(passports[i]["byr"]) >= 1920 and  \
		       int(passports[i]["byr"]) <= 2002        :

				if int(passports[i]["iyr"]) >= 2010 and  \
			       int(passports[i]["iyr"]) <= 2020        :

					if int(passports[i]["eyr"]) >= 2020 and  \
				       int(passports[i]["eyr"]) <= 2030        :

						if (passports[i]["hgt"][len(passports[i]["hgt"])-2:] == "in"  and        \
				       		int(passports[i]["hgt"][:-2]) >= 59                       and        \
				       		int(passports[i]["hgt"][:-2]) <= 76                            ) or  \
				       	   (passports[i]["hgt"][len(passports[i]["hgt"])-2:] == "cm"  and        \
				       		int(passports[i]["hgt"][:-2]) >= 150                      and        \
				       		int(passports[i]["hgt"][:-2]) <= 193                           ):

							if passports[i]["hcl"][:1] == "#"                          and  \
				       	       (x for x in passports[i]["hcl"] if x in (0-9,"a"-"f"))          :

								if passports[i]["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):

									if (x for x in passports[i]["pid"] if x in (0-9))  and  \
				       	        	   (len(passports[i]["pid"]) == 9):
										numberValidPassportsPartII += 1


readInputFile()
countValidPassports()

print "Part I : Number of valid passports: " + str(numberValidPassportsPartI)
print "Part II: Number of valid passports: " + str(numberValidPassportsPartII)
