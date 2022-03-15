from board import Square, Property, Street, Board 
from player import Player
from dice import Dice 
import pygame
import os

WIDTH, HEIGHT = 1000,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monopoly")

FPS = 60
WHITE = (255,255,255)
BOARD_IMAGE = pygame.image.load(os.path.join('Assets','board.jpeg'))
BOARD = pygame.transform.scale(BOARD_IMAGE, (500,500))


def take_turn(player,dice,board):
	roll, double = dice.roll()

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

	if board.tiles[index].is_owned:
		owner = board.tiles[index].owner
		player.take_cash(board.tiles[player.get_position()].get_rent(owner,board))
		owner.add_cash(board.tiles[player.get_position()].get_rent(owner,board))
		return

	if double:
		print("\n\n\n\n\n\n\nDOUBLE!!!!!!!!!!\n\n\n\n\n\n\n")
		take_turn(player, dice, board)


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


def draw_window(player1,player2,red,green,board):
	WIN.fill(WHITE)
	WIN.blit(BOARD, (0,0))
	pygame.draw.rect(WIN,(255,0,0),red)
	pygame.draw.rect(WIN,(0,255,0),green)
	pygame.display.update()


def main():
	board = Board()
	dice = Dice()

	player1 = Player(1500, 'Manny')
	player2 = Player(1500, 'Ananty')

	first = True
	
	clock = pygame.time.Clock()
	run = True  
	while run:
		clock.tick(FPS)
		for event in pygame.event.get(): 
			index1 = player1.get_position()
			index2 = player2.get_position()
			at_tile1 = board.get_square(index1) 
			at_tile2 = board.get_square(index2)
			at_tile1_coord_x = at_tile1.coord[0]
			at_tile1_coord_y = at_tile1.coord[1]
			at_tile2_coord_x = at_tile2.coord[0]
			at_tile2_coord_y = at_tile2.coord[1]
			#print(f"{at_tile1_coord_x} {at_tile1_coord_y},{at_tile2_coord_x} {at_tile2_coord_y}")
			red = pygame.Rect(at_tile1_coord_x, at_tile1_coord_y,10,10)
			green = pygame.Rect(at_tile2_coord_x,at_tile2_coord_y+10,10,10)

			if event.type == pygame.QUIT: 
				run = False 

			if event.type == pygame.KEYDOWN  and first:
				if event.key == pygame.K_r:
					first = False 
					decide_first(player1, player2, dice)

			if event.type == pygame.KEYDOWN: 
				if event.key == pygame.K_r:
					if player1.turn_pos:
						take_turn(player1, dice, board)
						take_turn(player2, dice, board)
					
					if player2.turn_pos:
						take_turn(player2, dice, board)
						take_turn(player1, dice, board)

			draw_window(player1,player2,red,green,board)	

	pygame.quit()



if __name__ == "__main__": 
	main()


'''
def take_turn(player,dice,board):
	roll, double = dice.roll()

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

	if board.tiles[index].is_owned:
		owner = board.tiles[index].owner
		player.take_cash(board.tiles[player.get_position()].get_rent(owner,board))
		owner.add_cash(board.tiles[player.get_position()].get_rent(owner,board))
		return

	if double:
		print("\n\n\n\n\n\n\nDOUBLE!!!!!!!!!!\n\n\n\n\n\n\n")
		take_turn(player, dice, board)



def display_stats(player):
	properties = []
	for property in player.owned_properties:
		properties.append(property.name)

	cards = []
	for card in player.cards:
		card.append(card)

	print(f"MONEY: {player.cash}\nPROPERTIES: {properties}\nCARDS: {cards}")



board = Board()
dice = Dice()

player1 = Player(1500, 'Manny')
player2 = Player(1500, 'Ananty')

prompt = input('your move: ')

decide_first(player1, player2, dice)
num_turns = 0

while num_turns < 50:
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

		num_turns += 1

		prompt = input('your move: ')

	while prompt == 'b':
		if player1.turn_pos > player2.turn_pos:
			while board.get_type_square(player.get_position()) == Square:
				prompt = input("not valid. Try again: ")

			if (board.get_type_square(player.get_position()) == Property or board.get_type_square(player.get_position()) == Street) and not board.tiles[player.get_position()].is_owned:
				board.tiles[player1.get_position()].buy_property(player1)
'''
