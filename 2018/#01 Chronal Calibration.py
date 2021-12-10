################################################
### Advent of Code 2018
###
### Day 01 - Chronal Calibration
###
### author:  Kim Sieber
### create:  09.12.2021
################################################

calibs = [int(line) for line in open("#01 Input", "r")]

### PART I
print('Part I     : ', sum(calibs))

### PART II
freqs = []
freq = 0
i = 0
while freq not in freqs:
    freqs.append(freq)
    freq += calibs[i]
    i += 1
    if i >= len(calibs):   i = 0

print('Part II    : ', freq)
