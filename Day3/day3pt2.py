import re

input = open("./day3/input.txt", "r").read().splitlines()
# input = input[0:10]
output = 0
num = "[\d]+|[\d]\.[\d]"
sym = "[*]"
sep_num = "[\d]{1}[\.|*]{1}[\d]{1}"
# sep_num = "[\d][\.|^\w][\d]"

# build symbol heatmap
rows, cols = len(input), len(input[0])
symbol_coords = []
for x in range(rows):
    for y in range(cols):
        # print(input[x][y])
        if re.match(sym, input[x][y]):
            # print('match')
            symbol_coords.append((x, y))
# search for numbers
# print('coords:')
# [print(coords) for coords in symbol_coords]
targets = []
for symbol in symbol_coords:
    combined = (
        input[symbol[0] - 1][symbol[1] - 1 : symbol[1] + 2],
        input[symbol[0]][symbol[1] - 1 : symbol[1] + 2],
        input[symbol[0] + 1][symbol[1] - 1 : symbol[1] + 2],
    )
    [print(x) for x in combined]
    to_break = False
    for part in combined:
        print(f'part: {part} and combined: {combined}')
        if re.search(sep_num, part):
            print(re.search(sep_num, part))
            if part == combined[0]:
                targets.append((symbol, -1))
            elif part == combined[1]:
                targets.append((symbol, 'same'))
            elif part == combined[2]:
                targets.append((symbol, 1))
            to_break = True
    if to_break:
        continue
    else:
        combined = [bool(re.search(num, part)) for part in combined]
        print(combined)
        if sum(combined) == 2:
            targets.append((symbol, False))

# print(targets)


def recurse_left(line: str, index: int) -> str:
    if index - 1 >= 0:
        if line[index - 1].isnumeric():
            return recurse_left(line, index - 1) + str(line[index])
        elif not line[index - 1].isnumeric():
            if line[index].isnumeric():
                return line[index]
            else:
                return ''
    elif index == 0:
        return str(line[index])


def recurse_right(line: str, index: int) -> str:
    if index + 1 < len(line):
        if line[index + 1].isnumeric():
            return str(line[index]) + recurse_right(line, index + 1)
        elif not line[index + 1].isnumeric():
            if line[index].isnumeric():
                return line[index]
            else:
                return ''
    elif index == len(line) - 1:
        return str(line[index])


def separated_numbers(row, col) -> int:
    # print('recursing as sep numbers')
    # print(input[row], col)
    left = recurse_left(input[row], col - 1)
    right = recurse_right(input[row], col + 1)
    print('left/right: ', left, right)
    return (left, right)


def different_numbers(row, col) -> int:
    if found := re.match('\d{3}', input[row][col-1:col+2]):
        # print('found: ', found)
        return found[0]
    left = recurse_left(input[row], col).strip(".")
    right = recurse_right(input[row], col).strip(".")
    # print('different numbers left/right', left, right)
    if left == right:
        return left
    elif left := re.search(num, left):
        left = left[0]
    else:
        left = ""
    if right := re.search(num, right):
        right = right[0]
    else:
        right = ""
    if left.rstrip(".").isnumeric() and len(left) > len(right):
        return left
    elif right.lstrip(".").isnumeric() and len(right) > len(left):
        return right
    else:
        return None


for target in targets:
    print("target:", target)
    col = target[0][1]
    if target[1] or target[1] == 'same':
        if target[1] == 'same':
            row = target[0][0]
        else:
            row = target[0][0] + target[1]
        sep = separated_numbers(row, col)
        # print(f'sep: {sep}')
        output += int(sep[0]) * int(sep[1])
    elif not target[1]:
        row = target[0][0]
        below = different_numbers(row + 1, col)
        middle = different_numbers(row, col)
        above = different_numbers(row - 1, col)
        # this case indicates the sep_num regex triggered
        # print(f"above: {above} middle: {middle} below: {below}")
        all = [above, middle, below]
        # print(all)
        if None in all:
            all.remove(None)
        if '' in all:
            all.remove('')
        print(all)
        output += (int(all[0]) * int(all[1]))


print(f"output: {output}")
