##################################################
### Advent of Code 2023
###
### Autor:    Kim Sieber
### Erstellt: 04.12.2023
###
### Tag 04: Scratchcards
###
####################################################

### Gewinnfolge (1 für erste Gewinnzahl, danach jeweils verdoppelung (Liste ist im Code einfacher zu handeln als Protenzrechnung
WinningScore = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024
                ]
### Einlesen der Daten
###   SquareCards[0..n][0][0..n] = (int) Liste Gewinnzahlen
###                    [1][0..n] = (int) Liste eigene Zahlen
### Einlesen und bis Zahlenblöcke formatieren
SquareCards =  [y[1].split('|') for y in [x.split(':') for x in open('#04 Input', 'r').read().split('\n')]]
### Jede Karte nachbearbeiten
for i in range(len(SquareCards)):
    ### Gewinnzahlen und eigene Zahlen
    for j in range(2):
        SquareCards[i][j] = SquareCards[i][j].strip()                                                           # Leerzeichen an Enden entfernen
        SquareCards[i][j] = SquareCards[i][j].replace('  ', ' ')                                                # Doppelte Leerzeichen entfernen
        SquareCards[i][j] = [int(a) for a in SquareCards[i][j].strip().split(' ')]          # Umwandeln in Integer-Liste


### Ermittlung Punktezahl
###
### @param  WinCards[0..n] = (int) Liste Gewinnzahlen
### @param  MyCards[0..n]  = (int) Liste meiner Zahlen
### @return AnzahlTreffer  = (int) Anzahl passender Karten
###         Score          = (int) Gewinn-Punkte
def getScore(WinCards, MyCards):
    AnzahlTreffer = 0
    for MC in MyCards:
        if MC in WinCards:
            AnzahlTreffer += 1
    return AnzahlTreffer, WinningScore[AnzahlTreffer]


### Instanzzähler anlegen (für PART II)
###    Instances[0..n]  = (int) Zähler, initial 1, kann erhöht werden
Instances = [1 for n in range(len(SquareCards))]

### Schleife über alle Karten und Punktzahlen addieren
Score = 0
for CardID in range(len(SquareCards)):
    AnzahlTreffer, thisScore  = getScore(SquareCards[CardID][0], SquareCards[CardID][1])
    Score                    += thisScore
    ### Abhängig der Anzahl gewonnener Nummern (Treffer), die Anzahl nachfolgender Karten um je 1 erhöhen
    for Copy in range(1,AnzahlTreffer+1):
        ### Das ganze x-Mal ausführen, soviele Karten vorhanden sind.
        for InstanceID in range(Instances[CardID]):
            Instances[CardID+Copy] += 1
    
############### PART I  ##############################
print ('PART I : The total sum of points is       :', Score )    
    
############### PART II ##############################
print ('PART I : The number of total scratchcards :', sum(Instances) )    
    
    
