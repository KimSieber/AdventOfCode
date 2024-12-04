###################################################
### Advent of Code 2022
###
### Autor:    Kim Sieber
### Erstellt: 01.12.2023
###
### Tag 9: Rope Bridge
###
####################################################

### Daten einlesen in Liste [][] und zweite Spalte als Integer umwandeln
Data = [n.split(' ') for n in open('#09 Input', 'r').read().split('\n')]
for i in range(len(Data)):
    Data[i][1] = int(Data[i][1])

#print (Data)


### Ermittlung der Grid-Größe
###
### @param  Data = [[(str),(int)], ...] Bewegungsdaten
### @return x    = (int) Feldbreite
### @return y    = (int) Feldlänge
### @return posx    = (int) Start-Position X
### @return posy    = (int) Start-Position Y
def ermittleGridGroesse(Data):
    maxR = maxL = maxU = maxD = 0
    posX = posY = 0
    for move in Data:
        if move[0] == 'R':
            posX += move[1]
            if posX > maxR: maxR = posX
        if move[0] == 'L':
            posX -= move[1]
            if posX < maxL: maxL = posX
            
        if move[0] == 'D':
            posY += move[1]
            if posY > maxD: maxD = posY
        if move[0] == 'U':
            posY -= move[1]
            if posY < maxU: maxU= posX
            
    x    = abs(maxR) + abs(maxL) + 1    # +1, weil Start-Position/Feld mit eingerechnet werden muss
    y    = abs(maxD) + abs(maxU) + 1
    posx = maxL                      
    posy = maxU
    
    x    = 1000
    y    = 1000
    posx = 500                      
    posy = 500

    return x,y,posx,posy
    
### Andruck Spielfeld zur Kontrolle
def druckeFeld(Grid):
    print ()
    print ()
    for i in range(len(Grid)):
        row = ''
        for j in range(len(Grid[i])):
            row += Grid[i][j]
        print (row)
    print ()
    
### Bewegung durchführen und H-versetzen, T-nachziehen und alte Position T mit # belegen
###
### Globale Variable Grid verwenden
### @param  Befehl   = [(str), (int)] Bewegungsrichtung (L,R,D,U) und Anzahl
def bewegenH(Befehl):
    ### Schleife für die Anzahl der Bewegungen in angegebener Richtung
    for m in range(Befehl[1]):
        ### Alte Position von H & T löschen
        Grid[PosH["y"]][PosH["x"]] = '.'
        Grid[PosT["y"]][PosT["x"]] = '.'
        ################################# 
        ### Bewegung H berechnen  
        if Befehl[0] == 'R':
            PosH['x'] += 1 
        if Befehl[0] == 'L':
            PosH['x'] -= 1 
        if Befehl[0] == 'D':
            PosH['y'] += 1 
        if Befehl[0] == 'U':
            PosH['y'] -= 1 
        ################################# 
        ### Wenn zwei X entfernt, dann einen nachziehen und auf gleiche Achse setzen
        if (PosH['x']-PosT['x']) >= 2:
            PosT['x'] = PosH['x'] - 1
            PosT['y'] = PosH['y']
        if (PosH['x']-PosT['x']) <= -2:
            PosT['x'] = PosT['x'] - 1
            PosT['y'] = PosH['y']
        ### Wenn zwei Y entfernt, dann einen nachziehen und auf gleiche Achse setzen
        if (PosH['y']-PosT['y']) >= 2:
            PosT['y'] = PosH['y'] - 1
            PosT['x'] = PosH['x']
        if (PosH['y']-PosT['y']) <= -2:
            PosT['y'] = PosH['y'] + 1
            PosT['x'] = PosH['x']
        ################################# 
        ### Neue Positionen setzen
        Grid[PosH['y']][PosH['x']] = 'H'
        if PosH['y'] != PosT['y']  or  PosH['x'] != PosT['x']:
            Grid[PosT['y']][PosT['x']] = 'T'
        GridMarker[PosT['y']][PosT['x']] = '#'
        ### Bewegung T berechnen
#        print ('   PosH=',PosH["y"],PosH["x"], '  PosT=',PosT["y"],PosT["x"] )
#        druckeFeld(Grid)
    


### Größe des Feldes und Start-Position ermitteln    
x,y,posx,posy = ermittleGridGroesse(Data)
### Erstellung Feld und Markierung Start-Position
Grid       = [['.' for i in range(x)] for j in range(y)]      ### Spielfläche
GridMarker = [['.' for i in range(x)] for j in range(y)]      ### Markiert, wo überall T schon war
PosH       = {'y': posy, 'x': posx}
PosT       = {'y': posy, 'x': posx}
PosS       = {'y': posy, 'x': posx}

Grid[PosH["y"]][PosH["x"]] = 'H'   

#druckeFeld(Grid)
### Schleife über alle Bewegungen
for b in Data:
#    print('b = ',b)
    bewegenH(b)
    #druckeFeld(Grid)

#### Ergebnis-Felder ausgeben
#druckeFeld(Grid)
#druckeFeld(GridMarker)

### Ermittle Anzahl Positionen, an denen T war
NoPosOfT = sum([l.count('#') for l in GridMarker])

############### PART I  ##############################
print ('PART I : The tail of the rope visit so many positions  :', NoPosOfT )    




















    
    