################################################
### Advent of Code 2021
###
### Tag 06 - Laternfish
###
### Autor:    Kim Sieber
### Erstellt: 06.12.2021
################################################

INPUT_FILENAME = "#06 Input" # Test 1"

### Datei einlesen in Liste
### @return: fishes_per_timer[0..8] = Anzahl Fishe mit diesem Counter/Days
def readInput(file_name):
    input_file  = open(file_name, "r")
    fishes = [int(f) for f in input_file.readline().split(',')]
    fishes_per_timer = [0 for _ in range(9)]
    for fish in fishes:
        fishes_per_timer[fish] += 1        
    return fishes_per_timer

### Verarbeitet einen Tag (Anzahl Fishe an diesem Tag einen Tag heruntersetzen)
def processCycle(fishes_per_timer):
    output = [0 for _ in range(9)]
    for i in fishes_per_timer:
        output[0] = fishes_per_timer[1]
        output[1] = fishes_per_timer[2]
        output[2] = fishes_per_timer[3]
        output[3] = fishes_per_timer[4]
        output[4] = fishes_per_timer[5]
        output[5] = fishes_per_timer[6]
        output[6] = fishes_per_timer[7] + fishes_per_timer[0]
        output[7] = fishes_per_timer[8]
        output[8] = fishes_per_timer[0]
    return output


### PART I
fishes_per_timer = readInput(INPUT_FILENAME)

for i in range(80):
    fishes_per_timer = processCycle(fishes_per_timer)

print ()
print ('Solution PART I   : ', sum(fishes_per_timer), ' fishes after ', i+1, ' days')
print ()


### PART II
for i in range(80,256):
    fishes_per_timer = processCycle(fishes_per_timer)

print ()
print ('Solution PART II  : ', sum(fishes_per_timer), ' fishes after ', i+1, ' days')
print ()

