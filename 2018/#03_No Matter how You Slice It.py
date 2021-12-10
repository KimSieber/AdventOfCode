################################################
### Advent of Code 2018
###
### Day 03 - No Matter how You Slice It
###
### author:  Kim Sieber
### create:  10.12.2021
################################################

def readInput():
    claims = []
    for claim in open("#03 Input", "r"):
        part   = claim.split('@')
        part2  = part[1].split(':')
        part20 = part2[0].split(',') 
        part21 = part2[1].split('x') 
        entry = {'claimID':int(part[0].replace('#','').strip()), \
                 'x'   : int(part20[0]), 'y'   : int(part20[1]) , \
                 'wide': int(part21[0]), 'tall': int(part21[1]) ,   }
        claims.append(entry)
    return claims


claims = readInput()

maxX = max([claim['x']+claim['wide'] for claim in claims]) + 1
maxY = max([claim['y']+claim['tall'] for claim in claims]) + 1
board = [[0 for _ in range(maxY)] for _ in range(maxX)]

### PART I
for claim in claims:
    for y in range(claim['tall']):
        for x in range(claim['wide']):
            board[claim['y'] + y][claim['x'] + x] += 1

overlapping = 0
for line in board:
    overlapping += len([1 for l in line if l>1])
    
print('Part I   : ', overlapping)

### PART II
def checkClaimOverlapping(claim):
    for y in range(claim['tall']):
        for x in range(claim['wide']):
            if board[claim['y'] + y][claim['x'] + x] > 1:
                return True
    return False
    
for claim in claims:
    if checkClaimOverlapping(claim) == False:
        break
        
print ('Part II  : ',claim['claimID'])
