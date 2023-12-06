lines = open("Day06/input").read().split("\n")

times = [int(x) for x in lines[0].split()[1:]]
distances = [int(x) for x in lines[1].split()[1:]]

gigatime = int("".join(lines[0].split()[1:]))
gigadistance = int("".join(lines[1].split()[1:]))

solution1 = 1

def minimum_finder(time, distance):
    start_second = int(time/2)
    lowest_maximum = int(time/2)
    highest_minimum = 0
    while True:
        distance_travelled = (time-start_second)*(start_second)
        if distance_travelled > distance:
            lowest_maximum = start_second
            start_second = int((lowest_maximum+highest_minimum)/2)
        else:
            highest_minimum = start_second
            start_second = int((lowest_maximum+highest_minimum)/2)
        if start_second == lowest_maximum or start_second == highest_minimum:
            return lowest_maximum

for time, distance in zip(times, distances):
    solution1 *= time-(2*minimum_finder(time, distance)-1)

print(solution1)
print(gigatime-(2*minimum_finder(gigatime, gigadistance)-1))