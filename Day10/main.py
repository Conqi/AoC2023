def is_valid_position(grid, position):
    line, column = position
    if 0 <= line < len(grid) and 0 < column < len(grid[0]):
        if grid[line][column] != "Y":
            return True
    return False

def get_surrounding_tiles(grid, position):
    line, column = position
    adjacent = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_position = (line + dr, column + dc)
        if is_valid_position(grid, new_position):
            adjacent.append(new_position)
    return adjacent

def has_path_to_border(grid, position):
    visited = set()
    queue = []
    queue.append(position)
    visited.add(position)
    while queue:
        position = queue.pop(0)
        line, column = position
        if line == 0 or column == 0 or line == len(grid) or column == len(grid[0])-1:
            return True
        adjacent = get_surrounding_tiles(grid, position)
        for next_position in adjacent:
            if next_position not in visited:
                queue.append(next_position)
                visited.add(next_position)
    return False

line = []
grid = []
new_grid = []
line_counter = 0
position = []
direction = ""
loop_length = 0
j  = 0
points_in_loop = 0

for input in open("Day10/input"):
    line = list(input.strip())
    grid.append(line)
    new_grid.append([])
    new_grid.append([])
    new_grid.append([])
    if "S" in line:
        position.append(line_counter)
        position.append(line.index("S"))
    line_counter += 1

if grid[position[0]-1][position[1]] == "|": #| above S
    position[0] = position[0]-1
    direction = "up"
elif grid[position[0]+1][position[1]] == "|": #| below S
    position[0] = position[0]+1
    direction = "down"
elif grid[position[0]][position[1]-1] == ("-" "F" or "L"): #- or F or L left of S
    position[1] = position[1]-1
    direction = "left"
else:
    position[1] = position[1]+1
    direction = "right"

for line in grid:
    i = j*3+1
    for character_to_replace in line:
        match character_to_replace:
            case ".":
                new_grid[i-1].append(".")
                new_grid[i-1].append(".")
                new_grid[i-1].append(".")
                new_grid[i].append(".")
                new_grid[i].append(".")
                new_grid[i].append(".")
                new_grid[i+1].append(".")
                new_grid[i+1].append(".")
                new_grid[i+1].append(".")
            case "|":
                new_grid[i-1].append(".")
                new_grid[i-1].append("|")
                new_grid[i-1].append(".")
                new_grid[i].append(".")
                new_grid[i].append("|")
                new_grid[i].append(".")
                new_grid[i+1].append(".")
                new_grid[i+1].append("|")
                new_grid[i+1].append(".")
            case "-":
                new_grid[i-1].append(".")
                new_grid[i-1].append(".")
                new_grid[i-1].append(".")
                new_grid[i].append("-")
                new_grid[i].append("-")
                new_grid[i].append("-")
                new_grid[i+1].append(".")
                new_grid[i+1].append(".")
                new_grid[i+1].append(".")
            case "L":
                new_grid[i-1].append(".")
                new_grid[i-1].append("|")
                new_grid[i-1].append(".")
                new_grid[i].append(".")
                new_grid[i].append("L")
                new_grid[i].append("-")
                new_grid[i+1].append(".")
                new_grid[i+1].append(".")
                new_grid[i+1].append(".")
            case "J":
                new_grid[i-1].append(".")
                new_grid[i-1].append("|")
                new_grid[i-1].append(".")
                new_grid[i].append("-")
                new_grid[i].append("J")
                new_grid[i].append(".")
                new_grid[i+1].append(".")
                new_grid[i+1].append(".")
                new_grid[i+1].append(".")
            case "7":
                new_grid[i-1].append(".")
                new_grid[i-1].append(".")
                new_grid[i-1].append(".")
                new_grid[i].append("-")
                new_grid[i].append("7")
                new_grid[i].append(".")
                new_grid[i+1].append(".")
                new_grid[i+1].append("|")
                new_grid[i+1].append(".")
            case "F":
                new_grid[i-1].append(".")
                new_grid[i-1].append(".")
                new_grid[i-1].append(".")
                new_grid[i].append(".")
                new_grid[i].append("F")
                new_grid[i].append("-")
                new_grid[i+1].append(".")
                new_grid[i+1].append("|")
                new_grid[i+1].append(".")
            case "S":
                    new_grid[i-1].append(".")
                    new_grid[i-1].append("|")
                    new_grid[i-1].append(".")
                    new_grid[i].append("-")
                    new_grid[i].append("S")
                    new_grid[i].append("-")
                    new_grid[i+1].append(".")
                    new_grid[i+1].append("|")
                    new_grid[i+1].append(".")
    j += 1

grid = new_grid

position[0] = position[0]*3+1
position[1] = position[1]*3+1

if direction == "up":
    position[0] = position[0]+2
elif direction == "down":
    position[0] = position[0]-2
elif direction == "left":
    position[1] = position[1]+2
else:
    position[1] = position[1]-2

current_character = grid[position[0]][position[1]]

while current_character != "S":
    grid[position[0]][position[1]] = "Y"
    match current_character:
        case "|":
            if direction == "down":
                position[0] = position[0]+1
            if direction == "up":
                position[0] = position[0]-1
        case "-":
            if direction == "left":
                position[1] = position[1]-1
            if direction == "right":
                position[1] = position[1]+1
        case "L":
            if direction == "down":
                position[1] = position[1]+1
                direction = "right"
            if direction == "left":
                position[0] = position[0]-1
                direction = "up"
        case "J":
            if direction == "down":
                position[1] = position[1]-1
                direction = "left"
            if direction == "right":
                position[0] = position[0]-1
                direction = "up"
        case "7":
            if direction == "right":
                position[0] = position[0]+1
                direction = "down"
            if direction == "up":
                position[1] = position[1]-1
                direction = "left"
        case "F":
            if direction == "left":
                position[0] = position[0]+1
                direction = "down"
            if direction == "up":
                position[1] = position[1]+1
                direction = "right"
    loop_length += 1
    current_character = grid[position[0]][position[1]]

grid[position[0]][position[1]] = "Y"

line_counter = 0

for line in grid:
    line = ''.join(line).replace("|", ".").replace("-", ".").replace("L", ".").replace("J", ".").replace("7", ".").replace("F", ".").replace("|", ".")
    if line_counter%3 == 1:
        column_counter = 0
        for point in line:
            if column_counter%3 == 1 and point != "Y":            
                position = line_counter, column_counter
                if has_path_to_border(grid, position) == False:
                    points_in_loop += 1
            column_counter += 1
    line_counter += 1

print(round(loop_length/6))
print(points_in_loop)