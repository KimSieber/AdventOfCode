################################################
### Advent of Code 2021
###
### Tag 09 - Smoke Basin
###
### Autor:    Kim Sieber
### Erstellt: 09.12.2021
################################################

### Lies Datei ein und gibt den Meeresboden-Spiegel zurück
### @return floor[ [0,,n], [0,,n], [0,,n], ...] = 0..9 (Height)
def readInput():
    input_file = open("#09 Input", "r")
    floor = []
    for line in input_file:
        floor.append([int(h) for h in line.strip()])
    input_file.close()
    return floor

def checkLowestPoint(floor, x, y):
    def checkOne(val, x, y):
        if x not in range(len(floor)) or y not in range(len(floor[0])):    return True 
        if val < floor[x][y]                                          :    return True 
        return False 
    
    if checkOne(floor[x][y], x-1, y  ) == True and \
       checkOne(floor[x][y], x+1, y  ) == True and \
       checkOne(floor[x][y], x  , y-1) == True and \
       checkOne(floor[x][y], x  , y+1) == True       :
        return True 
    else:
        return False

def getBasinSize(floor, x1, y1):
    floor_copy = [[0 for _ in range(len(floor[0]))] for _ in range(len(floor))]
    def checkPoint(x,y):
        if x in range(len(floor)) and y in range(len(floor[0])):   
            if floor[x][y] < 9 and floor_copy[x][y] == 0:
                floor_copy[x][y] = 1
                checkPoint(x+1, y  )
                checkPoint(x-1, y  )
                checkPoint(x  , y+1)
                checkPoint(x  , y-1)
    
    checkPoint(x1,y1)
    
    summ = 0
    for line in floor_copy:
        summ += len([n for n in line if n==1])
    return summ


floor = readInput()


### PART I
sum = 0
basins = []
for x in range(len(floor)):
    for y in range(len(floor[0])):
        if checkLowestPoint(floor, x, y) == True:
            sum += floor[x][y] + 1
            basins.append(getBasinSize(floor, x, y))         # für PART II

print ()
print ('Solution Part I     : ', sum, ' is the sum of the risk levels')
print ()


### PART II
basins = sorted(basins)

print ()
print ('Solution Part II    : ', (basins[-1] * basins[-2] * basins[-3]), \
       ' is result of multipling the size of the three largest basins')
print ()