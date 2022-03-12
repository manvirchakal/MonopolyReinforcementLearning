import random 

class Dice():
	def roll(self):
		first = random.randint(1,6)
		second = random.randint(1,6)
		total = first + second
		print(total)
		return total