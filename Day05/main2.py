def find_number_in_map(map_number, number):
    single_map = maps[7-map_number]
    ranges = []
    for line in single_map.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))

    for range in ranges:
        start_range = range[0]
        end_range = range[0]+range[2]
        if start_range <= number < end_range:
            #print("Zahl", number, "gefunden, die für Runde", map_number, "funktioniert und nun zu", number+(range[1]-range[0]), "wird")
            number = number+(range[1]-range[0])
            break
    map_number += 1
    #print("Zahl", number, "war nicht in der Range und bleibt unverändert für Runde", map_number)

    if map_number < 8:
        find_number_in_map(map_number, number)
    else:
        find_number_in_seeds(number)

def find_number_in_seeds(potential_seed):
    for seed1, seed2 in zip(str_seeds[::2], str_seeds[1::2]):
        seed1 = int(seed1)
        seed2 = int(seed2)
        # if potential_seed%1000000 == 0:
        #     print(potential_seed)
        if seed1 <= potential_seed < seed1+seed2:
            print(potential_seed, "ist der kleinste Seed und", j, "die entsprechende Location")
            quit()
        # else:
        #     print("Zahl", potential_seed, "ist kein Seed")



str_seeds, *maps = open("Day05/input").read().split("\n\n")
str_seeds = str_seeds.split(":")[1].split(" ")[1:]

seeds = []
j = 56900000

for seed in str_seeds:
    seeds.append(int(seed))

while True:
    j += 1
    find_number_in_map(1, j)