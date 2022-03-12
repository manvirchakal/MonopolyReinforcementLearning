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

	if roll1 < roll2:
		player1.turn_pos = 0 
		player2.turn_pos = 1

	

def take_turn(player,dice):
	roll = dice.roll()

	player.move(roll)
	index = player.get_position()
	print(f"roll was {roll} and {player.name} is now at {board.get_tile_name(index)}")

	if index in [2,17,30]:
		return

	if index in [7,22,33]:
		return

	if index == 0:
		player.add_cash(200)

	if index == 4:
		player.take_cash(200)

	if index == 35:
		player.take_cash(100)

	if index == 10:
		return

	if index == 27:
		return

	if not board.tiles[index].is_owned:
		board.tiles[index].buy_property(player1)

	elif board.tiles[index].is_owned:
		owner = board.tiles[index].owner
		player.take_cash(board.tiles[player1.get_position()].get_rent())
		owner.add_cash(board.tiles[player1.get_position()].get_rent())


board = Board()
dice = Dice()

player1 = Player(1500, 'Manny')
player2 = Player(1500, 'Ananty')

prompt = input('your move: ')

decide_first(player1, player2, dice)

while prompt == 'r':
	if player1.turn_pos > player2.turn_pos:
		take_turn(player1, dice)
		take_turn(player2, dice)

	if player1.turn_pos < player2.turn_pos:
		take_turn(player2, dice)
		take_turn(player1, dice)

	prompt = input('your move: ')
