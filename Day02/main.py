solution1 = 0
solution2 = 0

for id, lines in enumerate(open("input")):
    lines = lines.strip("\n")
    game_number, draw = lines.split(":")
    ok = True
    power = 0
    red_max = 0
    green_max = 0
    blue_max = 0
    for single_draw in draw.split(";"):
        for ball_draw in single_draw.split(","):
            amount,color = ball_draw.split()
            if (color == "red" and int(amount)>red_max):
            	red_max = int(amount)
            elif (color == "green" and int(amount)>green_max):
            	green_max = int(amount)
            elif (color == "blue" and int(amount)>blue_max):
            	blue_max = int(amount)
            if (color == "red" and int(amount)>12) or (color == "green" and int(amount)>13) or (color == "blue" and int(amount)>14):
            	ok = False
    if ok == True:
	    solution1 += id+1
    power = red_max*green_max*blue_max
    solution2 += power
        		        		
print(solution1)
print(solution2)
