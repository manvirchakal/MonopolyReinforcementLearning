class Square():
	def __init__(self,index,name):
		self.index = index 
		self.name = name 

class Property(Square):
	def __init__(self,price,rent,color,is_mortgaged=False):
		self.price = price
		self.rent = rent
		self.color = color
		self.is_mortgaged = is_mortgaged

class Street(Property):
	def __init__(self,rent1,rent2,rent3,rent4,rent5,build_cost):
		self.rent1 = rent1
		self.rent2 = rent2
		self.rent3 = rent3
		self.rent4 = rent4
		self.rent5 = rent5
		self.build_cost = build_cost

class Board():
	def __init__(self):
		self.GO = Square(0, 'GO')
		self.medave = Street(1,'Mediterranean Ave',60,2,'Brown',10,30,90,160,250,50)
		self.commchest1 = Square(2, 'Comm Chest')
		self.baltave = Street(3,'Baltic Ave',60,4,'Brown',20,60,180,320,450,50)
		self.inctax = Square(4, 'Income Tax')
		self.rail1 = Property(5,'Reading Railroad',200, 25,'Railroad')
		self.orientave = Street(6,'Oriental Ave',100,6,'Blue',30,90,270,400,550,50)
		self.chance1 = Square(7, 'Chance')
		self.vermave = Street(8,'Vermont Ave',100,6,'Blue',30,90,270,400,550,50)
		self.connave = Street(9,'Connecticut Ave',120,8,'Blue',40,100,300,450,600,50)
		self.justv = Square(10,'Just Visiting')
		self.jail = Square(10, 'Jail')
		self.scharlep = Street(11,'St. Charles Place',140,10,'Pink',50,150,450,625,750,100)
		self.electc = Property(12,'Electric Comp',150,0,'Utility')
		self.statesave = Street(13,'States Avenue',140,10,'Pink',50,150,450,625,750,100)
		self.virgave = Street(14,'Virginia Ave',160,12,'Pink',60,180,500,700,900,100)
		self.rail2 = Property(15,'Pennsylvania Railroad',200,25,'Railroad')
		self.sjamesp = Property(16,'St. James Place',180,14,'Orange',70,200,550,750,950,100)
		self.commchest2 = Square(17, 'Comm Chest')
		self.tennave = Street(18,'Tennessee Ave',180,14,'Orange',70,200,550,750,950,100)
		self.nyave = Street(19,'New York Ave',200,16,'Orange',80,220,600,800,1000,100)
		self.freepark = Square(20, 'Free Parking')
		self.kentave = Street(21,'Kentucky Ave',220,18,'Red',90,250,700,875,1050,150)
		self.chance2 = Square(22, 'Chance')
		self.indave = Street(23,'Indiana Ave',220,18,'Red',90,250,700,875,1050,150)
		self.illave = Street(23,'Illinois Ave',240,20,'Red',100,300,750,925,1100,150)
		self.rail3 = Property(24,'B&O Railroad',200,25,'Railroad')
		self.atlave = Street(23,'Atlantic Ave',260,22,'Yellow',110,330,800,975,1150,150)
		self.ventave = Street(24,'Ventor Ave',260,22,'Yellow',110,330,800,975,1150,150)
		self.water = Property(25,'Water Works',150,0,'Utility')
		self.marvgard = Street(26,'Marvin Gardens',280,24,'Yellow',120,360,850,1025,1200,150)
		self.gotojail = Square(27, 'Go To Jail')
		self.pacave = Street(28,'Pacific Ave',300,26,'Green',130,390,900,1100,1275,200)
		self.ncarolave = Street(29, 'North Carolina Ave',300,26,'Green',130,390,900,1100,1275,200)
		self.commchest3 = Sqaure(30,'Comm Chest')
		self.pennave = Street(31,'Pennsylvania Ave',320,28,'Green',150,450,1000,1200,1400,200)
		self.rail4 = Property(32,'Short Line',200,25)
		self.chance3 = Square(33, 'Chance')
		self.parkplace = Street(34,'Park Place',350,35,'Purple',175,500,1100,1300,1500,200)
		self.luxtax = Sqaure(35,'Luxury Tax')
		self.boardwalk = Street(36,'Boardwalk',400,50,'Purple',200,600,1400,1700,2000,200)