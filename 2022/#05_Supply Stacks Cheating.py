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

part1 = ''
part2 = ''

stacks_example = [["Z", "N"],
                ["M", "C", "D"],
                ["P"]]

stacks_real = [["Z", "P", "M", "H", "R"],
                ["P", "C", "J", "B"],
                ["S", "N", "H", "G", "L", "C", "D"],
                ["F", "T", "M", "D", "Q", "S", "R", "L"],
                ["F", "S", "P", "Q", "B", "T", "Z", "M"],
                ["T", "F", "S", "Z", "B", "G"],
                ["N", "R", "V"],
                ["P", "G", "L", "T", "D", "V", "C", "M"],
                ["W", "Q", "N", "J", "F", "M", "L"]]

stacks_real, AnweisungsText = open('#05 Input', 'r').read().split('\n\n')
stacks_real = StapelAufloesen( stacks_real )

stacks1 = stacks_real

#part1
#with open("#05 Input Test 1", "r") as file:
Anweisungen = AnweisungsText.split('\n')
for line in Anweisungen:
    line = line.strip()
    words = line.split(' ')
    quantity = int(words[1])
    from_stack = int(words[3])
    to_stack = int(words[5])

    for i in range(quantity):
        crate = stacks1[from_stack-1].pop()
        stacks1[to_stack-1].append(crate)

for stack in stacks1:
    part1 = part1 + stack[-1]

print(part1)

