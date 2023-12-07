input = open("Day07/input").readlines()

def findHandStrength(hand):
    hand_strength = [0]
    for card in hand:
        if card != "1":
            hand_strength.append(hand.count(card))
    for card in hand:
        if card == "1":
            hand_strength[hand_strength.index(max(hand_strength))] = max(hand_strength)+1
    if 5 in hand_strength:
        return 7
    elif 4 in hand_strength:
        return 6
    elif 3 in hand_strength:
        if hand_strength.count(2) == 2 or (hand_strength.count(3) == 1 and hand_strength.count(2) == 3):
            return 5
        return 4
    elif hand_strength.count(2) == 4:
        return 3
    elif 2 in hand_strength:
        return 2
    else:
        return 1

i = 0
j = 1
hands1 = {}
hands2 = {}
winnings1 = 0
winnings2 = 0

for line in input:
    replaced_hand = "".join(input[i].split(" ")[0].replace("A", "E").replace("J", "B").replace("Q", "C").replace("K", "D").replace("T", "A"))
    hands1[str(findHandStrength(input[i].split(" ")[0]))+replaced_hand] = int(input[i].split(" ")[1].strip())
    
    replaced_hand = "".join(input[i].split(" ")[0].replace("A", "E").replace("J", "1").replace("Q", "C").replace("K", "D").replace("T", "A"))
    hands2[str(findHandStrength(replaced_hand))+replaced_hand] = int(input[i].split(" ")[1].strip())    

    i += 1

hands1 = sorted(hands1.items())
hands2 = sorted(hands2.items())

for hand in hands1:
    winnings1 += hand[1]*j
    j += 1

j = 1

for hand in hands2:
    winnings2 += hand[1]*j
    j += 1

print(winnings1)
print(winnings2)