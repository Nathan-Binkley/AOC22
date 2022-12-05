import re

lines = []
with open("input.txt", "r") as f:
    l = f.readline()
    while l:
        try:
            lines.append(l.rstrip())
        except:
            lines.append(l)
        l = f.readline()

def reset_cases(): 
    global cases
    cases = {
        1: "ZJNWPS",
        2: "GST",
        3: "VQRLH",
        4: "VSTD",
        5: "QZTDBMJ",
        6: "MWTJDCZL",
        7: "LPMWGTJ",
        8: "NGMTBFQH",
        9: "RDGCPBQW"
    }

reset_cases()

def part1():
    for i, line in enumerate(lines):
        numbers = re.findall(r'\d+', line)
        amount = int(numbers[0])
        start = int(numbers[1])
        end = int(numbers[2])
        for i in range(amount):
            temp = cases[start][-1:]
            cases[end] = cases[end] + temp
            cases[start] = cases[start][:-1]
        # if i == 2:
        #     break
    final_string = ""
    for i in range(9):
        final_string += cases[i+1][-1]
    return final_string

print("Part 1: ", part1())

# NOT NTTBGBTBT
 # NOT WSSDHLJTW
reset_cases()

def part2():
    for i, line in enumerate(lines):
        numbers = re.findall(r'\d+', line)
        amount = int(numbers[0])
        start = int(numbers[1])
        end = int(numbers[2])
        
        temp = cases[start][-amount:]
        cases[end] = cases[end] + temp
        cases[start] = cases[start][:-amount]
        
    final_string = ""
    for i in range(9):
        final_string += cases[i+1][-1]
    return final_string
    
# NOT NTTBGBTBT
# NOT WSSDHLJTW
reset_cases()    

print("Part 2: ", part2())