class Square():
	def __init__(self,index,name):
		self.index = index 
		self.name = name 


class Property(Square):
	def __init__(self,index,name,price,rent,color,num_colors,is_mortgaged=False):
		self.index = index 
		self.name = name 
		self.price = price
		self.rent = rent
		self.color = color
		self.is_mortgaged = is_mortgaged
		self.is_owned = False
		self.owner = None
		self.num_colors = num_colors

	def mortgage(self, player):
		if self.is_mortgaged == False:
			self.is_mortgaged = True 
			player.add_cash(self.price/2)
		elif self.Is_mortgaged == True:
			print(f"{self.name} is already mortgaged.")

	def unmortgage(self, player):
		if self.is_mortgaged == True:
			self.is_mortgaged = False
			player.take_cash(int((self.price/2)+(self.price*0.03)))
		elif self.is_mortgaged == False:
			print(f"{self.name} is not mortgaged.")

	def check_ownership(self):
		return self.is_owned

	def buy_property(self,player):
		player.owned_properties.append(self)
		player.take_cash(self.price)
		self.owner = player
		self.is_owned = True

	def get_rent(self, player, board):
		num_prop = 0
		rent = self.rent
		for property in player.owned_properties:
			if property.color == self.color:
				num_prop += 1 

		if num_prop == self.num_colors:
			rent = self.rent*2 

		return rent



class Street(Property):
	def __init__(self,index,name,price,rent,color,rent1,rent2,rent3,rent4,rent5,build_cost,num_colors,is_mortgaged=False):
		self.index = index 
		self.name = name 
		self.price = price 
		self.rent = rent
		self.color = color
		self.is_mortgaged = is_mortgaged
		self.rent1 = rent1
		self.rent2 = rent2
		self.rent3 = rent3
		self.rent4 = rent4
		self.rent5 = rent5
		self.build_cost = build_cost
		self.num_houses = 0
		self.is_owned = False
		self.num_colors = num_colors


class Board():
	def __init__(self):
		GO = Square(0, 'GO'),
		medave = Street(1,'Mediterranean Ave',60,2,'Brown',10,30,90,160,250,50,2)
		commchest1 = Square(2, 'Comm Chest')
		baltave = Street(3,'Baltic Ave',60,4,'Brown',20,60,180,320,450,50,2)
		inctax = Square(4, 'Income Tax')
		rail1 = Property(5,'Reading Railroad',200, 25,'Railroad',4)
		orientave = Street(6,'Oriental Ave',100,6,'Blue',30,90,270,400,550,50,3)
		chance1 = Square(7, 'Chance')
		vermave = Street(8,'Vermont Ave',100,6,'Blue',30,90,270,400,550,50,3)
		connave = Street(9,'Connecticut Ave',120,8,'Blue',40,100,300,450,600,50,3)
		justv = Square(10,'Just Visiting')
		jail = Square(10, 'Jail')
		scharlep = Street(11,'St. Charles Place',140,10,'Pink',50,150,450,625,750,100,3)
		electc = Property(12,'Electric Comp',150,0,'Utility',2)
		statesave = Street(13,'States Avenue',140,10,'Pink',50,150,450,625,750,100,3)
		virgave = Street(14,'Virginia Ave',160,12,'Pink',60,180,500,700,900,100,3)
		rail2 = Property(15,'Pennsylvania Railroad',200,25,'Railroad',4)
		sjamesp = Street(16,'St. James Place',180,14,'Orange',70,200,550,750,950,100,3)
		commchest2 = Square(17, 'Comm Chest')
		tennave = Street(18,'Tennessee Ave',180,14,'Orange',70,200,550,750,950,100,3)
		nyave = Street(19,'New York Ave',200,16,'Orange',80,220,600,800,1000,100,3)
		freepark = Square(20, 'Free Parking')
		kentave = Street(21,'Kentucky Ave',220,18,'Red',90,250,700,875,1050,150,3)
		chance2 = Square(22, 'Chance')
		indave = Street(23,'Indiana Ave',220,18,'Red',90,250,700,875,1050,150,3)
		illave = Street(24,'Illinois Ave',240,20,'Red',100,300,750,925,1100,150,3)
		rail3 = Property(25,'B&O Railroad',200,25,'Railroad',4)
		atlave = Street(26,'Atlantic Ave',260,22,'Yellow',110,330,800,975,1150,150,3)
		ventave = Street(27,'Ventor Ave',260,22,'Yellow',110,330,800,975,1150,150,3)
		water = Property(28,'Water Works',150,0,'Utility',2)
		marvgard = Street(29,'Marvin Gardens',280,24,'Yellow',120,360,850,1025,1200,150,3)
		gotojail = Square(30, 'Go To Jail')
		pacave = Street(31,'Pacific Ave',300,26,'Green',130,390,900,1100,1275,200,3)
		ncarolave = Street(32, 'North Carolina Ave',300,26,'Green',130,390,900,1100,1275,200,3)
		commchest3 = Square(33,'Comm Chest')
		pennave = Street(34,'Pennsylvania Ave',320,28,'Green',150,450,1000,1200,1400,200,3)
		rail4 = Property(35,'Short Line',200,25,'Railroad',4)
		chance3 = Square(36, 'Chance')
		parkplace = Street(37,'Park Place',350,35,'Purple',175,500,1100,1300,1500,200,2)
		luxtax = Square(38,'Luxury Tax')
		boardwalk = Street(39,'Boardwalk',400,50,'Purple',200,600,1400,1700,2000,200,2)

		self.tiles = [GO,
				medave,
				commchest1,
				baltave,
				inctax,
				rail1,
				orientave,
				chance1,
				vermave,
				connave,
				[justv,jail],
				scharlep,
				electc,
				statesave,
				virgave,
				rail2,
				sjamesp,
				commchest2,
				tennave,
				nyave,
				freepark,
				kentave,
				chance2,
				indave,
				illave,
				rail3,
				atlave,
				ventave,
				water,
				marvgard,
				gotojail,
				pacave,
				ncarolave,
				commchest3,
				pennave,
				rail4,
				chance3,
				parkplace,
				luxtax,
				boardwalk]

	def get_tile_name(self,index):
		if index == 10:
			return self.tiles[index][0].name

		if index == 0:
			return 'GO'

		return self.tiles[index].name

	def get_num_tiles(self):
		print(len(self.tiles))
