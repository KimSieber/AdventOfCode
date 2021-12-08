################################################
### Advent of Code 2021
###
### Tag 08 - Seven Segment Search
###
### Autor:    Kim Sieber
### Erstellt: 08.12.2021
################################################

### Lies Datei ein und gibt Puzzle zurück, die Buchstaben je Seqment alphabetisch sortiert
### @return puzzle[{'in': [0..n], 'out':[0..n] }]
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


puzzle = readInput()


### PART I
cnt_uniq_num_seg = 0
for line in puzzle:
    for seg in line['out']:
        if len(seg) in [2,3,4,7]:
            cnt_uniq_num_seg += 1

print()       
print('Solution Part I    : ', cnt_uniq_num_seg, \
      ' times appear the digits 1,4,7 or 8')
print()


### PART II
### Zieht die Buchstaben aus einem String ab (entfernt diese)
def substractLetter(let_base, let_substr):
    for l in let_substr:
        let_base = let_base.replace(l,'')
    return let_base
    
### ermittelt die Zeichenketten je Zahl und gibt diese zurück
def decodeNumbers(segs):
    decoded_numbers = ['' for _ in range(10)]
    for seg in segs:
        if len(seg) == 2:
            decoded_numbers[1] = seg
        if len(seg) == 3:
            decoded_numbers[7] = seg
        if len(seg) == 4:
            decoded_numbers[4] = seg
        if len(seg) == 7:
            decoded_numbers[8] = seg
    for seg in segs:
        if len(seg) == 5:         # 2,5,3
            if len(substractLetter(substractLetter(seg, decoded_numbers[4]), decoded_numbers[7])) == 2:
                decoded_numbers[2] = seg
            elif len(substractLetter(seg, decoded_numbers[7])) == 2:
                decoded_numbers[3] = seg
            else:
                decoded_numbers[5] = seg
        if len(seg) == 6:          # 0,6,9
            if len(substractLetter(substractLetter(seg, decoded_numbers[4]), decoded_numbers[7])) == 1:
                decoded_numbers[9] = seg
            elif len(substractLetter(seg, decoded_numbers[7])) == 4:
                decoded_numbers[6] = seg
            else:
                decoded_numbers[0] = seg
    return decoded_numbers

    
summery = 0
for line in puzzle:
    dec_num = decodeNumbers(line['in'])
    val     = 0
    for idx_out in range(4):
        val += (10 ** idx_out) * dec_num.index(line['out'][3-idx_out])
    summery += val
    

print()       
print('Solution Part II   : ', summery, \
      ' is the summery of all output values')
print()








