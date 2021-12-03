################################################
### Advent of Code 2021
###
### Tag 03 - Binary Diagnostic
###
### Autor:    Kim Sieber
### Erstellt: 03.12.2021
################################################

INPUT_FILENAME = "#03 Input"

### Datei einlesen und Ziffern als Array zurückgeben
def readInput(file_name):
    input_file = open(file_name, "r")
    input = []
    for line in input_file:
        input.append(line.rstrip())
    input_file.close()
    return input

### Ermittelt Anzahl 0 und 1 an definierter Stelle eines Binär-Strings
def count_bits(input, pos):
    out = [0,0]
    for i in input:
        out[int(i[pos])] += 1
    return out


report = readInput(INPUT_FILENAME)

### PART I
gamma   = ''
epsilon = ''

for pos in range(len(report[0])):
    out      = count_bits(report, pos)
    gamma   += '0' if out[0] >= out[1] else '1'
    epsilon += '1' if out[0] >= out[1] else '0'


print ()
print ("Solution Part I   : ", int('0b'+gamma,2) * int('0b'+epsilon,2), \
       "  is the power consumption of the submarine")
print ()

### PART II
def diagnostic_report(report, high):
    pos = 0
    rem_del = []
    while len(report) > 1:
        out = count_bits(report, pos)
        if high==True:
            keep = '1' if out[1] >= out[0] else '0'
        else:
            keep = '1' if out[1] < out[0] else '0'
        
        for r in report:
            if r[pos] != keep:
                rem_del.append(r)
    
        for d in rem_del:
            report.remove(d)
        rem_del = []
        
        pos = (pos+1) if pos < len(report[0]) else 0
    return report[0]


oxy = diagnostic_report(report[:], True)
co2 = diagnostic_report(report[:], False)

print ("Solution Part II  : ", int('0b'+oxy,2) * int('0b'+co2,2), \
       "  is the life support rating")
print ()

