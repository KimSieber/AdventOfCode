###################################################
### Advent of Code 2022
###
### Autor:    Kim Sieber
### Erstellt: 26.11.2023
###
### Tag 2: Rock Paper Scissors
###                                       Pkt.
###            A = Rock        = X        1
###            B = Paper       = Y        2
###            C = Scissors    = Z        3
###
###       Win: B > X       Y > A
###            A > Z       X > C
###            C > Y       Z > B
###
###       Pkt: Win   = 6
###            Draw  = 3
###            Loose = 0
####################################################

### Definitionen / Spielregeln / Punktezählung
PktTabelle  = {'X':1, 'Y':2, 'Z':3}              # => Punkte je gewählter Hand
DrawTabelle = {'X':'A', 'Y':'B', 'Z':'C'}        # => 3 Punkte, wenn beide gleiche Hand haben
WinTabelle  = {'X':'C', 'Y':'A', 'Z':'B'}        # => 6 Punkte, wenn ich gewinne

### Definitionen für PART II
GoingWin   = {'A':'Y', 'B':'Z', 'C':'X'}              # => Was muss ich wählen (X,Y,Z), um gegen (A,B,C) zu gewinnen
GoingDraw  = {'A':'X', 'B':'Y', 'C':'Z'}              # => Was muss ich wählen (X,Y,Z), um gegen (A,B,C) ein unentschieden zu haben
GoingLoose = {'A':'Z', 'B':'X', 'C':'Y'}              # => Was muss ich wählen (X,Y,Z), um gegen (A,B,C) zu verlieren

### Funktion ermittelt Runden-Ergebnis und gibt Punktzahl zurück
def playing(ChoiceOtherPlay, ChoiceYourRespond):
    Pkt = PktTabelle[ChoiceYourRespond]
    if ChoiceOtherPlay == DrawTabelle[ChoiceYourRespond]:
        return (Pkt + 3)
    if ChoiceOtherPlay == WinTabelle[ChoiceYourRespond]:
        return (Pkt + 6)
    return Pkt
    
### Daten auslesen und je Runde die Auswahl speicher
###   rounds[0..n][0] = (int) Kalorienzahl
rounds = [round.split(' ') for round in open("#02 Input", "r").read().split('\n')]
### Auscodiert ->
#rounds = open("#02 Input Test 1", "r").read().split('\n')
#for i in range(0,len(rounds)):
#    rounds[i] = rounds[i].split(' ')

############### PART I ###############################
Pkt = []
for round in rounds:
    Pkt.append(playing(round[0], round[1]))


print ('PART I : The total score to your strategy guide is ', sum(Pkt), '.')

############### PART II ###############################
Pkt = []
for round in rounds:
    if round[1] == 'X':           # Loose
        MyHand = GoingLoose[round[0]]
    if round[1] == 'Y':           # Loose
        MyHand = GoingDraw[round[0]]
    if round[1] == 'Z':           # Loose
        MyHand = GoingWin[round[0]]
    Pkt.append(playing(round[0], MyHand))
   
print ('PART II: The total score to your strategy guide is ', sum(Pkt), '.')
    
    
    
    
    