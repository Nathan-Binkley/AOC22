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
    pass

print("Part 1: ", part1())

def part2():
    pass

print("Part 2: ", part2())