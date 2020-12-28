###############################################
##### AdventOfCode 2020
#####
##### Day 25 - Combo Breaker
#####
##### @author  Kim Sieber
##### @date    28.12.2020 
###################################################
### TEST-Input
#public_keys = [5764801, 17807724]
### Real Puzzle
public_keys = [14222596, 4057428]

### Ermittelt die Loop-Size
### @public_key         = (int) Oeffentlicher Schluessel
### @return             = (int) Anzahl Loops = Loop-Size
def getLoopSize(public_key):
    val  = 1
    loop = 0
    while val != public_key:
        loop += 1
        val = val * 7
        val = val % 20201227
    return loop

### Ermittelt den Verschluesselungs-Schluessel
### @public_key         = (int) Oeffentlicher Schluessel
### @loop_size          = (int) Anzahl Loops = Loop-Size
### @return             = (int) encryption key
def getEncryptKey(public_key, loop_size):
    val  = 1
    for _ in range(loop_size):
        val = val * public_key
        val = val % 20201227
    return val

loop_sizes = [getLoopSize(public_keys[0]), getLoopSize(public_keys[1])]
encrypt_keys = [getEncryptKey(public_keys[0],loop_sizes[1]), getEncryptKey(public_keys[1],loop_sizes[0])]

print()
if encrypt_keys[0] != encrypt_keys[1]:
    print("FEHLER - encryption keys sind unterschiedlich")
else:
    print("PART I & II : The encryption key is : ", encrypt_keys[0])
print()
