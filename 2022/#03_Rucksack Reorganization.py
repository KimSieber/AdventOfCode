###################################################
### Advent of Code 2022
###
### Autor:    Kim Sieber
### Erstellt: 26.11.2023
###
### Tag 3: Rucksack Reorganization
###                                      
####################################################

### Rucksäcke einlesen
###   rucksaecke[0..n] = (str) Aufzählung Artikel           => Bsp: ['aASDFa', 'asdfaAfa', ...]
Rucksaecke = open("#03 Input", "r").read().split('\n')
#print (Rucksaecke)

### Priorität eines Zeichens ermitteln und zurückgeben
def ermittlePrioritaet(Zeichen):
    if Zeichen == Zeichen.upper():
        return ord(Zeichen)-38
    else:
        return ord(Zeichen)-96

### Rucksäcke in 2 Fächer teilen
###   rucksaecke[0..n][0..1] = (str) Aufzählung Artikel, unterteil nach Fächer           => Bsp: [['aAS', 'DFa'], ['asdf','aAfa'], [.,.], ...]
RucksaeckeMitFaecher = []
for r in Rucksaecke:
    RucksaeckeMitFaecher.append([ r[0:int(len(r)/2)], r[int(len(r)/2):int(len(r))] ])
#print (RucksaeckeMitFaecher)

############### PART I ###############################
### gleiche Zeichen suchen und Priorität ermitteln und addieren
SumPrio = 0
for rucksack in RucksaeckeMitFaecher:
    for i in range(int(len(rucksack[0]))):
        if rucksack[0][i] in rucksack[1]:
            SumPrio += ermittlePrioritaet(rucksack[0][i])
            break

print ('PART I : The sum of the priorities of the item typs is ', SumPrio, '.')

############### PART II ###############################
SumPrioThree = 0
### Schleife über alle Rucksack-Gruppen (3er-Gruppen)
for i in range(0,int(len(Rucksaecke)), 3):
    ### Schleife über alle Buchstaben/Items im 1. Rucksack
    for Zeichen in Rucksaecke[i]:
        if Zeichen in Rucksaecke[i+1] and \
           Zeichen in Rucksaecke[i+2]:
            SumPrioThree += ermittlePrioritaet(Zeichen)
            break;
                                 
print ('PART II: The sum of the priorities in the tree-Elf groups is ', SumPrioThree, '.')
          








