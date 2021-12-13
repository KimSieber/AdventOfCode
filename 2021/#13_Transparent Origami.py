###############################################
### Advent of Code 2021
###
### Day 13 - Transparent Origami
###
### author:  Kim Sieber
### create:  13.12.2021
################################################

file       = open("#13 Input", "r").read().split('\n\n')
points     = [[int(c) for c in line.strip().split(',')] for line in file[0].split('\n')]
folds      = [line.split(' ')[-1].split('=') for line in file[1].split('\n')]
folds      = [[fold[0], int(fold[1])] for fold in folds]


def processFold(points, fold):
    for idx_point in range(len(points)):
        if fold[0] == 'y':
            if points[idx_point][1] > fold[1]:
                points[idx_point][1] = abs(points[idx_point][1]-(fold[1]*2))
        if fold[0] == 'x':
            if points[idx_point][0] > fold[1]:
                points[idx_point][0] = abs(points[idx_point][0]-(fold[1]*2))
    for idx_point in range(len(points)-1,-1,-1):
        if points.count(points[idx_point]) > 1:
            points.pop(idx_point)
    return points


### PART I
points = processFold(points, folds[0])
print ('Solution Part I   : ', len(points))


### PART II
for i in range(1,len(folds)):
    points = processFold(points, folds[i])
print ('Solution Part II  : ')
maxX = max([point[0] for point in points])
maxY = max([point[1] for point in points])
board = [[' ' for _ in range(maxX+1)] for _ in range(maxY+1)]
for point in points:
    board[point[1]][point[0]] = '#'
for b in board:
    line = ''
    for c in b:
        line += c
    print (line)




