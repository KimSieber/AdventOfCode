###############################################
### Advent of Code 2021
###
### Day 14 - Extended Polymerization
###
### author:  Kim Sieber
### create:  15.12.2021
################################################

polymer, insertion = open("#14 Input", "r").read().split('\n\n')
insertion          = {a.split(' -> ')[0]: a.split(' -> ')[1] for a in insertion.split('\n')}
last_char          = polymer[-1]
poly               = {key: 0 for key in insertion}
for i in range(len(polymer)-1):
    poly[polymer[i:i+2]] += 1
    

def processStep(poly, insertion):
    poly_new = {key: 0 for key in insertion}
    for key in poly:
        poly_new[key[0]+insertion[key]] += poly[key]
        poly_new[insertion[key]+key[1]] += poly[key]
    return poly_new


def countChar(poly, last_char):
    cntChar             = {key[0]:0 for key in poly}
    cntChar[last_char] += 1
    for key in poly:      
        cntChar[key[0]] += poly[key]
    return cntChar


### PART I
for i in range(10):
    poly = processStep(poly, insertion)
cntChar = countChar(poly, last_char)
print ('Solution Part I   : ', max(cntChar.values()) - min(cntChar.values()) )


### PART II
for i in range(30):
    poly = processStep(poly, insertion)
cntChar = countChar(poly, last_char)
print ('Solution Part II  : ', max(cntChar.values()) - min(cntChar.values()) )