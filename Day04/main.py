solution = 0
card = 0
number_of_cards = {}

for input in open("Day04/input"):
    win_counter = 0
    card += 1
    if card not in number_of_cards.keys():
        number_of_cards[card] = 1
    line = input.split(":")[1].strip()
    winning_numbers, actual_numbers = line.split("|")
    winning_numbers = winning_numbers.split()
    actual_numbers = actual_numbers.split()
    repeats = number_of_cards[card]
    
    for actual_number in actual_numbers:
        if actual_number in winning_numbers:
            win_counter += 1
    
    while repeats > 0:
        win_repeats = win_counter
        while win_repeats > 0:
            number_of_cards.setdefault((card + win_repeats), 1)
            number_of_cards[(card + win_repeats)] = (number_of_cards[card+win_repeats]+1)
            win_repeats -= 1
        repeats -= 1
    if win_counter>0:
        solution += pow(2, win_counter-1)

print(solution)
print(sum(number_of_cards.values()))