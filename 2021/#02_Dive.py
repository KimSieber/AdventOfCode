################################################
### Advent of Code 2021
###
### Tag 02 - Dive
###
### Autor:    Kim Sieber
### Erstellt: 03.12.2021
################################################

INPUT_FILENAME = "#02 Input"

### Datei einlesen und Ziffern als Array zurückgeben
def readInput(file_name):
    input_file = open(file_name, "r")
    commands = []
    for line in input_file:
        cmd_rar = line.split(" ")
        cmd = [cmd_rar[0], int(cmd_rar[1])]
        commands.append(cmd)
    input_file.close()
    return commands


commands = readInput(INPUT_FILENAME)

x = y = aim = 0

for cmd in commands:
    if cmd[0] == 'forward':
        x += cmd[1]
        y += aim * cmd[1]
    elif cmd[0] == 'down':
        aim += cmd[1]
    elif cmd[0] == 'up':
        aim -= cmd[1]
    
### PART I
print ()    
print ("Solution Part I   : ", (x * aim))
print ()


### PART II
print ()
print ("Solution Part II  : ", (x * y))
print ()
        
        
        
        
        
        
