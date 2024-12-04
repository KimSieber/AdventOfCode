###################################################
### Advent of Code 2022
###
### Autor:    Kim Sieber
### Erstellt: 30.11.2023
###
### Tag 8: Treetop Tree House
###
####################################################

### Puzzle einlesen in Array-Matrix
###   Grid[0..n][0..n] = Baumhöhe   0..9
Grid = [[n[i] for i in range(len(n))] for n in open('#08 Input', 'r').read().split('\n')]

############### PART I ###############################
### Prüft, ob Baum zum Rand sichtbar ist
###
### @param  Grid     = [[(int)]] Baum-Matrix
### @param  x        =  (int) Zeile des zu prüfenden Baumes (0..n)
### @param  y        =  (int) Spalte des zu prüfenden Baumes (0..n)
### @return sichtbar = (bool) true/false, ob vom Rand sichtbar
def pruefeSichtbarkeit(Grid, x, y):
    ### Höhe des zu prüfenden Baumes
    Hoehe = Grid[x][y]
    ### Initial - Baum am Rand ist immer sichbar
    if x == 0 or y == 0 or x == (len(Grid)-1) or y == (len(Grid[0])-1):
        return True
    ### nach oben prüfen
    for i in range (x-1,-1,-1):
        if Grid[i][y] >= Hoehe:
            break
    else:
        return True
    ### nach links prüfen
    for i in range (y-1,-1,-1):
        if Grid[x][i] >= Hoehe:
            break
    else:
        return True
    ### nach unten prüfen
    for i in range (x+1,len(Grid)):
        if Grid[i][y] >= Hoehe:
            break
    else:
        return True    
    ### nach rechts prüfen
    for i in range (y+1,len(Grid[x])):
        if Grid[x][i] >= Hoehe:
            break
    else:
        return True
    
    return False

### Bäume zählen, die vom Rand nicht sichtbar sind
Anzahl = 0
for x in range (len(Grid)):
    for y in range (len(Grid[x])):
        if pruefeSichtbarkeit(Grid, x, y):
            Anzahl += 1            
           
print ('PART I : Count of trees, that are visible from the edge :', Anzahl )    




############### PART II ##############################
### Ermittelt die multiplizierte Anzahl sichbarer Bäume je Koordinatoe 
###
### @param  Grid   = [[(int)]] Baum-Matrix
### @param  x      =  (int) Zeile des zu prüfenden Baumes (0..n)
### @param  y      =  (int) Spalte des zu prüfenden Baumes (0..n)
### @return Anzahl = (int) Anzahl sichbarer Bäume (2..n)    -> jeder Baum kann mind. seinen Nachbarn sehen, also mind. 4 -> außer in den Ecken, dort 2
def ermittleSichtbareBaeume(Grid, x, y):
    #print ('+-> Grid[',x,'][',y,'] =', Grid[x][y])
    ### Höhe des zu prüfenden Baumes
    Hoehe   = Grid[x][y]
    Produkt = 0
    Anzahl  = 0
    ### nach oben Zählen
    for i in range (x-1,-1,-1):
        Anzahl += 1
        if Grid[i][y] >= Hoehe:
            break
    Produkt = Anzahl
    Anzahl  = 0
    ### nach links prüfen
    for i in range (y-1,-1,-1):
        Anzahl += 1
        if Grid[x][i] >= Hoehe:
            break
    Produkt *= Anzahl
    Anzahl   = 0
    ### nach unten prüfen
    for i in range (x+1,len(Grid)):
        Anzahl += 1
        if Grid[i][y] >= Hoehe:
            break
    Produkt *= Anzahl
    Anzahl   = 0
    ### nach rechts prüfen
    for i in range (y+1,len(Grid[x])):
        Anzahl += 1
        if Grid[x][i] >= Hoehe:
            break
    Produkt *= Anzahl
    
    return Produkt


### Bäume zählen, die vom Rand nicht sichtbar sind
Produkt = []
for x in range (len(Grid)):
    for y in range (len(Grid[x])):
        Produkt.append(ermittleSichtbareBaeume(Grid, x, y))
           
print ('PART II: The highest scenic score of the grid is        :', max(Produkt) )    






