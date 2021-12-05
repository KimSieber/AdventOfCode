################################################
### Advent of Code 2021
###
### Tag 05 - Hydrothermal Venture
###
### Autor:    Kim Sieber
### Erstellt: 05.12.2021
################################################

INPUT_FILENAME = "#05 Input"  # Test 1"

### Datei einlesen in Liste
### @return: output[0..n][x1, y1, x2, y2]
def readInput(file_name):
    input_file  = open(file_name, "r")
    coords = []
    for line in input_file:
        coord = [int(c) for c in line.replace(' -> ', ',').split(',')]
        coords.append({'x1':coord[0], 'y1':coord[1], 'x2':coord[2], 'y2':coord[3]})
    return coords


### Ermittelt höchste Werte für x und y (für Board-Größe)
### @return: maxX, maxY
def getMaxCoordinate(coords):
    maxX = maxY = 0
    for coord in coords:
        if coord['x1'] > maxX: maxX = coord['x1']
        if coord['x2'] > maxX: maxX = coord['x2']
        if coord['y1'] > maxX: maxY = coord['y1']
        if coord['y2'] > maxX: maxY = coord['y2']
    return maxX, maxY


### Druckt Spielfeld aus für Test
def printBoard(board):
    for line in board:
        print_line = ''
        for coord in line:
            print_line += str(coord) if coord > 0 else '.'
        print (print_line)


### Zeichnet eine Line ins Board und gibt Board zurück
def drawLine(board, coord):
    x = coord['x1']
    y = coord['y1']
    x_step = (0 if coord['x1']==coord['x2'] else -1 if coord['x1']>coord['x2'] else 1)
    y_step = (0 if coord['y1']==coord['y2'] else -1 if coord['y1']>coord['y2'] else 1)
    board[y][x] += 1
    while x != coord['x2'] or y != coord['y2']:  
        x += x_step
        y += y_step
        board[y][x] += 1
    return board

  
### Ermittelt Anzahl Zahlen > 1 auf dem Board
def countPointsWithMoreLines(board):
    num = 0
    for line in board:
        for point in line:
            if point > 1: 
                num += 1
    return num
        
        
coords = readInput(INPUT_FILENAME)
maxX, maxY = getMaxCoordinate(coords)

### Blanko-Board erstellen: +1, weil bei 0.. beginnend und max der Höchstwert ist
board = [[0 for _ in range(maxX+1)] for _ in range(maxY+1)]         


### PART I
for coord in coords:
    if coord['x1'] == coord['x2'] or coord['y1'] == coord['y2']:
        board = drawLine(board, coord)

print()
print('Solution Part I    : ', countPointsWithMoreLines(board), \
      ' points do at least lines overlap (excl. diagonal lines)')
print()

### Board andrucken - nur für Test-Puzzle, finales Puzzle ist zu groß
#printBoard(board)


### PART II
### diagonale Linien ergänzen auf Board
for coord in coords:
    if coord['x1'] != coord['x2'] and coord['y1'] != coord['y2']:
        board = drawLine(board, coord)

print()
print('Solution Part II   : ', countPointsWithMoreLines(board), \
      ' points do at least lines overlap (incl. diagonal lines)')
print()

### Board andrucken - nur für Test-Puzzle, finales Puzzle ist zu groß
#printBoard(board)