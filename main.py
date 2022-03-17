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
pygame.init()
STATS_FONTS1 = pygame.font.SysFont('comicsans', 40)
STATS_FONTS2 = pygame.font.SysFont('comicsans', 13)
BOARD_IMAGE = pygame.image.load(os.path.join('Assets','board.jpeg'))
BOARD = pygame.transform.scale(BOARD_IMAGE, (500,500))


def handle_stats(player1,player2):
	pass


def take_turn(player,dice,board,mortgage_screen):
	roll, double = dice.roll()

	player.move(roll)
	index = player.position
	print(f"roll was {roll} and {player.name} is now at {board.get_tile_name(index)}")

	if board.get_tile_name(index) == 'Comm Chest':
		return False

	if board.get_tile_name(index) == 'Chance':
		return False

	if index == 0:
		return False

	if index == 4:
		player.take_cash(200)
		return False

	if index == 38:
		player.take_cash(100)
		return False

	if index == 10:
		return False

	if index == 20:
		return False

	if board.get_tile_name(index) == 'Go To Jail':
		return False

	if not board.tiles[index].is_owned:
		price = board.tiles[index].get_price()
		cash = player.get_cash()
		if cash >= price:
			board.tiles[index].buy_property(player)
			return False

		else: 
			print("CHAALLLLL PAAAAIIIIYAAAAAA OOOOYEEEEEE!!!!!")
			player.mortgage_screen_bool = True
			return True

	if board.tiles[index].is_owned:
		owner = board.tiles[index].owner
		player.take_cash(board.tiles[player.get_position()].get_rent(owner,board))
		owner.add_cash(board.tiles[player.get_position()].get_rent(owner,board))
		print(f"{player.get_name()} paid {board.tiles[player.get_position()].get_rent(owner,board)}")
		return False

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

	player1_name = STATS_FONTS1.render(player1.get_name(), 1, (0,0,0))
	player1_cash = STATS_FONTS1.render(f"${str(player1.get_cash())}", 1, (0,0,0))
	'''
	max_length = 80
	player1_prop_slice = []
	props = f"{player1.get_owned_properties()}"
	count = 0
	if len(props) > 80:
		while len(props) > 80:
			player1_prop_slice.append(props[count:count+80])
			count += 80
		if len(props)%80 < 80:
			player1_prop_slice.append(props[0:-(len(props)%80)])

	delta_y = 50
	count = 0
	for properties in player1_prop_slice:
		player1_prop = STATS_FONTS2.render(player1_prop_slice[count], 1, (0,0,0))
		WIN.blit(player1_prop, (500,delta_y))
		delta_y += 15
		count += 1
	'''
	player2_name = STATS_FONTS1.render(player2.get_name(), 1, (0,0,0))
	player2_cash = STATS_FONTS1.render(f"${str(player2.get_cash())}", 1, (0,0,0))
	WIN.blit(player1_name, (500,0))
	WIN.blit(player1_cash, (650,0))
	WIN.blit(player2_name, (500,250))
	WIN.blit(player2_cash, (650,250))

	pygame.display.update()


def main():
	board = Board()
	dice = Dice()

	player1 = Player(1500, 'Manny')
	player2 = Player(1500, 'Ananty')

	first = True
	
	clock = pygame.time.Clock()
	run = True  
	mortgage_screen = False
	index = 0
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
			red = pygame.Rect(at_tile1_coord_x, at_tile1_coord_y-10,20,20)
			green = pygame.Rect(at_tile2_coord_x,at_tile2_coord_y+10,20,20)

			if event.type == pygame.QUIT: 
				run = False 

			if event.type == pygame.KEYDOWN  and first:
				if event.key == pygame.K_r:
					first = False 
					decide_first(player1, player2, dice)
					print(player1.get_owned_properties())
					print(f"{player1.get_name()}: {player1.get_owned_properties()}")
					print(player2.get_owned_properties())
					print(f"{player2.get_name()}: {player2.get_owned_properties()}")

			if event.type == pygame.KEYDOWN and not mortgage_screen: 
				if event.key == pygame.K_r:
					if player1.turn_pos:
						mortgage_screen = take_turn(player1, dice, board, mortgage_screen)
						print(f"{player1.get_name()}: {player1.get_owned_properties()}")
						if event.type == pygame.KEYDOWN: 
							if event.key == pygame.K_r:
								mortgage_screen = take_turn(player2, dice, board, mortgage_screen)
								print(f"{player2.get_name()}: {player2.get_owned_properties()}")
					
					if player2.turn_pos:
						mortgage_screen = take_turn(player2, dice, board, mortgage_screen)
						print(f"{player2.get_name()}: {player2.get_owned_properties()}")
						if event.type == pygame.KEYDOWN: 
							if event.key == pygame.K_r:
								mortgage_screen = take_turn(player1, dice, board, mortgage_screen)
								print(f"{player1.get_name()}: {player1.get_owned_properties()}")

			if event.type == pygame.KEYDOWN and mortgage_screen and player1.mortgage_screen_bool: 
				props = player1.get_property_objects()
				if event.key == pygame.K_UP:
					if index + 1 < len(props):
						index += 1

					print(f"do you want to mortgage {props[index].get_name()}?")

				if event.key == pygame.K_DOWN: 
					if index - 1 > 0:
						index -=1

					print(f"do you want to mortgage {props[index].get_name()}?")

				if event.key == pygame.K_SPACE:
					props[index].mortgage(player1)
					print(f"{props[index].get_name()} has been mortgaged")
					player1.mortgage_screen_bool = False
					mortgage_screen = False

			if event.type == pygame.KEYDOWN and mortgage_screen and player2.mortgage_screen_bool: 
				props = player2.get_property_objects()
				if event.key == pygame.K_UP:
					if index + 1 < len(props):
						index += 1

					print(f"do you want to mortgage {props[index].get_name()}?")

				if event.key == pygame.K_DOWN: 
					if index - 1 > 0:
						index -=1

					print(f"do you want to mortgage {props[index].get_name()}?")

				if event.key == pygame.K_SPACE:
					props[index].mortgage(player2)
					print(f"{props[index].get_name()} has been mortgaged")
					player2.mortgage_screen_bool = False
					mortgage_screen = False
					break

			handle_stats(player1, player2)
			draw_window(player1,player2,red,green,board)	

	pygame.quit()



if __name__ == "__main__": 
	main()