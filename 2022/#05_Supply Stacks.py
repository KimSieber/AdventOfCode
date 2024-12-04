###################################################
### Advent of Code 2022
###
### Autor:    Kim Sieber
### Erstellt: 27.11.2023
###
### Tag 5: Supply Stacks
###                  
### Bsp. Stapeldefinition
### ---------------------      
###       [D]    
###   [N] [C]    
###   [Z] [M] [P]
###    1   2   3         
###
### Bsp. Anweisungsliste
### --------------------   
### move 1 from 2 to 1
### move 3 from 1 to 3
### move 2 from 2 to 1   
####################################################

####################################################
### Stapel-Zeichenkette in Array auflösen
###
### @param  StapelEingabe      = (str) Zeichenkette der Stapelelemente, mit Leerzeichen und Zeilenumbruch positioniert (Bsp. s.o.)
### @return Stapel[0..n][0..n] = (str) Kisten-ID, bspw. A, B, C, ... (in Reihenfolge Stapel 0-n und Höhe 0-n)
def StapelAufloesen(StapelText):
    Zeile        = StapelText.split('\n')
    StapelAnzahl = max( [ int(c) for c in Zeile[len(Zeile)-1].split() ] )
    StapelHoehe  = len(Zeile)-1
    Stapel       = [ ['' for a in range(StapelHoehe)] for b in range(StapelAnzahl) ]
    ### Schleife für alle Ebenen
    Ebene = 0
    for iEbene in range((len(Zeile)-2), -1, -1):
        StapelNr = 0
        ### Schleife für alle Stapel
        for iStapelNr in range (1, len(Zeile[iEbene])-1, 4):
            Stapel[ StapelNr ] [ Ebene ] = Zeile[ iEbene ] [ iStapelNr ]
            StapelNr += 1
        Ebene += 1
    ### Stapel um leere Felder reduzieren
    for i in range(StapelAnzahl):
        while ' ' in Stapel[i]:
            Stapel[i].remove(' ')
    ### Ergebnis zurückgeben
    return Stapel

####################################################
### Anweisungs-Liste in Array auflösen
###
### @param  AnweisungsListe    = (str) Zeichenkette mit Anweisungen, mit Zeilenumbruch getrennt (Bsp. s.o.)
### @return Anweisung[0..n][0..2] = (int) Anweisung  -> [..][0] = Anzahl zu bewegender Kisten
###                                                  -> [..][1] = Quell-Stapel  
###                                                  -> [..][1] = Ziel-Stapel  
def AnweisungenAufloesen(AnweisungsText):
    Anweisung = []
    AnweisungsListe = AnweisungsText.split('\n')
    for AnwZeile in AnweisungsListe:
        AnwEinzel = AnwZeile.split(' ')
        NeueAnweisung = [ int(AnwEinzel[1]), int(AnwEinzel[3]), int(AnwEinzel[5]) ]
        Anweisung.append( NeueAnweisung )
    return Anweisung

###############################################################
### Funktion zur Bewegung einer Kiste (PART I: Einzelne Kisten)
###
### @param  Stapel[0..n][0..n]    = (str) Kisten-ID    -> Ausgangs-Stapel
### @param  Anweisung[0..2]       = (int) Einzelne Anweisung
### @return Stapel[0..n][0..n]    = (str) Kisten-ID    -> Veränderter Stapel
def BewegungAusfuehren_PART_I(Stapel, Anweisung):
    for i in range( Anweisung[0] ):
        Kiste = Stapel[Anweisung[1]-1 ].pop()
        Stapel[Anweisung[2]-1].append( Kiste  ) 
    return Stapel

###############################################################
### Funktion zur Bewegung einer Kiste (PART II: Alle Kisten einer Anweisung zusammen)
###
### @param  Stapel[0..n][0..n]    = (str) Kisten-ID    -> Ausgangs-Stapel
### @param  Anweisung[0..2]       = (int) Einzelne Anweisung
### @return Stapel[0..n][0..n]    = (str) Kisten-ID    -> Veränderter Stapel
def BewegungAusfuehren_PART_II(Stapel, Anweisung):
    StartPos    = len(Stapel[ Anweisung[1]-1 ]) - Anweisung[0]
    KistenListe = []
    for i in range( Anweisung[0] ):
        KistenListe.append( Stapel[ Anweisung[1]-1 ].pop( StartPos ) )
    for KL in KistenListe:
        Stapel[ Anweisung[2]-1 ].append( KL ) 
    return Stapel

### Auslesen der Datei, Abschnitt Stapeldefinition, Abschnitt Anweisungsliste
StapelText, AnweisungsText = open('#05 Input', 'r').read().split('\n\n')

### Stapel in Array umwandeln
###   Stapel[0..n][0..n] = Kisten-ID, bspw. A, B, C, ... (in Reihenfolge Stapel 0-n und Höhe 0-n)
Stapel = StapelAufloesen( StapelText )

### Anweisungen in Array umwandeln
###   Anweisung[0..n][0..2] = (int) Anweisung
Anweisung = AnweisungenAufloesen( AnweisungsText )

### Anweisungen ausführen
for Anw in Anweisung:
    Stapel = BewegungAusfuehren_PART_I( Stapel, Anw )

############### PART I ###############################
print ('PART I : The top-crates after the rearrangement completes is    :', ''.join( [i.pop() for i in Stapel] ) )    

### Stapel in Array umwandeln (erneut, damit Anfang wieder hergestellt)
###   Stapel[0..n][0..n] = Kisten-ID, bspw. A, B, C, ... (in Reihenfolge Stapel 0-n und Höhe 0-n)
Stapel = StapelAufloesen( StapelText )

### Anweisungen ausführen
for Anw in Anweisung:
    Stapel = BewegungAusfuehren_PART_II( Stapel, Anw )

############### PART I ###############################
print ('PART II: The top-crates after the new rearrangement completes is:', ''.join( [i.pop() for i in Stapel] ) )    




