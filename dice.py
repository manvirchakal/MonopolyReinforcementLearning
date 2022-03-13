import random 

class Dice():
	def roll(self):
		double = False
		first = random.randint(1,6)
		second = random.randint(1,6)
		total = first + second
		if first == second:
			double = True

		return total, double