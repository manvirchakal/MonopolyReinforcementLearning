class Player():
	def __init__(self,cash,name):
		self.name = name
		self.cash = cash
		self.position = 0
		self.owned_properties = []
		self.cards = []
		self.turn_pos = 0

	def get_position(self):
		return self.position

	def move(self, delta):
		self.position += delta 

	def add_cash(self, amount):
		self.cash += amount

	def take_cash(self, amount):
		self.cash -= amount