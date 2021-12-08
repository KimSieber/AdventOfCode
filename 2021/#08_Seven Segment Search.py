################################################
### Advent of Code 2021
###
### Tag 08 - Seven Segment Search
###
### Autor:    Kim Sieber
### Erstellt: 08.12.2021
################################################

### Lies Datei ein und gibt Puzzle zurück, die Segment-Buchstaben je Zahl alphabetisch sortiert
### @return puzzle[{'in': [0..n], 'out':[0..n] }] = 'abc...'
def readInput():
    input_file = open("#08 Input", "r")
    puzzle = []
    for line in input_file:
        in_out = line.split(' | ')
        in_    = [''.join(sorted(i)) for i in [i.strip() for i in in_out[0].split()] ]
        out_   = [''.join(sorted(i)) for i in [i.strip() for i in in_out[1].split()] ]
        puzzle.append( { 'in' : in_  ,     \
                         'out': out_   } )
    input_file.close()
    return puzzle

### Ermittelt für jede Ziffer 0..9 die passende Digit-Zeichenfolge (Zeichen=Segment-Anzeige)
### @return:  decoded_numbers[0..9] = 'abcd...'
def decodeNumbers(digits):
    decoded_numbers = ['' for _ in range(10)]
    for digit in digits:
        if len(digit) == 2:   decoded_numbers[1] = digit
        if len(digit) == 3:   decoded_numbers[7] = digit
        if len(digit) == 4:   decoded_numbers[4] = digit
        if len(digit) == 7:   decoded_numbers[8] = digit
    for digit in digits:
        digit_without_7  = [d for d in digit           if d not in decoded_numbers[7]]
        digit_without_47 = [d for d in digit_without_7 if d not in decoded_numbers[4]]
        if len(digit) == 5:         # 2,3,5
            if len(digit_without_47) == 2: 
                decoded_numbers[2] = digit
            elif len(digit_without_7) == 2:
                decoded_numbers[3] = digit
            else:
                decoded_numbers[5] = digit
        if len(digit) == 6:          # 0,6,9
            if len(digit_without_47) == 1: 
                decoded_numbers[9] = digit
            elif len(digit_without_7) == 4:
                decoded_numbers[6] = digit
            else:
                decoded_numbers[0] = digit
    return decoded_numbers


puzzle = readInput()


### PART I
cnt = 0
for line in puzzle:
    cnt += sum([1 for s in line['out'] if len(s) in (2,3,4,7)])

print()       
print('Solution Part I    : ', cnt, \
      ' times appear the digits 1,4,7 or 8')
print()


### PART II
summery = 0
for line in puzzle:
    dec_num = decodeNumbers(line['in'])
    val = sum([(10 ** idx_out) * dec_num.index(line['out'][3-idx_out]) for idx_out in range(4)])
    summery += val

print()       
print('Solution Part II   : ', summery, \
      ' is the summery of all output values')
print()