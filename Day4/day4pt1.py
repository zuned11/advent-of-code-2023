import re

input = open('./Day4/input.txt', 'r').read().splitlines()

result = 0
for line in input:
    winners = [int(num[0]) for num in re.finditer('\d+', line[10:41])]
    guesses = [int(num[0]) for num in re.finditer('\d+', line[42::])]

    correct = 0
    for win in winners:
        print(f'checking for winning num {win}')
        if win in guesses:
            print(f'found {win} in {guesses}!')
            correct += 1

    if correct:
        result += 2 ** (correct - 1)
print(result)