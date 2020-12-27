###############################################
##### AdventOfCode 2020
#####
##### Day 23 - Crab Cups
#####
##### @author  Kim Sieber
##### @date    25.12.2020 
##### HINWEIS: Hier funktioniert nur PART I
#####          Laufzeit fuer PART II zu lange, in Version 2 alternative
#####          Speicherverwaltung
###################################################
import time
### Puzzle-Input
PUZZLE = "653427918"
### Test-Puzzle-Input
#PUZZLE = 389125467

### Fuehrt Anzahl Runden/Moves aus und gibt Cups-Liste zurueck
### @puzzle[0..9]   = (int) 9-stellige Eingangszahl als Liste
### @rounds         = (int) gewueschte Anzahl an runden
### @puzzle[0..9]   = (int) Ergebnis-Zahlenfolge, 9 Zahlen als Liste
def moves(puzzle, rounds):
    lenPuzzle = len(puzzle)
    puzzle.insert(0, 0)
    clock = lambda a : a-lenPuzzle if a>lenPuzzle else a+lenPuzzle if a<1 else a

    pos = 1
    i   = 1
    while i <= rounds:
        if i % 500 == 0 : print("move ", i, " at Time: ", time.ctime())
        cup_curr = puzzle[clock(pos)]
        cup_1    = puzzle[clock(pos+1)]
        cup_2    = puzzle[clock(pos+2)]
        cup_3    = puzzle[clock(pos+3)]

        puzzle.remove(cup_1)
        puzzle.remove(cup_2)
        puzzle.remove(cup_3)

        cup_dest = clock(cup_curr-1)
        while cup_dest not in puzzle:
            cup_dest = clock(cup_dest-1)

        insert_index = puzzle.index(cup_dest) + 1

        puzzle.insert(insert_index, cup_3)
        puzzle.insert(insert_index, cup_2)
        puzzle.insert(insert_index, cup_1)

        for j in range(0,puzzle.index(cup_curr) - pos):
            temp = puzzle.pop(1)
            puzzle.append(temp)

        i += 1
        pos = clock(pos+1)
    return puzzle[1:]

### Gibt die Zahlen ab 1, clockweise, zurueck, ohne 1
### @puzzle         : (str) Ergebnis-Zahlenfolge, 9 Stellen
### @label          : (str) Ergebnis
def getLabel(puzzle):
    idx1   = puzzle.index(1)
    string = list(map(str, puzzle))
    return "".join(string[idx1+1:] + string[:idx1])


puzzle = [int(i) for i in str(PUZZLE)]
puzzle = moves(puzzle, 100)

print()
print("PART I  : Label of cups after 100 moves      : ", getLabel(puzzle))
print()

PUZZLE_list = [int(i) for i in str(PUZZLE)]
PUZZLE_add = [i for i in range(len(PUZZLE_list),1000001)]
puzzle = PUZZLE_list + PUZZLE_add

print()
print("START-TIME : ", time.ctime())
### ==> IMPORTANT <==  nicht 10000000-mal laufen lassen - Laufzeit zu lang
puzzle = moves(puzzle, 2000)

print("END-TIME : ", time.ctime())
print()
print("PART II : Product of the two caps after cup 1 : ... running time too long ...")
print()

