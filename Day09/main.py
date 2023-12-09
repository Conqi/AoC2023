def computeNextSequence(sequence, p2):
    global solution2
    global soy2
    helper2 = 0
    if not soy2:
        soy2.append(sequence[0])
    loop_ended = False
    if all(numbers == 0 for numbers in sequence):
        loop_ended = True
        difference = 0
        for entries in reversed(soy2):
            helper2 = entries - helper2
        solution2 += helper2
        soy2.clear()

    if loop_ended == False:
        steps = [next_number - current_number for current_number, next_number in zip(sequence, sequence[1:])]
        soy2.append(sequence[1] - sequence[0])
        difference = computeNextSequence(steps, p2)

    return sequence[-1] + difference

solution1 = 0
solution2 = 0
soy2 = []

for input in open("Day09/biginput"):
    line = list(map(int, input.split()))
    solution1 += computeNextSequence(line, False)

print(solution1)
print(solution2)