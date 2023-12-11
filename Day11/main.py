columns_with_galaxies = []
rows_without_galaxies = []
galaxies = []
expanded_galaxies = []
mega_expanded_galaxies = []
line_counter = 0
row_counter = 0
solution1 = 0
solution2 = 0

for input in open("Day11/input").readlines():
    line = list(input.strip())
    if "#" in line:
        if line.index("#") not in columns_with_galaxies:
            columns_with_galaxies.append(line.index("#"))
        for point in line:
            if point == "#":
                if row_counter not in columns_with_galaxies:
                    columns_with_galaxies.append(row_counter)
                star_position = line_counter, row_counter
                galaxies.append(star_position)
            row_counter += 1
        row_counter = 0
    else:
        rows_without_galaxies.append(line_counter)    
    line_counter += 1

expanded_galaxies = galaxies.copy()
mega_expanded_galaxies = galaxies.copy()

for i in range(len(line)):
    if i not in columns_with_galaxies:
        for j in range(len(galaxies)):
            if galaxies[j][1] > i:
                expanded_galaxies[j] = expanded_galaxies[j][0], expanded_galaxies[j][1]+1
                mega_expanded_galaxies[j] = mega_expanded_galaxies[j][0], mega_expanded_galaxies[j][1]+999999

for i in range(line_counter):
    if i in rows_without_galaxies:
        for j in range(len(galaxies)):
            if galaxies[j][0] > i:
                expanded_galaxies[j] = expanded_galaxies[j][0]+1, expanded_galaxies[j][1]
                mega_expanded_galaxies[j] = mega_expanded_galaxies[j][0]+999999, mega_expanded_galaxies[j][1]

for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        solution1 += abs(expanded_galaxies[i][0]-expanded_galaxies[j][0])+abs(expanded_galaxies[i][1]-expanded_galaxies[j][1])
        solution2 += abs(mega_expanded_galaxies[i][0]-mega_expanded_galaxies[j][0])+abs(mega_expanded_galaxies[i][1]-mega_expanded_galaxies[j][1])

print(solution1)
print(solution2)