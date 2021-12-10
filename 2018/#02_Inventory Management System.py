################################################
### Advent of Code 2018
###
### Day 02 - Inventory Management System
###
### author:  Kim Sieber
### create:  10.12.2021
################################################

lines = [line.strip() for line in open("#02 Input", "r")]

### PART I
cnt_2 = cnt_3 = 0
for line in lines:
    flag_2 = flag_3 = False
    for c in line:
        if line.count(c) == 2: flag_2 = True 
        if line.count(c) == 3: flag_3 = True 
    if flag_2 == True:   cnt_2 += 1
    if flag_3 == True:   cnt_3 += 1


print('Part I   : ', cnt_2 * cnt_3)

### PART II
def getCommonLetters(lines):
    for line in lines:
        for check in lines:
            diff = []
            for i in range(len(line)):
                if line[i] != check[i]:
                    diff.append(line[i])
            if len(diff) == 1:
                return line.replace(diff[0], '')
            
print('Part II  : ', getCommonLetters(lines))