from board import Square, Property, Street, Board 
from player import Player
from dice import Dice 

def decide_first(player1,player2,dice):
	roll1 = dice.roll()
	roll2 = dice.roll()

	while roll1 == roll2:
		roll1 = dice.roll()
		roll2 = dice.roll()

	if roll1 > roll2:
		player1.turn_pos = 1 
		player2.turn_pos = 0
		return

	if roll1 < roll2:
		player1.turn_pos = 0 
		player2.turn_pos = 1
		return

	

def take_turn(player,dice,board):
	roll = dice.roll()

	player.move(roll)
	index = player.position
	print(f"roll was {roll} and {player.name} is now at {board.get_tile_name(index)}")

	if board.get_tile_name(index) == 'Comm Chest':
		return

	if board.get_tile_name(index) == 'Chance':
		return

	if index == 0:
		return

	if index == 4:
		player.take_cash(200)
		return

	if index == 38:
		player.take_cash(100)
		return

	if index == 10:
		return

	if index == 20:
		return

	if board.get_tile_name(index) == 'Go To Jail':
		return

	if not board.tiles[index].is_owned:
		board.tiles[index].buy_property(player)
		return

	elif board.tiles[index].is_owned:
		owner = board.tiles[index].owner
		player.take_cash(board.tiles[player.get_position()].get_rent(owner,board))
		owner.add_cash(board.tiles[player.get_position()].get_rent(owner,board))
		return

def display_stats(player):
	properties = []
	for property in player.owned_properties:
		properties.append(property.name)

	cards = []
	for card in player.cards:
		card.append(card)

	print(f"MONEY: {player.cash}\nPROPERTIES: {properties}\nCARDS: {cards}")



board = Board()
print(board.get_tile_name(39))
dice = Dice()

player1 = Player(1500, 'Manny')
player2 = Player(1500, 'Ananty')

prompt = input('your move: ')

decide_first(player1, player2, dice)

while prompt == 'r':
	if player1.turn_pos > player2.turn_pos:
		take_turn(player1, dice, board)
		display_stats(player1)
		take_turn(player2, dice, board)
		display_stats(player2)

	if player1.turn_pos < player2.turn_pos:
		take_turn(player2, dice, board)
		display_stats(player2)
		take_turn(player1, dice, board)
		display_stats(player1)

	prompt = input('your move: ')
