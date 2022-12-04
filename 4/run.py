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
    elf_pairs = 0
    for pair in lines:
        elf = pair.split(",") 
        start = int(elf[0].split("-")[0])
        end = int(elf[0].split("-")[1])
        start2 = int(elf[1].split("-")[0])
        end2 = int(elf[1].split("-")[1])
        if (start2 <= start and end2 >= end) or (start <= start2 and end >= end2):
            elf_pairs += 1

    return elf_pairs

print("Part 1: ", part1())

def part2():
    elf_pairs = 0
    for pair in lines:
        elf = pair.split(",") 
        start = int(elf[0].split("-")[0])
        end = int(elf[0].split("-")[1])
        start2 = int(elf[1].split("-")[0])
        end2 = int(elf[1].split("-")[1])
        print(elf)
        if start <= end2 and end >= start2:
            print("OVERLAP")
            elf_pairs += 1

    return elf_pairs
    
    

print("Part 2: ", part2())