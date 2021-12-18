###############################################
### Advent of Code 2021
###
### Day 17 - Trick Shot
###
### author:  Kim Sieber
### create:  18.12.2021
################################################

### Test-Puzzle
#puzzle = 'target area: x=20..30, y=-10..-5'         # => 45

### Real-Puzzle
puzzle = 'target area: x=235..259, y=-118..-62'

tgt_tmp = [l.split('=')[1].split('..') for l in puzzle.split(':')[1].strip().split(',')]
target  = {'x': [int(i) for i in tgt_tmp[0]], 'y': [int(i) for i in tgt_tmp[1]]}


def getPossibleX(target):
    reply  = []
    i      = 0 
    while True:
        i += 1
        result = sum([s for s in range(i+1)])               # Gaußsche Summenformel
        if result >  target['x'][1]:
            break
        if result >= target['x'][0]:
            reply.append(i)
    return reply  
    

def startProbe(velo, target):
    replyFlag = False
    replyMaxY = 0
    x  =  y   = 0
    while x <= target['x'][1] and y >= target['y'][0]:
        x += velo['x']
        y += velo['y']
        
        if y > replyMaxY:
            replyMaxY = y
        
        if velo['x'] != 0:
            velo['x'] += 1 if velo['x'] < 0 else -1
    
        velo['y'] -= 1
        
        if x in range (target['x'][0], target['x'][1]+1) and \
           y in range (target['y'][0], target['y'][1]+1)       :
            replyFlag = True
    
    return replyFlag, replyMaxY


### PART I
possibleX  = getPossibleX(target)
possibleXYmax = []
for veloX in getPossibleX(target):
    veloY      = 0
    while veloY < 200:
        flagIn, maxY = startProbe({'x': veloX, 'y': veloY}, target)
        if flagIn == True:
            possibleXYmax.append([veloX, veloY, maxY])
        veloY += 1
print ('Solution Part I   : ', max([i[2] for i in possibleXYmax]))

        
### PART II   
possibleVelo = []
for veloX in range(0, target['x'][1]+1):
    for veloY in range (target['y'][0], 200):
        flagIn, tmp = startProbe({'x': veloX, 'y': veloY}, target)
        if flagIn == True:
            possibleVelo.append([veloX, veloY])
print ('Solution Part II  : ', len(possibleVelo))