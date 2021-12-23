###############################################
### Advent of Code 2021
###
### Day 21 - Dirac Dice
###
### author:  Kim Sieber
### create:  23.12.2021
################################################

### TEST
### Player 1 starting position: 4
### Player 2 starting position: 8

### PUZZLE
### Player 1 starting position: 4
### Player 2 starting position: 7

import itertools

class player:
	def __init__ (self, startPosition, endScore):
		self.position = startPosition
		self.score    = 0
		self.endScore = endScore
		
	def rolling(self, points):
		self.position += points
		if self.position > 10:
			self.position -= 10
		self.score += self.position
		if self.score >= self.endScore:
			return True
		else:
			return False
		
class dice:
	def __init__ (self, sides):
		self.sides = sides
		self.dice_value = 0
		
	def rolling(self):
		points = 0
		for _ in range(3):
			self.dice_value += 1
			if self.dice_value > self.sides:
				self.dice_value -= self.sides
			points += self.dice_value
		return points
				
				
players = [player(4), player(8)]
die     = dice(100)				
				
for player_no in itertools.repeat([0,1]):
	if players[player_no].rolling(die.rolling) == True:
		break
		
winner = player_no
looser = [1,0][player_no]
				
print ('Solution Part I   : ', players[looser].score * die.dice_value)
