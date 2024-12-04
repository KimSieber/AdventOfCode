##################################################
### Advent of Code 2023
###
### Autor:    Kim Sieber
### Erstellt: 02.12.2023
###
### Tag 02: Cube Conundrum
###
####################################################

### Einlesen der Daten
###   InputGames = [0..n][0] = (str) Spielnummer mit Bezeichnung, bspw. "Game 1"
###                      [1] = (str)
InputGames =  [y.split(';') for y in [x.split(':')[1] for x in open('#02 Input', 'r').read().split('\n')]]

#print (InputGames)

### Umformatierung der gelesenen daten
###   Games[0..n][0..n][0] = (int) Anzahl rote Würfel
###                    [1] = (int) Anzahl grüne Würfel
###                    [2] = (int) Anzahl blaue Würfel
###         +--------------> Spiel-ID
###               x--------> Ziehungen - Subsets
###                     x--> Farb-Code
Games = []
for InputGame in InputGames:                                            #-> [' 3 blue, 4 red', ' 1 red, 2 green, 6 blue', ' 2 green']
    GameOut = []
    for Subsets in InputGame:                                           #-> 3 blue, 4 red
        Subset    = Subsets.split(',')                                  #-> SubSet = ['3 blue','4 red']
        SubsetOut = [0,0,0]                                             #-> Initialisierung Ausgabe = [0,0,0] 
        for Cubes in Subset:                                            #-> 3 blue
            Cube = [x.strip() for x in Cubes.strip().split(' ')]
            if Cube[1].strip() == 'red':        SubsetOut[0] += int(Cube[0])
            if Cube[1].strip() == 'green':      SubsetOut[1] += int(Cube[0])
            if Cube[1].strip() == 'blue':       SubsetOut[2] += int(Cube[0])
                
        GameOut.append(SubsetOut)
    Games.append(GameOut)

#print (Games)

### Prüft die Subsets im Spiel, ob alle möglich wären
###
### @param  Game[0..n][0..2] = (int) Anzahl Würfel je Farbe
### @return possible         = (bool) true/false
def checkGame(Game):
    for Subset in Game:
        if Subset[0] > 12 or \
           Subset[1] > 13 or \
           Subset[2] > 14      :
            return False
    return True    
       
    
    
############### PART I  ##############################
### Ermittlung der IDs der Spiele, die aus 12=red, 13=green, 14=blue Würfel bestehen können
PossibleGameIDs = []
for i in range(len(Games)):
    if checkGame(Games[i]):
        PossibleGameIDs.append(i+1)         # +1, da Gameliste mit 1 beginnt, Python-Liste aber mit 0
### Summe der gefundenen ID's    
SumGameID = sum(PossibleGameIDs)
        
print ('PART I : The sum of the IDs of the possible games is :', SumGameID )    

### Ermittelt die Mindest-Anzahl an Würfeln je Spiel und Multipliziert diese
###
### @param  Game[0..n][0..2] = (int) Anzahl Würfel je Farbe
### @return product          = (int) Ergebnis = Multipliziere Mindest-Zahlen
def multiplyMinimumCubesInGame(Game):
    MinimumCubes = [0,0,0]
    for Subset in Game:
        if Subset[0] > MinimumCubes[0]:  MinimumCubes[0] = Subset[0]
        if Subset[1] > MinimumCubes[1]:  MinimumCubes[1] = Subset[1]
        if Subset[2] > MinimumCubes[2]:  MinimumCubes[2] = Subset[2]
        
    return MinimumCubes[0] * MinimumCubes[1] * MinimumCubes[2]

############### PART I  ##############################
### Addition aller Ergebnisse der Muliplikation der Mindest-Würfel-Anzahlen
SumOfPower = 0
for Game in Games:
    SumOfPower += multiplyMinimumCubesInGame(Game)


print ('PART II: The sum of the power fo these sets is       :', SumOfPower )    




