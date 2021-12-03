################################################
### Advent of Code 2021
###
### Tag 01 - Sonar Sweep
###
### Autor:    Kim Sieber
### Erstellt: 03.12.2021
################################################

INPUT_FILENAME = "#01 Input"

### Datei einlesen und Ziffern als Array zurückgeben
def readInput(file_name):
    input_file = open(file_name, "r")
    input_int = []
    for line in input_file:
        input_int.append(int(line.rstrip()))
    input_file.close()
    return input_int

### Ermittelt in einem Array die Anzahl zum Vorwert steigener Zahlen
def trace_increasing_values(values):
    last_val = 0
    count_inc_val = 0
    for val in values:
        if last_val > 0:
            if val > last_val:
                count_inc_val += 1
        last_val = val
    return count_inc_val

depths = readInput(INPUT_FILENAME)

### PART I
print ()    
print ("Solution Part I   : ", trace_increasing_values(depths), \
       " number of times a depth measurement increases.")
print ()


### PART II
sum_depths = []
for depth_key in range(0, len(depths)-2):
    sum = depths[depth_key] + depths[depth_key+1] + depths[depth_key+2]
    sum_depths.append(sum)

print ()    
print ("Solution Part II  : ", trace_increasing_values(sum_depths), \
       " number of times the sum of measurement in sliding window increases.")
print ()
    
    
    
    
    

