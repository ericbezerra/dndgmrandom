import random

class Dice:

	def __init__(self, sides):
		self.sides = sides

	def roll(self, verbose=None):
		roll = random.randint(1, self.sides)
		if verbose == True:
			print(roll)
		return roll

