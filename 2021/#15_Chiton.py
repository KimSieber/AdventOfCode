###############################################
### Advent of Code 2021
###
### Day 15 - Chiton
###
### author:  Kim Sieber
### create:  17.12.2021
### hint  :  Dijkstra-algorithm
### notice:  2. try (1. try with too lang running time
### running time:  PART I  < 2 sec
###                PART II > 6 Min
################################################
from math import inf as infinite


def getDistance(cavern):
    maxX      = len(cavern[0])-1
    maxY      = len(cavern   )-1   
    distances = {}
    for x in range(maxX+1):
        for y in range(maxY+1):
            distances[(x,y)] = infinite 
    distances[(0,0)] = 0
    queue     = [(0,0)] 

    while len(queue) > 0:
        x, y = queue.pop(0)
        for ax, ay in [ (x+1,y), (x-1,y), (x,y+1), (x,y-1) ]:
            if ax in range(0,maxX+1) and ay in range(0,maxY+1):
                if distances[(ax,ay)] > (distances[(x,y)] + cavern[ay][ax]):
                    distances[(ax,ay)] = distances[(x,y)] + cavern[ay][ax]
                    if (ax,ay) not in queue:
                        queue.append((ax, ay))
    return distances[(maxX, maxY)]


### PART I
cavern    = [[int(a) for a in line.strip()] for line in open("#15 Input", "r")]
print ('Solution Part I   : ', getDistance(cavern))


### PART II
cavern2 = []
for loopY in range(5):
    for y in range(len(cavern)):
        lineX = []
        for loopX in range(5):
            for x in range(len(cavern[0])):
                val = cavern[y][x] + loopX + loopY
                if val > 9:
                    val -= 9
                lineX.append(val)
        cavern2.append(lineX)
print ('Solution Part II  : ', getDistance(cavern2))