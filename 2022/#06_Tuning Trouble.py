###################################################
### Advent of Code 2022
###
### Autor:    Kim Sieber
### Erstellt: 28.11.2023
###
### Tag 6: Tuning Trouble
###                  
####################################################

Datenstrom = open('#06 Input', 'r').read()

### Prüft, ob keine Dubletten in der Buchstabenfolge sind
###
### @param  Marker  = (str) Zeichenkette mit Buchstaben (meist 4)
### @return Antwort = (bool) true = alle Buchstaben kommen in Kette nur einmal vor
def checkEindeutigeBuchstaben(Marker):
    for i in range(len(Marker)):
        if Marker.count(Marker[i]) > 1:
            return False
    return True

### Ermittelt erste Position, in der nach vorne Variabel Anzahl an Zeichen eindeutig sind
###
### @param  Daten    = (str) Zeichenkette
### @param  Anzahl   = (int) Anzahl gewünschte Zeichen
### @return Position = (int) Position des "Start of message/packet Markers"
def ermittleStartOfMarker(Daten, Anzahl):
    for Position in range(Anzahl,len(Daten)):
        if checkEindeutigeBuchstaben(Daten[Position-Anzahl:Position]):
            return Position
    
############### PART I ###############################
print ('PART I : The first start-of-packet marker ist detected on character :', ermittleStartOfMarker(Datenstrom, 4) )    


############### PART II ##############################
print ('PART II: The first start-of-message marker ist detected on character:', ermittleStartOfMarker(Datenstrom, 14) )     



