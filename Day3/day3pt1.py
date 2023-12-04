import re

input = open("./day3/input.txt", "r").read().splitlines()
sum = 0
num = "[\d]+"
symbol_regex = "[^\w\.]"
# build symbol heatmap
rows, cols = len(input), len(input[0])
heatmap = [[0 for i in range(cols)] for j in range(rows)]
for x in range(rows):
    for y in range(cols):
        heatmap[x][y] = 1 if re.match(symbol_regex, input[x][y]) else 0
# search for numbers
matches = []
for line_num in range(len(input)):
    row_matches = re.finditer(num, input[line_num])
    matches += [(line_num, match) for match in row_matches]
[print(match) for match in matches]

for x, re_match in matches:
    seek_x, seek_y = (
        0 if re_match.span()[0] - 1 < 0 else re_match.span()[0] - 1,
        len(input[x])
        if re_match.span()[1] + 1 > len(input[x])
        else re_match.span()[1] + 1,
    )

    combined = (int(re_match[0]),
        str(input[x - 1][seek_x:seek_y] if x - 1 > 0 else "")
        + str(input[x][seek_x:seek_y] if x >= 0 else "")
        + str(input[x + 1][seek_x:seek_y] if x + 1 < len(input) else "")
    )
    print(combined)

    if re.search(symbol_regex, combined[1]):
        sum+=combined[0]

print("result:" + str(sum))
