###############################################
### Advent of Code 2021
###
### Day 18 - Snailfish
###
### author:  Kim Sieber
### create:  20.12.2021
### hint  :  2. try
################################################
from ast import literal_eval
import re

with open("#18 Input", "r") as file:
    snailfishNumbers = [line.strip() for line in file]


def explode_number(line):
    def get_all_pairs(line):
        pairs = []          # -> enthält die Start-Positionen
        brackets = [int(m.start()) for m in re.finditer('\[',line)]
        for pos_start in brackets:
            pos_end     = line.find(']', pos_start+1)
            if line.find('[', pos_start+1, pos_end) == -1:
                if (line[:pos_start].count('[') - line[:pos_start].count(']')) >= 4:
                    pairs.append(pos_start)
        return pairs
    
    flagLoop = True 
    while flagLoop == True:
        flagLoop = False
        pairs = get_all_pairs(line)
        ### Schleife von hinten alle auflösen
        while True:
            ### Alle Paare finden, die nicht weiter geschachtelt und Level > 4
            pairs = get_all_pairs(line)
            if len(pairs) == 0: break
            ### Daten ermitteln
            startPos              = pairs[0]
            endPos                = line.find(']',startPos)
            valueLeft, valueRight = [int(m.group()) for m in re.finditer('([0-9]+)',line) if m.start() > startPos  and m.end() < endPos+1]
            line_left, line_right = line[:startPos], line[endPos+1:]
            ### Paar entfernen und 1 einseetzen
            line       = line_left + '0' + line_right
            
            ### suche nächste Zahl nach rechts und addiere drauf
            numsAfter = [m for m in re.finditer('([0-9]+)',line) if m.start() > startPos]
            if len(numsAfter) > 0:
                numAfter = numsAfter[0]
                newValue = int(numAfter.group()) + valueRight
                if newValue > 9:   flagLoop = True
                line = line[:numAfter.start()] + str(newValue) + line[numAfter.end():]
    
            ### suche nächste Zahl nach links und addiere drauf
            numsBefore = [m for m in re.finditer('([0-9]+)',line) if m.start() < startPos]
            if len(numsBefore) > 0:
                numBefore = numsBefore[-1]
                newValue = int(numBefore.group()) + valueLeft
                if newValue > 9:   flagLoop = True
                line = line[:numBefore.start()] + str(newValue) + line[numBefore.end():]
            
        ### Splitting only first from left
        numG9 = [m for m in re.finditer('([0-9]+)',line) if int(m.group()) > 9]
        if len(numG9) > 0:    
            num = numG9[0]
            line = line[:num.start()] + '[' + str(int(int(num.group())/2)) + ',' + str(int(num.group()) - int(int(num.group())/2)) + ']' + line[num.end():]
            flagLoop = True
        
    return line
    
    
def get_magnitude(tree):
    if isinstance(tree[0],list):
        tree[0] = get_magnitude(tree[0])
    if isinstance(tree[1],list):
        tree[1] = get_magnitude(tree[1])
    return ((3 * tree[0]) + (2 * tree[1]))
    
    
    return tree
    


line = snailfishNumbers[0]
for i in range(1,len(snailfishNumbers)):
    line = explode_number('[' + line + ',' + snailfishNumbers[i] + ']')

print ('( final sum is : ', line,'  )')
tree = literal_eval(line)
print ('Solution Part I   : ', get_magnitude(tree))



maxMagnitude = 0
for f in range(len(snailfishNumbers)):
    for l in range(len(snailfishNumbers)):
        if f != l:
            line = explode_number('[' + snailfishNumbers[f] + ',' + snailfishNumbers[l] + ']')
            tree = literal_eval(line)
            magn = get_magnitude(tree)
            if magn > maxMagnitude:
                maxMagnitude = magn
print ('Solution Part II  : ', maxMagnitude)
    
    
    
    
    
    
    
    