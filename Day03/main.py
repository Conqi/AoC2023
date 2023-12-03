schematic = ""

with open("Day03/input") as input:
    for line in input:
        schematic += "." + line
    line_length = len(line)+2
    schematic = ("."*(line_length-1))+"\n"+schematic+"\n"+("."*(line_length-1))+"\n"
    schematic = schematic.replace("\n", ".")

solution1 = 0
solution2 = 0

for i in range(len(schematic)):
    symbol = schematic[i]
    up_left = i-(line_length+1)
    up = i-line_length
    up_right = i-(line_length-1)
    left = i-1
    right = i+1
    down_left = i+(line_length-1)
    down = i+line_length
    down_right = i+(line_length+1)
    directions = [up_right, up, up_left, right, left, down_right, down, down_left]
    found_numbers = []
    #when a symbol is found
    if symbol.isdigit() == False and symbol != ".":
        for direction in directions:
            #search for three digit numbers
            if schematic[direction-2:direction+1].isdigit():
                solution1+=int(schematic[direction-2:direction+1])
                if symbol == "*":
                    found_numbers.append(schematic[direction-2:direction+1])
                if direction == up_right:
                    directions.remove(up)
                    directions.remove(up_left)
                if direction == up:
                    directions.remove(up_left)
                if direction == down_right:
                    directions.remove(down)
                    directions.remove(down_left)
                if direction == down:
                    directions.remove(down_left)
            elif schematic[direction-1:direction+2].isdigit():
                solution1+=int(schematic[direction-1:direction+2])
                if symbol == "*":
                    found_numbers.append(schematic[direction-1:direction+2])
                if direction == up_right:
                    directions.remove(up)
                if direction == down_right:
                    directions.remove(down)
            elif schematic[direction:direction+3].isdigit():
                solution1+=int(schematic[direction:direction+3])
                if symbol == "*":
                    found_numbers.append(schematic[direction:direction+3])
            #search for two digit numbers
            elif schematic[direction-1:direction+1].isdigit():
                solution1+=int(schematic[direction-1:direction+1])
                if symbol == "*":
                    found_numbers.append(schematic[direction-1:direction+1])
                if direction == up_right:
                    directions.remove(up)
                if direction == up:
                    directions.remove(up_left)
                if direction == down_right:
                    directions.remove(down)
                if direction == down:
                    directions.remove(down_left)
            elif schematic[direction:direction+2].isdigit():
                solution1+=int(schematic[direction:direction+2])
                if symbol == "*":
                    found_numbers.append(schematic[direction:direction+2])
            #search for one digit numbers
            elif schematic[direction].isdigit():
                solution1+=int(schematic[direction])
                if symbol == "*":
                    found_numbers.append(schematic[direction])
    if len(found_numbers) == 2:
        solution2 += int(found_numbers[0])*int(found_numbers[1])

print(solution1)
print(solution2)