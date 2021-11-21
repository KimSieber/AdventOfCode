################################################
### Advent of Code 2019
###
### Tag 16 - Fehlerhafte Frequenzübertragung
###
### Autor:    Kim Sieber
### Erstellt: 22.11.2021
### 
### Zur Lösung Part II Hilfe benötigt für Lösungsweg:
### https://work.njae.me.uk/2019/12/20/advent-of-code-2019-day-16/
################################################
from collections import deque

INPUT_FILENAME = "#16 Input"
PATTERN_BASE   = [0,1,0,-1]

### Datei einlesen und Ziffern als Array zurückgeben
def readInput(file_name):
    input_file = open(file_name, "r")
    input_str = list(input_file.read())
    input_int = [int(i) for i in input_str]
    input_file.close()
    return input_int

### Multipliziert die Signal-Ziffern mit der vorgegebenen Pattern-Liste
### (Pattern-Liste ist abhängig Zeile/Runde angepasst zu übergeben)
def runLine(signal, pattern):
    result = 0
    for pos in range(len(signal)):
        pattern.rotate(-1)
        result += signal[pos] * pattern[0]
    return abs(result)%10

### Durchläuft eine Phase und gibt das Ergebnis dieser Phase zurück
def runPhase(signal, pattern_base):
    signal_new = [0 for _ in signal]
    for pos in range(len(signal)):
        pattern = deque([p for p in pattern_base for _ in range(pos+1)])
        signal_new[pos] = runLine(signal, pattern)
    return signal_new



### PART I
signal = readInput(INPUT_FILENAME)

for phase in range(100):
    signal = runPhase(signal, PATTERN_BASE)

print ("Puzzle answer PART I:  ", "".join(str(s) for s in signal[:8]))


### PART II
signal = readInput(INPUT_FILENAME)
offset = int("".join(str(s) for s in signal[:7]))
signal = [int(s) for _ in range(10000) for s in signal][offset:]
for phase in range(100):
#    signal = runPhase(signal, PATTERN_BASE)            #--> Laufzeit zu lang / unendlich
    ### Nachstehende Lösung aus Netz geholt, Erklärung siehe Link oben
    for i in range(-2, -len(signal)-1, -1):
            signal[i] = (signal[i] + signal[i+1]) % 10

print ("Puzzle answer PART II: ", "".join(str(s) for s in signal[:8]))












