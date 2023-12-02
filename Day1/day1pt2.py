import re
input = []
output = 0
with open("./input.txt") as input_file:
    for line in input_file:
        input.append(line)

#definitely not optimal, but all numbers!
target_regex = "one|two|three|four|five|six|seven|eight|nine|zero|0|1|2|3|4|5|6|7|8|9"
numex = re.compile(target_regex)
numbers = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}
for line in input:
    broken_line = numex.findall(line) 
#    print(broken_line)
    first_digit = numbers.get(broken_line[0], broken_line[0])  
    second_digit = numbers.get(broken_line[-1], broken_line[-1])   
#    print(first_digit, second_digit)   
    output += int(str(first_digit) + str(second_digit))

print(output)
