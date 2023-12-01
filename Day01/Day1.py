def process_text(text):
    lines = text.readlines()
    combined_text = "0"
    combined_number = 0
    combined_text_replaced = "0"
    combined_number_replaced = 0
    for line in lines:
        first, last = find_numbers(line)
        combined_text = first+last
        combined_number += int(combined_text)

        line = line.replace("one", "o1e")
        line = line.replace("two", "t2o")
        line = line.replace("three", "t3e")
        line = line.replace("four", "f4r")
        line = line.replace("five", "f5e")
        line = line.replace("six", "s6x")
        line = line.replace("seven", "s7n")
        line = line.replace("eight", "e8t")
        line = line.replace("nine", "n9e")
        first, last = find_numbers(line)
        combined_text_replaced = first+last
        combined_number_replaced += int(combined_text_replaced)
    print(combined_number)
    print(combined_number_replaced)

def is_number(char):
  return char.isdigit()

def find_numbers(line):
    first = None
    last = None
    char = ""
    for i in range(len(line)): 
        if is_number(line[i]):
            if first == None:
                first = line[i] 
            last = line[i]
    if first == None:
        first = "0"
    if last == None:
        last = first
    return first, last 

input = open("Day01/input")
process_text(input)