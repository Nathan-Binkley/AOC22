lines = []
with open("input.txt", "r") as f:
    l = f.readline()
    while l:
        try:
            lines.append(l.rstrip())
        except:
            lines.append(l)
        l = f.readline()

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
def part1():
    priority = 0
    for i in lines:
        first_half = i[:len(i) // 2]
        second_half = i[len(i) // 2:]
        for j in first_half:
            if j in second_half:
                priority += letters.index(j) + 1
                break

    return priority

                

print("Part 1: ", part1())

def part2():
    group = []
    priority = 0
    for i in lines:
        if len(group) < 3:
            group.append(i)
        if len(group) == 3:
            for letter in group[0]:
                if letter in group[1] and letter in group[2]:
                    priority += letters.index(letter) + 1
                    break
            group = []
    return priority
        
    

print("Part 2: ", part2())