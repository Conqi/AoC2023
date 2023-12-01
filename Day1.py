def process_text(text):
    #lines = text.split("\n")
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
        line = line.replace("three", "3")
        line = line.replace("four", "4")
        line = line.replace("five", "5")
        line = line.replace("six", "6")
        line = line.replace("seven", "7n")
        line = line.replace("eight", "8t")
        line = line.replace("nine", "9")
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
    if last == None:
        last = first
    return first, last 

input = open("input")
process_text(input)