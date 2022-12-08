lines = []
with open("input.txt", "r") as f:
    l = f.readline()
    while l:
        try:
            lines.append(l.rstrip())
        except:
            lines.append(l)
        l = f.readline()

max_size = 100000

class Directory:
    def __init__(self, name):
        self.name = name
        self.children = []

    def get_name(self):
        return self.name

    def add_child(self, child):
        self.children.append(child)

    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None
    
    def get_all_children(self):
        return [child for child in self.children]

    def get_size(self):
        size = 0
        for child in self.children:
            size += child.get_size()
        return size

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.children = []

    def get_size(self):
        return self.size
    
    def get_name(self):
        return self.name

    def get_children(self):
        return self.children


    

def part1():

    current_directory_path = []
    directories = []
    files = []

    current_directory = None
    root = Directory("/")
    current_directory_path.append(root)
    directories.append(root)
    current_directory = root

    for line in lines: # Build the tree
        directory = None
        items = line.split(" ")

        if items[1] == "ls": #listing directory
            continue           

        elif items[0] == "dir": #Listing Directory
            directory = Directory(items[1])
            directories.append(directory)
            current_directory.add_child(directory)
            
        elif items[1] == "cd": # Changing Directory
            if items[2] == "..":
                current_directory_path.pop()
                current_directory = current_directory_path[-1]
            else: # change directory
                directory = current_directory.get_child(items[2])
                current_directory_path.append(directory)
                current_directory = directory

        else: # is file
            file = File(items[1], int(items[0]))
            current_directory.add_child(file)
            files.append(file)

    directory_sizes = []
    for directory in directories:
        directory_sizes.append(directory.get_size())

    directory_sizes.sort()
    sum = 0
    for i in directory_sizes:
        if i <= max_size:
            sum += i
    return sum

print("Part 1: ", part1())


def part2():

    current_directory_path = []
    directories = []
    files = []

    current_directory = None
    root = Directory("/")
    current_directory_path.append(root)
    directories.append(root)
    current_directory = root

    for line in lines: # Build the tree
        directory = None
        items = line.split(" ")

        if items[1] == "ls": #listing directory
            continue           

        elif items[0] == "dir": #Listing Directory
            directory = Directory(items[1])
            directories.append(directory)
            current_directory.add_child(directory)
            
        elif items[1] == "cd": # Changing Directory
            if items[2] == "..":
                current_directory_path.pop()
                current_directory = current_directory_path[-1]
            else: # change directory
                directory = current_directory.get_child(items[2])
                current_directory_path.append(directory)
                current_directory = directory

        else: # is file
            file = File(items[1], int(items[0]))
            current_directory.add_child(file)
            files.append(file)

    directory_sizes = []
    for directory in directories:
        directory_sizes.append(directory.get_size())

    directory_sizes.sort()
    used_space = 0
    for i in files:
        used_space += i.get_size()

    unused_space = part_2_max_size - used_space

    for i in directory_sizes:
        if unused_space + i >= part_2_min_size:
            return i
    

part_2_min_size = 30000000 # diff needs to be greater than this
part_2_max_size = 70000000 # max size on disk

print("Part 2: ", part2())

