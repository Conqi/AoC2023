import math, time

start = time.time()

directions, *map = open("Day08/input").read().splitlines()

map = map[1:]
instructions = {}
start_positions = []
path_steps = []
steps = 0
solution1 = 1
solution2 = 1
j = 0

for line in map:
    position, destination = line.split(" = ")
    instructions[position] = destination[1:-1].split(", ")
    if position[-1] == "A":
        start_positions.append(position)

while True:
    steps += 1
    i = 0
    if directions[j] == "L":
        start_positions[i] = instructions[start_positions[i]][0]
    else:
        start_positions[i] = instructions[start_positions[i]][1]
    if start_positions[i][-1] == "Z":
        if start_positions[i] == "ZZZ":
            solution1 = steps
        start_positions.pop(i)
        path_steps.append(steps)
        steps = 0
        j = 0
    if j+1 < len(directions) and steps != 0:
        j += 1
    else:
        j = 0
    if len(start_positions) == 0:
        break

for steps in path_steps:
    solution2 = math.lcm(solution2, steps)

print(solution1)
print(solution2)
print(time.time()-start)