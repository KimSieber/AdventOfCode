###############################################
##### AdventOfCode 2020
#####
##### Day 23 - Crab Cups
#####
##### @author  Kim Sieber
##### @date    27.12.2020 
##### HINWEIS: In Version 1 wurde Liste mit Cups veraendert: Ergebnis=Laufzeit 12 Stunden
#####          In dieser Version wurde je Cup nur Vor- und Nachgaenger gespeichert,
#####          daher keine Speicherverschiebung sondern nur punktuelle Datenaenderung
#####          Laufzeit jetzt für PART II akzeptabel.
###################################################
import time
### Puzzle-Input
PUZZLE = 653427918
### Test-Puzzle-Input
#PUZZLE = 389125467

### Puzzle - Aufbau
### puzzle[cupNo]['lef']      = (int) Cup davor
###              ['rig']      = (int) Cup danach
puzzle = {}

### Bildet Gesamt-Puzzle
def buildPuzzle(PUZZLE, num):
    puzzle = {}
    clock = lambda a : a-num if a>=num else a+num if a<0 else a

    append = []
    if num > len(str(PUZZLE)): append = [i for i in range(len(str(PUZZLE))+1,num+1)]
    puzzle_input = [int(i) for i in str(PUZZLE)] + append

    cup_first      = False
    cup_before     = False
    for cup in puzzle_input:
        if not cup_first:
            cup_first = cup
        else:
            puzzle[cup_act] = {'lef':cup_before, 'rig':cup} 
        if not cup_before: 
            cup_before = puzzle_input[len(puzzle_input)-1] 
        else:
            cup_before = cup_act
        cup_act = cup 
    puzzle[cup_act] = {'lef':cup_before, 'rig':cup_first} 
    return puzzle



### Fuehrt Anzahl Runden/Moves aus und gibt Cups-Liste zurueck
### @puzzle[0..9]   = (int) 9-stellige Eingangszahl als Liste
### @rounds         = (int) gewueschte Anzahl an runden
### @puzzle[0..9]   = (int) Ergebnis-Zahlenfolge, 9 Zahlen als Liste
def moves(puzzle, rounds):
    global PUZZLE
    len_puz = len(puzzle)
    clock = lambda a : a-len_puz if a>len_puz else a+len_puz if a<1 else a

    cup_curr = int(str(PUZZLE)[:1])
    i        = 1
    while i <= rounds:
        if i % 1000000 == 0 : print("        => move", i, "at Time: ", time.ctime())
        cup_1    = puzzle[cup_curr]['rig']
        cup_2    = puzzle[cup_1   ]['rig']
        cup_3    = puzzle[cup_2   ]['rig']

        cup_dest = clock(cup_curr - 1)
        while cup_dest in [cup_1, cup_2, cup_3]:
            cup_dest = clock(cup_dest - 1)

        puzzle[cup_curr]['rig'] = puzzle[cup_3   ]['rig']
        puzzle[cup_3   ]['rig'] = puzzle[cup_dest]['rig']
        puzzle[cup_dest]['rig'] = cup_1
        puzzle[cup_1   ]['lef'] = cup_dest

        i += 1
        cup_curr = puzzle[cup_curr]['rig']

    return puzzle

### Gibt die Zahlen ab 1, clockweise, zurueck, ohne 1
### @puzzle         : Format siehe oben
### @label          : (str) Ergebnis
def getLabel(puzzle):
    next_cup = 1
    string = ""
    for i in range(0,8):
        next_cup = puzzle[next_cup]['rig']
        string  += str(next_cup)
    return string


puzzle = buildPuzzle(PUZZLE, 9)
puzzle = moves(puzzle, 100)
print()
print("PART I  : Label of cups after 100 moves       : ", getLabel(puzzle))
print()

print("PART II => START-TIME          : ", time.ctime(), " ...")
puzzle = buildPuzzle(PUZZLE, 1000000)
print("        => cup-circle builded ...")
puzzle = moves(puzzle, 10000000)
print("        => END-TIME            : ", time.ctime(), " ...finished.")

num1 = puzzle[ 1  ]['rig']
num2 = puzzle[num1]['rig']
print()
print("PART II : Product of the two caps after cup 1 : ", num1*num2)
print()


