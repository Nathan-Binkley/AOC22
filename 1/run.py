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
    elves = []
    val = 0
    for i in lines:
        if i:
            val += int(i)
        else:
            elves.append(val)
            val = 0
    return max(elves)

print("Part 1: ", part1())

def part2():
    elves = []
    val = 0
    for i in lines:
        if i:
            val += int(i)
        else:
            elves.append(val)
            val = 0
    return sum(sorted(elves)[-3:])

print("Part 2: ", part2())