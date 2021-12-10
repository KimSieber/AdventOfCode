################################################
### Advent of Code 2021
###
### Tag 10 - Syntax Scoring
###
### Autor:    Kim Sieber
### Erstellt: 10.12.2021
################################################

### Datei einlesen in Liste
### @return: lines[0..1] = '(()<>{[...'
def readInput():
    input_file  = open("#10 Input", "r")
    lines = [l.strip() for l in input_file]
    input_file.close()   
    return lines


lines = readInput()

score = 0
points = []
for line in lines:
    old_len = len(line)+1                           ### Klammerpaare entfernen
    while len(line) < old_len:
        old_len = len(line)
        line = line.replace('[]','')
        line = line.replace('()','')
        line = line.replace('{}','')
        line = line.replace('<>','')
    for l in line:                                  ### PART I
        if l in (']',')','}','>'):
            if l == ')':     score += 3
            if l == ']':     score += 57
            if l == '}':     score += 1197
            if l == '>':     score += 25137
            break
    else:                                           ### PART II
        point = 0
        for i in range(1, len(line)+1):
            if line[-i] == '(':  point = (point * 5) + 1
            if line[-i] == '[':  point = (point * 5) + 2
            if line[-i] == '{':  point = (point * 5) + 3
            if line[-i] == '<':  point = (point * 5) + 4
        points.append(point)


print ()
print ('Solution Part I    : ',score,' is the syntax error score')
print ()

points.sort()
print ()
print ('Solution Part II   : ',points[int((len(points)-1)/2)],' is the middle score')
print ()