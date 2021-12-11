###############################################
### Advent of Code 2018
###
### Day 11 - Dumbo Octopus
###
### author:  Kim Sieber
### create:  11.12.2021
################################################

def processStep(octo):
    def processFlash(x, y):
        for x1 in range(-1, 2):
            for y1 in range(-1, 2):
                if (x+x1) in range(len(octo)) and (y+y1) in range(len(octo)):
                    if octo[y+y1][x+x1] > 0:
                        octo[y+y1][x+x1] += 1
        octo[y][x] = 0

    octo = [[o+1 for o in line] for line in octo]
    flashes = 0
    old_flashes = -1
    while old_flashes < flashes:
        old_flashes = flashes
        for x in range(len(octo)):
            for y in range(len(octo)):
                if octo[y][x] > 9:
                    flashes += 1
                    processFlash(x, y)
    return flashes, octo

### PART I
octo = [[int(o) for o in line.strip()] for line in open("#11 Input", "r")]
flash_count = 0
for step in range(100):
    flashes, octo = processStep(octo)
    flash_count += flashes

print('Part I   : ',flash_count)

### PART II
octo = [[int(o) for o in line.strip()] for line in open("#11 Input", "r")]
octo_matrix = [[0 for _ in range(len(octo))] for _ in range(len(octo))]
i = 0
while octo != octo_matrix:
    i += 1
    flashes, octo = processStep(octo)

print('Part II  : ',i)





