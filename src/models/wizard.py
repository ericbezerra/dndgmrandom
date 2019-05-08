from models.dice import Dice
from models.character import Character
from models.tables import *

class Wizard:
	def __init__(self):
		option = ""
		while True:
			print("\n\nGM RANDOM WIZARD\n")
			print("\n\nChoose the option\n")
			option = input("1 - Random Character\n2 - Wizard Character\n3 - Exit\n")
			if option == "1":
				self.randomChar()
			elif option == "2":
				print("Wizard...")
			else:
				break

	def randomAS(self):
		value = 0
		rolls = []
		d6 = Dice(6)
		for i in range(4):
			rolls.append(d6.roll())
		rolls.remove(min(rolls, key=int))
		for i in range(len(rolls)):
			value = value + rolls[i]
		return value

	def randomChar(self):
		c = Character("Eric")
		c.setRace(Tables().getRace())
		c.setSubRace(Tables().getSubrace(c.race))
		c.setGenre("Male")
		c.setCharacterName(Tables().getName(c.race, c.genre))
		c.setClass(Tables().getClass())
		c.setAlignment(Tables().getAlignment())
		c.setStrenth(self.randomAS())
		c.setDexterity(self.randomAS())
		c.setConstitution(self.randomAS())
		c.setInteligence(self.randomAS())
		c.setWisdom(self.randomAS())
		c.setCharisma(self.randomAS())
		c.setProficiencyBonus()
		c.setInspiration()
		c.setAC()
		c.setSpeed()
		c.setLevel()
		c.setXP()
		c.setBackGround()
		c.show()
		#print("Player name: " + c.playerName)
		#print("Character name: " + c.character_name)

	