####################################################
### Advent of Code 2022
###
### Autor:    Kim Sieber
### Erstellt: 31.12.2022
###
### Tag 1: Calorie Counting
###
####################################################

### Daten auslesen und je Elfe die Kalorien-Pakete gelistet
###   elves[0..n][0..n] = (int) Kalorienzahl
elves = [[int(e) for e in elv] for elv in [c.split('\n') for c in open("#01 Input", "r").read().split('\n\n')]]

### Summe je Elfe berechnen
###   elves_sum[0..n]   = (int) Summe Kalorien
elves_sum = [sum(elv) for elv in elves]

### PART I: Maximum der Kalorien je Elfe
print ('PART I : The elve with the most calories carries ', max(elves_sum), ' calories.')

### Sortieren nach Größe, absteigend
elves_sum.sort(reverse = True)

### PART II: Summe der 3 ersten (damit größten) Kalorien-Summen 
print ('PART II: The three elve with the most calories carries totaly ', sum([elves_sum[i] for i in range(3)]), ' calories.')
