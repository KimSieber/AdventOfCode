###############################################
### Advent of Code 2021
###
### Day 14 - Extended Polymerization
###
### author:  Kim Sieber
### create:  15.12.2021
################################################
from idlelib.idle_test.test_editor import insert

polymer, insertion = open("#14 Input", "r").read().split('\n\n')
insertion          = {a.split(' -> ')[0]: a.split(' -> ')[1] for a in insertion.split('\n')}
last_char          = polymer[-1]
poly               = {key: 0 for key in insertion}
for i in range(len(polymer)-1):
    poly[polymer[i:i+2]] += 1
    

def processStep(poly, insertion):
    poly_new = {key: 0 for key in insertion}
    for key in poly:
        new_keys = [key[0]+insertion[key], insertion[key]+key[1]]
        poly_new[new_keys[0]] += poly[key]
        poly_new[new_keys[1]] += poly[key]
    return poly_new


def countChar(poly, last_char):
    cntChar = {last_char: 1}
    for key in poly:
        if key[0] in cntChar:     cntChar[key[0]] += poly[key]
        else:                     cntChar[key[0]]  = poly[key]
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