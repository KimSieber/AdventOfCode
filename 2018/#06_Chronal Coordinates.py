##########################
### Advent of Code 2018
###
### Day 06 - Chronal Coordinates
###
### author:  Kim Sieber
### create:  12.12.2021
################################################

interferences = [[int(x) for x in line.strip().split(',')] for line in open("#06 Input", "r")]


def buildBoard(interferences):
    sizeX  = max( [ x[0] for x in interferences ] ) + 2
    sizeY  = max( [ y[1] for y in interferences ] ) + 2 
    board  = [ [ None for _ in range(sizeX) ] for _ in range(sizeY) ]
    board2 = [ [ 0 for _ in range(sizeX) ] for _ in range(sizeY) ]
    for y in range(sizeY):
        for x in range(sizeX):
            distances        = [ abs(interferences[point][0]-x) + abs(interferences[point][1]-y) \
                                 for point in range(len(interferences))                             ]
            closest_distance = min(distances)
            closest_point    = distances.index(closest_distance) if distances.count(closest_distance) == 1 else None
            board[y][x]      = closest_point
            board2[y][x]     = sum(distances)
            
    return board, board2


def getFinitePoints(board, interferences):
    finitive_points = [p for p in range(len(interferences))]
    maxX = len(board[0]) - 1
    maxY = len(board   ) - 1
    for y in range(maxY):
         if board[y   ][0   ] in finitive_points:  finitive_points.remove( board[y   ][0   ] )
         if board[y   ][maxX] in finitive_points:  finitive_points.remove( board[y   ][maxX] )
    for x in range(maxX):
         if board[0   ][x   ] in finitive_points:  finitive_points.remove( board[0   ][x   ] )
         if board[maxY][x   ] in finitive_points:  finitive_points.remove( board[maxY][x   ] )
    return finitive_points


board, board2 = buildBoard( interferences )
finite_points = getFinitePoints( board, interferences )
largest_area  = max([sum([sum([1 for p in line if p==point]) for line in board]) for point in finite_points])
        
print ('Solution Part I   : ', largest_area)

print ('Solutino Part II  : ', sum([sum([1 for point in line if point < 10000]) for line in board2]))







