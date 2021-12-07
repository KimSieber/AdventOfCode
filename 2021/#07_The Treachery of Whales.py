################################################
### Advent of Code 2021
###
### Tag 07 - The Treachery of Whales
###
### Autor:    Kim Sieber
### Erstellt: 07.12.2021
################################################

input_file = open("#07 Input", "r")
crabs      = [int(f) for f in input_file.readline().split(',')]
input_file.close()

fuel_part_I  = []
fuel_part_II = []
for i in range(max(crabs)+1):
    fuel_part_I .append(sum( [          abs(i-crab)     for crab in crabs] ) ) 
    fuel_part_II.append(sum( [sum(range(abs(i-crab)+1)) for crab in crabs] ) )

### PART I
print()
print('Solution Part I    : ', min(fuel_part_I), \
      ' fuel needed to reach cheapest position')

### PART II
print()
print('Solution Part II   : ', min(fuel_part_II), \
      ' fuel needed to reach cheapest position with raising consumption')
