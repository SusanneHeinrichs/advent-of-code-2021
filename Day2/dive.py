with open('data/day_2.txt', 'r') as f:
    lines = f.readlines()
    commands = [entry.strip() for entry in lines]

# Part 1
horizontal, depth  = 0, 0

for command in commands:
    direction, units = command.split(' ')[0], int(command.split(' ')[1])
    if(direction == "up"):
        depth -= units
    elif(direction == "down"):
        depth += units
    else:
        horizontal += units
result = depth * horizontal
print("The result of the first part is "+ str(result) + ".")

# Part 2
horizontal, depth, aim  = 0, 0, 0

for command in commands:
    direction, units = command.split(' ')[0], int(command.split(' ')[1])
    if(direction == "up"):
        aim -= units
    elif(direction == "down"):
        aim += units
    else:
        horizontal += units
        depth += aim * units
result = depth * horizontal
print("The result of the second part is "+ str(result) + ".")


