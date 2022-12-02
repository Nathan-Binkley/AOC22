lines = []
with open("input.txt", "r") as f:
    l = f.readline()
    while l:
        try:
            lines.append(l.rstrip())
        except:
            lines.append(l)
        l = f.readline()

# rock == A X
# paper == B Y
# scissors == C Z

def is_winner(a, b):
    if a == "A" and b == "Y":
        return True
    if a == "B" and b == "Z":
        return True
    if a == "C" and b == "X":
        return True
    return False

def is_draw(a, b):
    if a == "A" and b == "X":
        return True
    if a == "B" and b == "Y":
        return True
    if a == "C" and b == "Z":
        return True
    return False

def part1():
    score = 0
    for i in lines:
        vals = i.split(" ")
        if is_draw(vals[0], vals[1]):
            score += 3
        elif is_winner(vals[0], vals[1]):
            score += 6 # 6 if winner
        else:
            score += 0
        if vals[1] == "Y":
            score += 2
        if vals[1] == "Z":
            score += 3
        if vals[1] == "X":
            score += 1
    return score

print("Part 1: ", part1())

def part2():
    score = 0
    for i in lines:
        vals = i.split(" ")
        if vals[1] == "X":
            score += 0 # loss
            if vals[0] == "A":
                score += 3
            if vals[0] == "B":
                score += 1
            if vals[0] == "C":
                score += 2
            
            
        if vals[1] == "Y":
            score += 3 # draw
            if vals[0] == "A":
                score += 1
            if vals[0] == "B":
                score += 2
            if vals[0] == "C":
                score += 3

        if vals[1] == "Z":
            score += 6 # win
            if vals[0] == "A":
                score += 2
            if vals[0] == "B":
                score += 3 
            if vals[0] == "C":
                score += 1
        print("Score: ", score, vals)
        
    return score

print("Part 2: ", part2())