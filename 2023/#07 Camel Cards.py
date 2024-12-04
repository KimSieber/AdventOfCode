#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
--- Advent of Code 2023                    ---
--- Day 7: Camel Cards                     ---
----------------------------------------------

Created: Sat Nov  9 00:09:00 2024
@author: Kim Sieber

Datentypen:
    Hands[0..n][0..3]   = Liste von "Händen", also Spielern
               [0]  -> Kartenset, bspw. AA123
               [1]  -> Einsatz, bps. 656
               [2]  -> Wert der Karten (berechnet, s.Regel unten)
               [3]  -> Gewinn, aus Einsatz und sortierter Position multipliziert
               
    Wert der Hand / des Kartensets: 
        Für jede Karte wird ein eindeutiger Wert ermittelt, nach dem über alle
        Karten am Schluss sortiert werden kann.
        Der Wert ermittelt sich aus einer Zahl, deren ersten Position die 
        "Hand/Strength" ergibt, indem die Quersumme der Kartenanzahlen gebildet wird:
            Five of a Kind       -> AAAAA  (5+5+5+5+5 = 25)
            Four of a Kind       -> AA3AA  (5+5+1+5+5 = 21)
            Full House           -> 23332  (2+3+3+3+2 = 13)
            Three of a Kind      -> TTT98  (3+3+3+1+1 = 11)
            Two Pair             -> 23423  (2+2+1+2+2 = 9)
            One Pair             -> A234A  (2+1+1+1+2 = 7)
            High Card            -> 23456  (1+1+1+1+1 = 5)
        Im folgenden hat die Zahl weitere 10 Stellen, von denen jede Karte
        zwei Stellen belegt mit ihrem Wert 2=02,3=03,...,9=09,T=10,J=11,Q=12,K=13,A=14
        
        Somit ergibt sich bspw. für die Full House-Hand "22TTT"
            => 130202101010
"""

################
### Gibt numerischen Wert einer Karte an
dictCardValue = {"A":14, "K":13, "Q":12, "J":11, "T":10, "9":9, "8":8, "7":7,
                 "6":6, "5":5, "4":4, "3":3, "2":2}


################
### Daten einlesen
###    Liest Puzzle ein und gibt ein Array mit leeren Spalten für Wert und Gewinn zurück
def getHands(FileName: str) -> list:
    InputLines = open(FileName, "r").read().splitlines() 
    Hands = []
    for Line in InputLines:
        Hand, Bit = Line.split(" ")
        Hands.append([Hand, int(Bit), 0, 0])
    return Hands


################
### Wert der Hand ermitteln
###    Berechnet die Quersumme der Anzahl von Karten je Karte
def getValueOfCardSet(CardSet: str, PartTwo = False) -> int:
    Value = 0
    ## Anzahl gleiche Karten zählen
    Anzahl      = []
    Werte       = []
    ### PART II
    AnzahlPart2 = [0]     # Alle ohne J=Joker, aber Anzahl Joker auf größte Summe addiert
                          # Initialwert = 0, da wenn alles Joker, muss dennoch ein Eintrag vorh. sein
    if PartTwo:
        AnzahlJoker = CardSet.count("J")
    
    for Card in CardSet:
        # Erste Position im Wert: "Hand"/Kombination
        Anzahl.append (CardSet.count(Card))
        ### PART II
        if PartTwo and Card != "J": 
            AnzahlPart2.append (CardSet.count(Card))
        # 2. bis 6. Position - Wert der einzelnen Karten
        Werte.append(dictCardValue[Card])
    ### PART II: Zusätzlicher Wert der Joker + Mehrwert der anderen durch Joker
    if PartTwo and AnzahlJoker > 0:
        JokerValue = ((max(AnzahlPart2) + AnzahlJoker) * AnzahlJoker)
        MoreValue  = (max(AnzahlPart2) * AnzahlJoker)
        AnzahlPart2.append(JokerValue + MoreValue)
    
    # Werte Berechnen        
    Value =  sum(Anzahl) * 10000000000
    if PartTwo:
        Value = sum(AnzahlPart2) * 10000000000
    Value += Werte[0]    *   100000000
    Value += Werte[1]    *     1000000
    Value += Werte[2]    *       10000
    Value += Werte[3]    *         100
    Value += Werte[4]   
    return Value


###############
### Werte in Reihenfolge sortieren
###    Sortiert Liste anhand 3. Spalte = Wert der Cards/Hand
def sortByValue(Hands: list) -> list:
    def getKey(base_list: list) -> int:
        return base_list[2]
    
    Hands.sort(key=getKey,reverse=False)
    return Hands


######################
### Gewinn ermitteln
###    Ergänzt Kartenliste/Hands um Gewinn je Hand in der 4. Spalte
def getWinnings(Hands: list) -> list:
    for i in range(len(Hands)):
        Hands[i][3] = Hands[i][1] * (i+1)
    return Hands
    

##################### S T A R T ########################
#Hands = getHands("#07 Test.txt")
Hands = getHands("#07 Puzzle.txt")

##################### P A R T I  #######################
for i in range(len(Hands)):
    Hands[i][2] = getValueOfCardSet(Hands[i][0])
    
Hands = sortByValue(Hands)

Hands = getWinnings(Hands)

SumOfAllWinnings = sum([Hands[i][3] for i in range(len(Hands))])

#print (f"Hands:{Hands}")
print (f"PART I : Sum of all Winnings is {SumOfAllWinnings}")

##################### P A R T II #######################
dictCardValue["J"] = 1

for i in range(len(Hands)):
    Hands[i][2] = getValueOfCardSet(Hands[i][0], True)

Hands = sortByValue(Hands)

Hands = getWinnings(Hands)

SumOfAllWinnings = sum([Hands[i][3] for i in range(len(Hands))])

print (f"PART II: Sum of all Winnings with new rule is {SumOfAllWinnings}")