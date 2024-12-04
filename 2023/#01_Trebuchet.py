###################################################
### Advent of Code 2023
###
### Autor:    Kim Sieber
### Erstellt: 01.12.2023
###
### Tag 01: Trebuchet
###
####################################################

### Daten einlesen in Liste [][] und zweite Spalte als Integer umwandeln
Data = open('#01 Input', 'r').read().split('\n')

### Ermittelt Kalibrations-Wert (aus erste und letzte Ziffern eines Strings)
###
### @param  Eingabe         = (str) Zeichenkette mit mind. einer Ziffer (da diese von vorne und hinten die erste und letzte ist
### @return CalibrationVal  = (int) 2-stellige Zahl
def getCalibrationValue(CalibrationLine):
    ListOfDigit = [int(c) for c in CalibrationLine if c.isdigit()]      # Liste aller Zahlen im String erzeugen
    return (ListOfDigit[0]*10) + ListOfDigit.pop()                      # Erste Ziffer (*10) und zweite Ziffer zu 2-stelliger Zahl zusammenfügen

### Schleife über alle Calibration-Zeilen
SumCalibrationValues = 0
for i in range(len(Data)):
    SumCalibrationValues += getCalibrationValue(Data[i])

############### PART I  ##############################
print ('PART I : The sum of all the calibration values is :', SumCalibrationValues )    


### Ermittelt Kalibrations-Wert (aus erste und letzte Ziffern eines Strings, wandelt dabei aber Text in Ziffern um)
###
### @param  Eingabe         = (str) Zeichenkette mit Zahlen, als Ziffern und/oder geschriebener Zahl (engl.)
### @return CalibrationVal  = (int) 2-stellige Zahl
def getCalibrationValue2(CalibrationLine):
    ListOfDigit      = []                       # Liste aller Zahlen erzeugen, mit Ziffern, auch aus Text
    CalibrationLine += '     '                  # Verlängern um 5 Stellen, damit bis Ende auch nach zB "eight" gesucht werden kann
    for i in range(len(CalibrationLine)-5):
        if CalibrationLine[i].isdigit():
            ListOfDigit.append(int(CalibrationLine[i]))
        if CalibrationLine[i:i+3] == 'one':
            ListOfDigit.append(1)
        if CalibrationLine[i:i+3] == 'two':
            ListOfDigit.append(2)
        if CalibrationLine[i:i+5] == 'three':
            ListOfDigit.append(3)
        if CalibrationLine[i:i+4] == 'four':
            ListOfDigit.append(4)
        if CalibrationLine[i:i+4] == 'five':
            ListOfDigit.append(5)
        if CalibrationLine[i:i+3] == 'six':
            ListOfDigit.append(6)
        if CalibrationLine[i:i+5] == 'seven':
            ListOfDigit.append(7)
        if CalibrationLine[i:i+5] == 'eight':
            ListOfDigit.append(8)
        if CalibrationLine[i:i+4] == 'nine':
            ListOfDigit.append(9)
    return (ListOfDigit[0]*10) + ListOfDigit.pop()    

### Daten einlesen in Liste [][] und zweite Spalte als Integer umwandeln
#Data = open('#01 Input Test 2', 'r').read().split('\n')

### Schleife über alle Eingabezeilen

### Schleife über alle Calibration-Zeilen
SumCalibrationValues = 0
for i in range(len(Data)):
    SumCalibrationValues += getCalibrationValue2(Data[i])

############### PART I  ##############################
print ('PART II: The sum of all the calibration values is :', SumCalibrationValues )    

