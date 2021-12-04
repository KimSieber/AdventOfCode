################################################
### Advent of Code 2021
###
### Tag 04 - Giant Squid
###
### Autor:    Kim Sieber
### Erstellt: 04.12.2021
################################################

INPUT_FILENAME = "#04 Input" # Test 1"

### Datei einlesen und Nummern-Liste und Board-Liste erstellen
def readInput(file_name):
    input_file = open(file_name, "r")
    numbers    = [int(n) for n in input_file.readline().split(',')]
    input_file.readline()                      # Leerzeile nach Nummern überspringen
    boards     = []
    board      = []
    for line in input_file:
        if line.strip() != '':
            board.append(  [int(line[ 0: 2]), \
                            int(line[ 3: 5]), \
                            int(line[ 6: 8]), \
                            int(line[ 9:11]), \
                            int(line[12:14])    ] )
        else:
            boards.append(board)
            board = []
            
    boards.append(board)
    input_file.close()
    return numbers, boards

### Zahlen markieren im Board und Markierungs-Board zurückgeben
def mark_numbers(number, board, board_marked):
    l = n = 0
    for line in board:
        for num in line:
            if num == number:
                board_marked[l][n] = "X" 
            n += 1
        n  = 0
        l += 1
    return board_marked

### Board prüfen ob Bingo eingetreten und True/False zurükgeben (d.h. Reihe oder Spalte nur X) 
def check_Bingo(board_marked):
    for row in range(5):
        if board_marked[row][0] == 'X' and \
           board_marked[row][1] == 'X' and \
           board_marked[row][2] == 'X' and \
           board_marked[row][3] == 'X' and \
           board_marked[row][4] == 'X'        :
            return True
    for col in range(5):
        if board_marked[0][col] == 'X' and \
           board_marked[1][col] == 'X' and \
           board_marked[2][col] == 'X' and \
           board_marked[3][col] == 'X' and \
           board_marked[4][col] == 'X'        :
            return True
    return False

### Summiert alle markieren Zahlen im genannten Board zusammen
def sum_unmarked_numbers(boards, boards_marked, board_no):
    summery = 0
    for row in range(5):
        for col in range(5):
            if boards_marked[board_no][row][col] != 'X':
                summery += boards[board_no][row][col]
    return summery


### Datei einlesen
numbers, boards = readInput(INPUT_FILENAME)

### Blanko-MarkierungsBoards erstellen in Anzahl der existierenden Boards
boards_marked   = []
for _ in boards:
    boards_marked.append([ ['','','','',''], 
                          ['','','','',''],
                          ['','','','',''],
                          ['','','','',''],
                          ['','','','',''] ] )

### PROBLEM: Nachfolgende Initialerstellung ergibt anderes Ergebnis, obwohl scheinbar identisch
boards_marked2 = [[[''] * 5] * 5 ] * len(boards)
#boards_marked = [[[''] * 5] * 5 for _ in range(len(boards))]
#print ("boards_marked :",boards_marked)
#print ("boards_marked2:",boards_marked2)
#print ("boards        :",boards)

boards_finished             = []
boards_finished_with_number = []

### Bingo-Spielen
### -> Alle Boards gezogene Nummer prüfen und markieren (außer wenn schon gewonnen)
### -> Prüfen ob gewonnen und merken (wenn nicht schonmal gewonnen)
for number in numbers:
    for board_no in range(len(boards)):
        if board_no not in boards_finished:
            boards_marked[board_no] = mark_numbers(number, boards[board_no], boards_marked[board_no])

            if check_Bingo(boards_marked[board_no]):
                boards_finished.append(board_no)
                boards_finished_with_number.append(number)


### PART I - Score ermitteln
summery_first = sum_unmarked_numbers(boards, boards_marked, boards_finished[0])
print()
print("Solution Part I    : ", summery_first * boards_finished_with_number[0], \
      " is the final score of the first board")
print()


### PART II
summery_last = sum_unmarked_numbers(boards, boards_marked, boards_finished[-1])
print()
print("Solution Part II   : ", summery_last * boards_finished_with_number[-1], \
      " is the final score of the last board")
print()








