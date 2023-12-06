lines = open("Day06/input").read().split("\n")

gigatime = int("".join(lines[0].split()[1:]))
gigadistance = int("".join(lines[1].split()[1:]))

times = [int(x) for x in lines[0].split()[1:]]
distances = [int(x) for x in lines[1].split()[1:]]
solution = 1

for time, distance in zip(times, distances):
    winning_amount = 0
    for seconds in range(time+1):
        distance_travelled = (time-seconds)*(seconds)
        if distance_travelled > distance:
            winning_amount = time - (seconds * 2) + 1
            break
    solution *= winning_amount

for seconds in range(gigatime+1):
        distance_travelled = (gigatime-seconds)*(seconds)
        if distance_travelled > gigadistance:
            winning_amount = gigatime - (seconds * 2) + 1
            break

print(solution)
print(winning_amount)