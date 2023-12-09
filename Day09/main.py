import time
start = time.time()

solution2 = 0

def computeNextBiggerSequence(sequence):
    loop_ended = False
    if all(numbers == 0 for numbers in sequence):
        loop_ended = True
        difference = 0

    if loop_ended == False:
        steps = [next_number - current_number for current_number, next_number in zip(sequence, sequence[1:])]
        difference = computeNextBiggerSequence(steps)

    return sequence[-1] + difference

def computeNextSmallerSequence(sequence):
    loop_ended = False
    if all(numbers == 0 for numbers in sequence):
        loop_ended = True
        difference = 0

    if loop_ended == False:
        steps = [next_number - current_number for current_number, next_number in zip(sequence, sequence[1:])]
        difference = computeNextSmallerSequence(steps)

    return sequence[0] - difference

solution1 = 0
solution2 = 0

for input in open("Day09/input"):
    line = list(map(int, input.split()))
    solution1 += computeNextBiggerSequence(line)
    solution2 += computeNextSmallerSequence(line)

print(solution1)
print(solution2)
print(time.time() - start)