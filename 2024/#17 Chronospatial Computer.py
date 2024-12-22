#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
--- Advent of Code 2024                    ---
--- Day 17: Chronospatial Computer         ---
----------------------------------------------

Created: Fri Dec 20 19:16:17 2024
Author : Kim Sieber

Solution for PART II:
    https://github.com/Cdawn99/AoC2024/tree/master/Day17
     
"""
import time

A,B,C = 'A','B','C'

Puzzle = "#17 Puzzle.txt"
#Puzzle = "#17 Test2.txt"

########## INITIALISIERUNG ######################
data     = open(Puzzle, "r").read().split('\n\n')
opcodes  = [int(o) for o in data[1].split(':')[1].split(',')]
lines    = data[0].splitlines()
register = {}
register[A], register[B], register[C] = [int(line.split(':')[1]) for line in lines] 

output   = []
opcode_pnt = 0
    

########## PROGRAMS #############################
def get_inst() -> int:
    global opcode_pnt
    opcode_pnt += 1
#    print(f"opcode_pnt:{opcode_pnt}")
    return opcodes[opcode_pnt-1]

def get_combo(operand: int) -> int:
    if operand <  4: return operand
    if operand == 4: return register[A]
    if operand == 5: return register[B]
    if operand == 6: return register[C]
    if operand == 7: return False

def adv():    register[A] = int(register[A] / (2 ** get_combo(get_inst())))
def bxl():    register[B] = int(register[B] ^ get_inst())
def bst():    register[B] = get_combo(get_inst()) % 8
def jnz():    
    global opcode_pnt
    if register[A] != 0:    opcode_pnt = get_inst()
    else:                   get_inst()
def bxc():    
    register[B] = register[B] ^ register[C]
    get_inst()
def out():    output.append(get_combo(get_inst()) % 8)
def bdv():    register[B] = int(register[A] / (2 ** get_combo(get_inst())))
def cdv():    register[C] = int(register[A] / (2 ** get_combo(get_inst())))
   
function = {0:adv, 1:bxl, 2:bst, 3:jnz, 4:bxc, 5:out, 6:bdv, 7:cdv}


############### PART  I ##################
start_time = time.time()
### TEST-DATA
#register[A], register[B], register[C] = (0,0,0)
#opcodes                               = (1,7)
print("###### START #########")
print(f"register[A]:{register[A]}\nregister[B]:{register[B]}\nregister[C]:{register[C]}")
print(f"opcodes:{opcodes}")

while opcode_pnt < len(opcodes):   function[get_inst()]()

print("######  END  #########")
print(f"register[A]:{register[A]}\nregister[B]:{register[B]}\nregister[C]:{register[C]}")
print(f"output:{output}")
print()

output = [str(n) for n in output]
print(f"PART  I: ({(time.time()-start_time):.10f}s): {','.join(output)}")
# =1,5,0,1,7,4,1,0,3   ≠321575365   ≠150174103

############### PART II ##################
start_time = time.time()
register[A], register[B], register[C] = (1,0,0)
register_a = 1
i = 0
while output != opcodes:
    #print(f"+--> while register_a:{register_a}")
    output     = []
    opcode_pnt = 0
    i += 1
    register_a += (2 ** i)
    register[A] = register_a
    while opcode_pnt < len(opcodes):   function[get_inst()]()
    


print(f"PART II: ({(time.time()-start_time):.10f}s): {register_a}")