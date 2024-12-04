##################################################
### Advent of Code 2023
###
### Autor:    Kim Sieber
### Erstellt: 03.12.2023
###
### Tag 03: Gear Ratios
###
####################################################

### Einlesen der Daten
###   EngineSchematic[0..n] = (str) Zeichen und Zahlenkette, bspw: '.....+.58.'
EngineSchematic =  open('#03 Input', 'r').read().split('\n')


### Prüft, ob Zeichen ein Symbol ist (als weder '.' noch Ziffer
###
### @param  C  = (str)  1-stelliger String
### @return R  = (bool) true = wenn Zeichen ein Symbol ist, sonst false
def isSymbol(C):
    if C.isdigit(): return False
    if C == '.'   : return False
    return True

### Gibt eine Liste aller Zahlen zurück, die direkt oder diagonal an der angegeben Koordinate stehen
###
### @param  EngineSchematic[0..n] = (str) Zeichen und Zahlenkette, bspw: '.....+.58.'
### @param  x                     = (int) Zeilen-Nr.
### @param  y                     = (int) Spalten-Nr.
### @return Nums[0..n]            = (int) Liste mit Zahlen, kann auch kein Eintrag enthalten !
def findNumbers(EngineSchematic, x, y):
    Nums = []
    ### Ermittelt komplette Nummer in der Zeile (nur aufrufen, wenn besagte Stelle eine Ziffer ist)
    def getNumber(xi, yi):
        Num = ''
        ### vorwärts suchen
        for i in range(yi,len(EngineSchematic[xi])):
            if EngineSchematic[xi][i].isdigit():        Num = Num + EngineSchematic[xi][i]
            else:                                       break
        ### rückwärts suchen
        for i in range(yi-1, -1, -1):
            if EngineSchematic[xi][i].isdigit():        Num = EngineSchematic[xi][i] + Num
            else:                                       break
        return int(Num)
    
    ### Einmal um die Koordinate herum Ziffern prüfen
    if EngineSchematic[x][y-1].isdigit(): 
        Nums.append(getNumber(x, y-1))
    if EngineSchematic[x][y+1].isdigit(): 
        Nums.append(getNumber(x, y+1))
    if EngineSchematic[x-1][y].isdigit(): 
        Nums.append(getNumber(x-1, y))
    else:                                               # wenn direkt drüber keine Ziffern, dann schräg suchen, sonst nicht, da schräg dann zur Ziffer drüber gehört
        if EngineSchematic[x-1][y-1].isdigit(): 
            Nums.append(getNumber(x-1, y-1))
        if EngineSchematic[x-1][y+1].isdigit(): 
            Nums.append(getNumber(x-1, y+1))
    if EngineSchematic[x+1][y].isdigit(): 
        Nums.append(getNumber(x+1, y))
    else:                                               # wenn direkt drunter keine Ziffern, dann schräg suchen, sonst nicht, da schräg dann zur Ziffer drunter gehört
        if EngineSchematic[x+1][y-1].isdigit(): 
            Nums.append(getNumber(x+1, y-1))
        if EngineSchematic[x+1][y+1].isdigit(): 
            Nums.append(getNumber(x+1, y+1))
    
    return Nums 


### Durchsuche alle Zeilen und Zeichen nach Symbolen
SumNums = 0
for x in range(len(EngineSchematic)):
    for y in range(len(EngineSchematic[x])):
        ### Wenn Symbol, dann Zahlen drum herum suchen und addieren
        if isSymbol(EngineSchematic[x][y]):
            SumNums += sum(findNumbers(EngineSchematic, x, y))
  
############### PART I  ##############################
print ('PART I : The sum of the part numbers in the engine schematic is          :', SumNums )    

            
### Durchsuche alle Zielen und Zeilen nach dem Symbol '*'
SumPrdNums = 0
for x in range(len(EngineSchematic)):
    for y in range(len(EngineSchematic[x])):
        ### Wenn Stelle = Symbol '*', dann Zahlen drum herum suchen
        if EngineSchematic[x][y] == '*':
            Nums = findNumbers(EngineSchematic, x, y)
            ### Wenn genau zwei Zahlen gefunden werden, dies Muliplizieren und zur Gesamtsumme addieren
            if len(Nums) == 2:
                SumPrdNums += (Nums[0] * Nums[1])
            
############### PART II ##############################
print ('PART II: The sum of all of the gear ratios in your enginge schhematic is :', SumPrdNums )    
            
            
            