str_seeds, *maps = open("Day05/input").read().split("\n\n")
str_seeds = str_seeds.split(":")[1].split(" ")[1:]

seeds = []

for seed in str_seeds:
    seeds.append(int(seed))

for single_map in maps:
    ranges = []
    for line in single_map.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))

    for seed in seeds:
        for range in ranges:
            start_range = range[1]
            end_range = range[1]+range[2]
            if start_range <= seed < end_range:
                seeds[seeds.index(seed)] = range[0]+(seed-range[1])

print(min(seeds))