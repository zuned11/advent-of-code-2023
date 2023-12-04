
import re
input = open('./Day4/input.txt', 'r').read().splitlines()
cards = {}
result = 0
for line_num, line in enumerate(input):
    cards[line_num+1] = {'winners': [], 'guesses': [], 'copies': 1, 'wins': 0}
    cards[line_num+1]['winners'] = [int(num[0]) for num in re.finditer('\d+', line[line.index(':'): line.index('|')])]
    cards[line_num+1]['guesses'] = [int(num[0]) for num in re.finditer('\d+', line[line.index('|')::])]

for index, card in cards.items():
    for win in card['winners']:
        if win in card['guesses']:
            card['wins'] += 1
    if card['wins'] >= 1:
        while card['wins'] > 0:
            cards[index+card['wins']]['copies'] += card['copies']
            card['wins'] -= 1
    result += card['copies']

# [print(card) for card in cards.items()]
print(result)