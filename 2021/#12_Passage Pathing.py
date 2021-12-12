##########################
### Advent of Code 2021
###
### Day 12 - Passage Pathing
###
### author:  Kim Sieber
### create:  12.12.2021
################################################

caves = [line.strip().split('-') for line in open("#12 Input", "r")]

def getConnectedCaves(caves,start_cave):
    conn_caves = []
    for cave in caves:
        if   cave[0] == start_cave: conn_caves.append(cave[1])
        elif cave[1] == start_cave: conn_caves.append(cave[0])
    return conn_caves


def checkNextCave(ways, cave, part):
    if cave == 'start'       :   return False
    if cave.isupper()        :   return True
    if cave in ways:
        if part == 1         :   return False
        else:    # part == 2
            for way in [way for way in ways if way.islower()]:
                if ways.count(way) > 1        : return False
    return True
    

def moveSub(caves, act_cave, ways_new, part):
    global ways
    ways_new.append(act_cave)
    next_caves = [cave for cave in getConnectedCaves(caves, act_cave) if cave != 'start']
    for next_cave in next_caves:
        if next_cave == 'end':
            ways_temp = ways_new[:]
            ways_temp.append('end')
            ways.append(ways_temp)
        elif checkNextCave(ways_new, next_cave, part) == True:
            moveSub(caves, next_cave, ways_new[:], part)


### PART I
ways = []
moveSub(caves, 'start', [], 1)
print('Solution Part I   : ',len(ways))

### PART II
ways = []
moveSub(caves, 'start', [], 2)
print('Solution Part II  : ',len(ways))