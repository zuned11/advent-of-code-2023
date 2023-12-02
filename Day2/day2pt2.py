import re
input = []

input = open('./Day2/input.txt', 'r').read().splitlines()
ball_counter = re.compile(pattern="[0-9]*")
color_finder = re.compile(pattern='red|blue|green')

#process input
games = {}
for game in input:
	key = int(game[5:game.index(':')])
	games[key] = {
		'red': 0, 'blue': 0, 'green': 0
	}
	hands = game[game.index(':')+2::].split('; ')
	#'1 green, 3 red, 6 blue'
	for hand in hands:
		hand = hand.split(', ')
		for balls in hand:
			# print(balls)
			color = color_finder.search(balls)[0]
			ball_count = int(ball_counter.match(balls)[0])
			games[key][color] = ball_count if ball_count > games[key][color] else games[key][color]

#add outputs	
# {1: true, 2:false}
output = 0
for round in games.keys():
	game = games[round]
	print(game)
	output += game['red'] * game['blue'] * game['green']
print(output)
# for game in games.keys():
# 	print(f'{game}: {games[game]}')