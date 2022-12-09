
class Dir_node:
    def __init__(self, name) -> None:
        self._name = name
        self._dirs = []
        self._files = []

def getDirStructure(log):
    def parseLsCommand(log, i):
        line = log[i]
        files = []
        dirs = []
        while line[0] != '$' and i < len(log):
            if line[:3] == 'dir':
                dirs.append(line[4:-1])
            else:
                files.append(line.split('\n')[0])
            i = i+1
            if i < len(log):
                line = log[i]
        return files, dirs, i-1

    # TODO: Remove stack?
    stack = []
    dirs_dict = {}

    for i in range(len(log)):
        line = log[i]
        if line[:7] == '$ cd ..':
            stack.pop()
        elif line[:8] == '$ cd /':
            stack = [stack[0]]
        elif line[:4] == '$ cd':
            # Enter directory
            stack.append(Dir_node(line[5:-1]))
            dirs_dict[line[5:-1]] = stack[-1]
        elif line[:4] == '$ ls':
            # List directory content
            files, dirs, i = parseLsCommand(log, i+1)
            stack[-1]._files = files
            stack[-1]._dirs = dirs

    return dirs_dict

def getDirectoryFilesSizeSum(files):
    size_sum = 0
    for file in files:
        size = int(file.split(' ')[0])
        size_sum += size
    return size_sum

def getDirectorySum(dirs_dict, directory):
    files_size = getDirectoryFilesSizeSum(directory._files)
    dirs_size = 0
    for dir_name in directory._dirs:
        dirs_size += getDirectorySum(dirs_dict, dirs_dict[dir_name])

    return files_size + dirs_size

def getDirectoriesSum(dirs_dict, size_limit):
    total_sum = 0
    for key in dirs_dict:
        d = dirs_dict[key]
        dir_sum = getDirectorySum(dirs_dict, d)
        if dir_sum <= size_limit:
            total_sum += dir_sum

    return total_sum

def getPartOneSolution(log):
    dirs_dict = getDirStructure(log)
    dirs_sum = getDirectoriesSum(dirs_dict, 100000)
    return dirs_sum

def getInput(path):
    f = open(path)
    return f.readlines()

def main():
    """ Tests """
    log = getInput('data/day-7-test.txt')
    res = getPartOneSolution(log)
    assert(res == 95437)


    """ Solutions """
    log = getInput('data/day-7.txt')
    res = getPartOneSolution(log)
    assert(res > 1587563)
    print('Part one solution: {}'.format(res))  # 1587563 too low

    return 0

if __name__ == '__main__':
    main()