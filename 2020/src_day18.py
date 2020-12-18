#################################################
##### AdventOfCode 2020
#####
##### Day 18 - Operation Order
#####
##### @author  Kim Sieber
##### @date    18.12.2020
###################################################
### Parameter
FILENAME = "input.txt"

### Formeln
### frms[0..n]['str']			  			= (str) eingelesene, uninterpretierte Formel
###           ['frm'][0..n] 				= (str) Zahl oder Operator ('*', '+') oder Klammer ('pnt')
###                  [0..n]['pnt'][0..n]	= (str) Zahl oder Operator ('*', '+') oder Klammer ('pnt')
###                               ...usw.	-> Kann beliebig weiter geschachtelt werden
###           ['frm2']...					= gleiche Struktur wie 'frm', aber modifizierte Aufbereitung
frms = []

### Liest Datei ein
### @fln 	:	(str) Dateiname
### @return	:	[{}]	Formeln, Struktur s.o. 
def readInputFile(fln):
	inputs = []
	inputFile = open(fln, "r")
	for line in inputFile:
		inputs.append({'str': line.strip()})
	inputFile.close()
	return inputs

### Bildet die Formelstruktur, indem Klammern in Unter-Dimensionen gesetzt werden
### @form 		: (str) eingelesene, uninterpretierte Formel
### @return		: {}	Formeln, Struktur s.o.
def buildFormula(form):
	rnt    = []
	string = ""
	cntPnt = 0
	for key, val in enumerate(list(form)):
		if isinstance(val, dict):
			string = buildFormula(val['pnt'])
		if val == " " and len(string)>0 and cntPnt == 0:
			rnt.append(string.strip())
			string = ""
		elif val == "(":
			cntPnt += 1
			if cntPnt > 1:
				string += val
		elif val == ")":
			cntPnt -= 1
			if cntPnt == 0:
				rnt.append({'pnt': buildFormula(string)})
				string = ""
			if cntPnt > 0:
				string += val
		else:
			string += val
	if len(string) > 0:
		rnt.append(string.strip())
	return rnt

### Formel berechnen
### @frm 					: 	{}	Formeln, Struktur s.o.
### @flag_addition_first	: (bool) init:False, bei True werden Additionen zuerst gerechnet
### @return					:	(int) Ergebnis der Berechnung
def calcFormula(frm, flag_addition_first=False):
	### erst alle enthaltenen Klammern ausrechnen und Wert setzen
	frm_without_pnt = []
	for val in frm:
		if isinstance(val, dict):
			val = calcFormula(val['pnt'],flag_addition_first)
		frm_without_pnt.append(val)

	### dann alle +-Zeichen berechnen
	if flag_addition_first:
		frm_final = []
		val_before      = 0
		flag_val_before = False
		flag_add        = False
		for val in frm_without_pnt:
			if val.isdigit():
				if flag_val_before == False:
					val_before = int(val)
					flag_val_before = True
				else:
					if flag_add:
						val_before += int(val)
					else:
						frm_final.append(str(val_before))
						val_before = int(val)
			else:
				if val == "+":
					flag_add = True
				elif val == "*":
					flag_add = False
					frm_final.append(str(val_before))
					frm_final.append("*")
					flag_val_before = False
		frm_final.append(str(val_before))
	else:
		frm_final = frm_without_pnt

	### Rechnung durchfueren
	res = 0
	rem = "+"
	for val in frm_final:
		if val.strip() in ("*", "+"):
			rem = val
		else:
			if rem == "*":
				res *= int(val)
			elif rem == "+":
				res += int(val)
	return str(res)


frms = readInputFile(FILENAME)
for k, f in enumerate(frms):
	frms[k]['frm'] = buildFormula(frms[k]['str'])

res = 0
for frm in frms:
	res += int(calcFormula(frm['frm']))
print()
print("PART I  : The sum of the resulting values is                   : ", res)

resNew = 0
for frm in frms:
	resNew += int(calcFormula(frm['frm'],True))
print()
print("PART II : The sum of the resulting values with the new rules is: ", resNew)
print()

