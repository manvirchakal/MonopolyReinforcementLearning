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
		if (self.position + delta) > 39:
			print('loop')
			self.cash += 200
			pos = (self.position + delta)%40
			self.position = pos
		
		else:
			self.position += delta

	def add_cash(self, amount):
		self.cash += amount

	def take_cash(self, amount):
		self.cash -= amount