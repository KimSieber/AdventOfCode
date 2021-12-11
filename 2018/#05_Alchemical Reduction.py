################################################
### Advent of Code 2018
###
### Day 05 - Alchemical Reduction
###
### author:  Kim Sieber
### create:  11.12.2021
################################################
import string

polymer = open("#05 Input", "r").read()

def reacting(polymer):
    len_old = len(polymer)+1
    while len(polymer) < len_old:
        len_old = len(polymer)
        for char_low in list(string.ascii_lowercase):
            polymer = polymer.replace(char_low + char_low.upper(), '')
            polymer = polymer.replace(char_low.upper() + char_low, '')
    return polymer
    
### PART I
print ('Part I   : ', len(reacting(polymer)))

### PART II
alpha = list(string.ascii_lowercase)
poly_len = []
for a in alpha:
    poly = polymer.replace(a, '')
    poly = poly.replace(a.upper(), '')
    poly_len.append(len(reacting(poly)))
    
print ('Part II  : ',min(poly_len))

