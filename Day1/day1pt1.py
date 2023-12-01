input = []
output = 0
with open("./input.txt") as input_file:
    for line in input_file:
        input.append(line)


for line in input:
    
    for char in line:
        if char.isnumeric():
            first_num = char
            break
    for char in line[::-1]:
        if char.isnumeric():
            second_num = char
            break
    output += int(first_num + second_num)

print(output)
