import math

directions, *map = open("Day08/input").read().splitlines()

map = map[1:]
instructions = {}
start_positions = []
path_steps = []
current_position = "AAA"
steps1 = 0
steps2 = 0
solution2 = 1
j = 0

for line in map:
    position, destination = line.split(" = ")
    instructions[position] = destination[1:-1].split(", ")
    if position[-1] == "A":
        start_positions.append(position)

while current_position != "ZZZ":
    steps1 += 1 
    if directions[j] == "L":
        current_position = instructions[current_position][0]
    elif directions[j] == "R":
        current_position = instructions[current_position][1]
    if j+1 < len(directions):
        j += 1
    else:
        j = 0

j = 0

while True:
    steps2 += 1
    i = 0
    if directions[j] == "L":
        start_positions[i] = instructions[start_positions[i]][0]
    else:
        start_positions[i] = instructions[start_positions[i]][1]
    if start_positions[i][-1] == "Z":
        start_positions.pop(i)
        path_steps.append(steps2)
        steps2 = 0
        j = 0
    if j+1 < len(directions) and steps2 != 0:
        j += 1
    else:
        j = 0
    if len(start_positions) == 0:
        break

for steps in path_steps:
    solution2 = math.lcm(solution2, steps)

print(steps1)
print(solution2)