###############################################
##### AdventOfCode 2020
#####
##### Day 22 - Crab Combat
#####
##### @author  Kim Sieber
##### @date    23.12.2020 
###################################################
### Parameter
FILENAME = "input.txt"

### Liest Datei ein
### @file_name                         = (str) Dateiname
### @return    : players[0..1][0..n]   = (int) card_no
###                      +-------------- Zaehler Player
###                            +-------- Zaehler cards
def readInput(file_name):
    players     = []
    input_file  = open(file_name, "r")
    player_list = input_file.read().split("\n\n")
    for pl in player_list:
        deck = pl.split("\n")
        del deck[0]
        deck = [int(d) for d in deck]
        players.append(deck)
    input_file.close()
    return players

### Spielrunde ausfuehren
### Vergleicht pos[0] der Spieler miteinander, loescht pos[0] und fuegt dem Gewinner beide Werte hinten an
### Reihenfolge beim Anfuegen, groesster zuerst
### @players[0..1][0..n]                = (int) card_no
### @return    : player[0..n]           = (int) Kartenfolge des Gewinners
def play(players):
    while len(players[0]) > 0 and len(players[1]) > 0:
        cardPlayer1 = players[0].pop(0)
        cardPlayer2 = players[1].pop(0)
        if cardPlayer1 > cardPlayer2:       players[0].extend([cardPlayer1, cardPlayer2])
        if cardPlayer2 > cardPlayer1:       players[1].extend([cardPlayer2, cardPlayer1])
    if len(players[0]) > 0:     return players[0] 
    else:                       return players[1]


### Ermittelt Punktezahl des Gewinners
### @winner[0..n]                 = (int) card_no
### @return                       = (int) Punktezahl
def getScore(winner):
    score = 0
    multip = len(winner)
    for w in winner:
        score += w * multip
        multip -=1
    return score


players = readInput(FILENAME)
winner = play(players)

print()
print("PART I  : The winning player's score is       : ", getScore(winner))
print()



### Spielrunde ausfuehren
### Vergleicht pos[0] der Spieler miteinander, loescht pos[0] und fuegt dem Gewinner beide Werte hinten an
### Reihenfolge beim Anfuegen, groesster zuerst
### @set_player1[0..n]                 = (int) Set von Player 1 - card_no
### @set_player2[0..n]                 = (int) Set von Player 2 - card_no
### @return    : winner                = (int) Nr. des Gewinners, 1 oder 2
###              winners_set[0..n]     = (int) Kartenfolge des Gewinners
def playRecursive(set_player1, set_player2):
    prev_sets = []
    while len(set_player1) > 0 and len(set_player2) > 0:
        if ((set_player1), (set_player2)) in prev_sets:
            #print("the set is repeated. Player 1 wins !")
            return 1, set_player1
        prev_sets.append(((set_player1[:]),(set_player2[:])))

        cardPlayer1 = set_player1.pop(0)
        cardPlayer2 = set_player2.pop(0)

        if len(set_player1) >= cardPlayer1 and len(set_player2) >= cardPlayer2:
            winner, winners_set = playRecursive(set_player1[:cardPlayer1], set_player2[:cardPlayer2])

        else:
            if cardPlayer1 > cardPlayer2:       winner = 1
            if cardPlayer2 > cardPlayer1:       winner = 2

        if winner == 1 :       set_player1.extend([cardPlayer1, cardPlayer2])
        if winner == 2 :       set_player2.extend([cardPlayer2, cardPlayer1])
    if len(set_player1) > 0:     return 1, set_player1
    else:                        return 2, set_player2


players = readInput(FILENAME)
winner, winners_set = playRecursive(players[0], players[1])

print()
print("PART II : The winner is player ", winner, " with score : ", getScore(winners_set))
print()

