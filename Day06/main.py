times, distances = open("Day06/input").read().split("\n")

gigatime = times.split(':')[1].split()
gigadistance = distances.split(':')[1].split()
gigatime = "".join(gigatime)
gigadistance = "".join(gigadistance)

times = [int(x) for x in times.split(':')[1].split()]
distances = [int(x) for x in distances.split(':')[1].split()]
winning_times = []
solution = 1

times.append(int(gigatime))
distances.append(int(gigadistance))

for time in times:
    number_is_greater_than_threshold = False
    winning_amount = 0
    for seconds in range(time):
        distance_travelled = (time-seconds)*(seconds)
        if distance_travelled > distances[times.index(time)]:
            winning_amount += 1
            number_is_greater_than_threshold = True
        elif number_is_greater_than_threshold == True:
            break
    winning_times.append(winning_amount)

winning_times.pop()

for entries in winning_times:
    solution *= entries
    
print(solution)
print(winning_amount)
