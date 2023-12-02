import re
input = []

input = open('./Day2/input.txt', 'r').read().splitlines()
ball_counter = re.compile(pattern="[0-9]*")
color_finder = re.compile(pattern='red|blue|green')

RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14

#process input
games = {}
for game in input:
	key = int(game[5:game.index(':')])
	games[key] = True
	hands = game[game.index(':')+2::].split('; ')
	ball_dict = {}
	#'1 green, 3 red, 6 blue'
	for hand in hands:
		hand = hand.split(', ')
		for balls in hand:
			# print(balls)
			color = color_finder.search(balls)[0]
			ball_count = int(ball_counter.match(balls)[0])
			if color == 'red' and ball_count > RED_LIMIT:
				games[key] = False
				break
			if color == 'blue' and ball_count > BLUE_LIMIT:
				games[key] = False
				break
			if color == 'green' and ball_count > GREEN_LIMIT:
				games[key] = False
				break

#add outputs	
# {1: true, 2:false}
output = 0
for game in games.keys():
	output += game if games[game] else 0
print(output)
# for game in games.keys():
# 	print(f'{game}: {games[game]}')