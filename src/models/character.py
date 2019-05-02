

class Character:

	def __init__(self, playerName):
		self.setPlayerName(playerName)
		

	def show(self):
		print(
			"Player Name: " + self.playerName +
			"\nCharacter Name: " + self.character_name+ 
			"\nLevel: " + str(self.level)+
			"\nRace: " + self.race+ 
			"\nSubRace: " + self.subRace+
			"\nClass: " + self.character_class+
			"\nBackground: " + self.background + 
			"\nGenre: " + self.genre+
			"\nExperience: " + str(self.xp) + 
			"\nProficiency Bonus: " + "+" +str(self.proficiencyBonus)+ 
			"\n\nAbillity Scores \n" +
			"\nStr: " + str(self.strenth) +  " "+ str(self.strmod) + 
			"\nDex: " + str(self.dexterity) +  " "+ str(self.dexmod) + 
			"\nCon: " + str(self.constitution) +  " "+ str(self.conmod) + 
			"\nInt: " + str(self.inteligence) + " " + str(self.intmod) + 
			"\nWis: " + str(self.wisdom) + " " + str(self.wismod) + 
			"\nCha: " + str(self.charisma) + " " + str(self.chamod)+ 
			"\n\nAttributes \n" +
			"\nArmor Class: " + str(self.ac) + 
			"\nSpeed: " + str(self.speed)

			)

	def setCharacterName(self, character_name):
		self.character_name = character_name

	def setClass(self, character_class="None"):
		self.character_class = character_class

	def setLevel(self, level=1):
		self.level = level

	def setRace(self, race="Human"):
		self.race = race

	def setSubRace(self, subRace="None"):
		self.subRace = subRace

	def setBackGround(self, background="None"):
		self.background = background

	def setAlignment(self, alignment="NN"):
		self.alignment = alignment

	def setPlayerName(self, playerName):
		self.playerName = playerName

	def setXP(self, xp=0):
		self.xp = xp

	def setProficiencyBonus(self, proficiencyBonus=2):
		self.proficiencyBonus = proficiencyBonus

	def setInspiration(self, inspiration=False):
		self.inspiration = inspiration

	## Ability scores

	def setStrenth(self, strenth=10):
		self.strenth = strenth
		self.strmod = self.modifiers(self.strenth)

	def setDexterity(self, dexterity=10):
		self.dexterity = dexterity
		self.dexmod = self.modifiers(self.dexterity)

	def setConstitution(self, constitution=10):
		self.constitution = constitution
		self.conmod = self.modifiers(self.constitution)

	def setInteligence(self, inteligence=10):
		self.inteligence = inteligence
		self.intmod = self.modifiers(self.inteligence)

	def setWisdom(self, wisdom=10):
		self.wisdom = wisdom
		self.wismod = self.modifiers(self.wisdom)

	def setCharisma(self, charisma=10):
		self.charisma = charisma
		self.chamod = self.modifiers(self.charisma)



	def setAC(self, ac=0):
		if ac == 0: self.ac = (10 + self.dexmod)

	def setSpeed(self, speed=30):
		self.speed = speed

	## auto

	def modifiers(self, value):
		return int((value - 10) / 2)

	def setRaceModifier(self):
		if self.race == "Human": 
			self.setSpeed(30)
			print(self.strenth)
			self.setStrenth(self.strenth+1)
			self.setDexterity(self.dexterity+1)
			self.setConstitution(self.constitution+1)
			self.setInteligence(self.inteligence+1)
			self.setWisdom(self.wisdom+1)
			self.setCharisma(self.charisma+1)
		if self.race == "Dwarf": 
			self.setSpeed(25)
			
	def setSubRaceModifier(self):
		if self.subRace == "Variant":
			self.setStrenth(self.strenth-1)
			self.setDexterity(self.dexterity-1)
			self.setConstitution(self.constitution-1)
			self.setInteligence(self.inteligence-1)
			self.setWisdom(self.wisdom-1)
			self.setCharisma(self.charisma-1)
		if self.subRace == "Hill":
				self.setWisdom(self.wisdom+1)

	# customization
	def setGenre(self, genre):
		self.genre = genre
