
lines = []
with open("input.txt", "r") as f:
    l = f.readline()
    while l:
        try:
            lines.append(l.rstrip())
        except:
            lines.append(l)
        l = f.readline()


def part1():
    string = lines[0]
    last_four = []
    for count, letter in enumerate(string):
        last_four.append(letter)
        if len(last_four) > 4:
            last_four.pop(0)
        if len(last_four) == 4:
            if not (last_four.count(last_four[0]) > 1 \
            or last_four.count(last_four[1]) > 1 \
            or last_four.count(last_four[2]) > 1 \
            or last_four.count(last_four[3]) > 1) \
            and len(set(last_four)) == 4:
                return count + 1
    

print("Part 1: ", part1())


def part2():
    string = lines[0]
    last_four = []
    for count, letter in enumerate(string):
        last_four.append(letter)
        print(last_four)
        if len(last_four) > 14:
            last_four.pop(0)
        if len(last_four) == 14:
            
            if not (last_four.count(last_four[0]) > 1 \
            or last_four.count(last_four[1]) > 1 \
            or last_four.count(last_four[2]) > 1 \
            or last_four.count(last_four[3]) > 1 \
            or last_four.count(last_four[4]) > 1 \
            or last_four.count(last_four[5]) > 1 \
            or last_four.count(last_four[6]) > 1 \
            or last_four.count(last_four[7]) > 1 \
            or last_four.count(last_four[8]) > 1 \
            or last_four.count(last_four[9]) > 1 \
            or last_four.count(last_four[10]) > 1 \
            or last_four.count(last_four[11]) > 1 \
            or last_four.count(last_four[12]) > 1 \
            or last_four.count(last_four[13]) > 1) \
            and len(set(last_four)) >= 14:
                return count + 1

    return -1

print("Part 2: ", part2())