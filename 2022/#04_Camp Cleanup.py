###################################################
### Advent of Code 2022
###
### Autor:    Kim Sieber
### Erstellt: 26.11.2023
###
### Tag 4: Camp Cleanup
###                                      
####################################################

### Zeilen einlesen
Lines = open('#04 Input', 'r').read().split('\n')

### Zähler für Aufgabe Part 1 + 2
PairsFullyOverlap = 0
PairsOverlap = 0

### Je Zeile die Zahlen extrahieren und vergleichen
for Line in Lines:
    ab, cd = Line.split(',')
    a, b = [int(num) for num in ab.split('-')]
    c, d = [int(num) for num in cd.split('-')]
    
    ### PART I
    if (a <= c and d <= b) or (c <= a and b <= d):
        PairsFullyOverlap += 1;

    ### PART II
    if ( (a >= c and a <= d) or (b >= c and b <= d) ) or \
       ( (c >= a and c <= b) or (d >= a and d <= b) ): 
        PairsOverlap += 1;

############### PART I ###############################
print ('PART I : ', PairsFullyOverlap, ' assignment pairs does one range fully contain the other range.')    

############### PART II ###############################
print ('PART II: ', PairsOverlap, ' assignment pairs does the range overlap.')    



