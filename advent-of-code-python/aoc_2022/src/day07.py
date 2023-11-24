with open('../test/resources/day07.txt') as f:
    lines = f.readlines()


# PART 1
class File:
    def __init__(self, size: int, name: str) -> None:
        self.size: int = size
        self.name: str = name


class Directory:
    def __init__(self, name, parent) -> None:
        self.name: str = name
        self.parent: Directory = parent
        self.children: [Directory] = []
        self.files: [File] = []

    def cd_up(self):
        return self.parent

    def cd(self, child_name: str):
        for dir in self.children:
            if child_name == dir.name:
                return dir
        return Directory(child_name, self)

    def touch(self, size: int, name: str) -> None:
        self.files.append(File(size, name))

    def mkdir(self, name: str):
        self.children.append(Directory(name, self))

    def du(self, sum_threshold:int = 1_000_000_000_000) -> int:
        total = 0
        for file in self.files:
            total += file.size
        if self.children:
            for dir in self.children:
                total += dir.du()
        return total

    def get_sub_directories(self) -> []:
        sub_dirs: [Directory] = []
        if self.children:
            sub_dirs.extend(self.children)
            for dir in self.children:
                sub_dirs.extend(dir.get_sub_directories())
        return sub_dirs

    def get_root(self):
        if self.name == '/':
            return self
        parent = self.parent
        while parent:
            if parent.parent:
                parent = parent.parent
            else:
                break
        return parent


    def __repr__(self):
        return f'Dir:{self.name}, Size: {self.du()}'


def build_file_tree() -> Directory:
    current: Directory = Directory('/', None)
    for line in lines:
        if line.startswith("$"):
            line = line[2:]
            if line.startswith('cd'):
                line = line.split()
                if line[1] == '..':
                    current = current.cd_up()
                elif line[1] == '/':
                    current = current.get_root()
                else:
                    current = current.cd(line[1])
            elif line.startswith('ls'):
                continue
        else:
            if line.startswith('dir'):
                current.mkdir(line.split()[1])
            else:
                size, name = line.split()
                current.touch(int(size), name)
    return current.get_root()

dir1 = Directory('/', None)
dir_a = Directory('a', dir1)
dir_b = Directory('b', dir_a)
dir1.children = [dir_a]
dir_a.children = [dir_b]
assert '/' == dir_a.parent.name
assert dir1.cd('a') == dir_a

dir1.touch(10, 'a')
dir1.touch(2, 'b')
assert dir1.du() == 12
dir_a.touch(5, 'c')
assert dir1.du() == 17

root_dir = build_file_tree()
print(root_dir)
print(root_dir.du())

total = 0
for dir in root_dir.get_sub_directories():
    dir_size = dir.du()
    if dir_size < 100_000:
        total += dir_size
print(f'PART 1: {total}')

#PART 2
minimal_to_delete = root_dir.du() - 40_000_000
print(minimal_to_delete)
dirs_to_delete: [int] = []
for dir in root_dir.get_sub_directories():
    dir_size = dir.du()
    if dir_size > minimal_to_delete:
        dirs_to_delete.append(dir_size)
print(f'PART 2: {min(dirs_to_delete)}')