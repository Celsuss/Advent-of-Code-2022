
class DirNode:
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

    root_node = None
    stack = []
    dirs_que = []

    for i in range(len(log)):
        line = log[i]
        if line == '$ cd /\n':
            root_node = DirNode('/')
            stack = [root_node]
            dirs_que.append(root_node)

        elif line[:7] == '$ cd ..':
            stack.pop()
            
        elif line[:4] == '$ cd':
            dir_node = DirNode(line[5:-1]) 
            stack[-1]._dirs.append(dir_node)
            stack.append(dir_node)
            dirs_que.append(dir_node)

        elif line[:4] == '$ ls':
            files, dirs, i = parseLsCommand(log, i+1)
            stack[-1]._files = files

    return dirs_que

def getDirectoryFilesSizeSum(files):
    size_sum = 0
    for file in files:
        size = int(file.split(' ')[0])
        size_sum += size
    return size_sum

def getDirectoryNodeSum(node):
    files_sum = getDirectoryFilesSizeSum(node._files)
    dir_sum = 0
    for d in node._dirs:
        dir_sum += getDirectoryNodeSum(d)
    
    total_sum = files_sum + dir_sum
    return total_sum

def getPartOneSolution(log):
    size_limit = 100000
    dirs_que = getDirStructure(log)
    
    size_sum = 0
    for node in dirs_que:
        dir_size = getDirectoryNodeSum(node)
        if dir_size <= size_limit:
            size_sum += dir_size

    return size_sum

def getPartTwoSolution(log):
    dirs_que = getDirStructure(log)
    total_size = 70000000
    needed_size = 30000000
    used_size = getDirectoryNodeSum(dirs_que[0])
    target_size = needed_size - (total_size - used_size)

    target_dir_size = None

    for node in dirs_que:
        size = getDirectoryNodeSum(node)
        if size >= target_size and \
            (target_dir_size is None or size < target_dir_size):
            target_dir_size = size

        continue
    return target_dir_size

def getInput(path):
    f = open(path)
    return f.readlines()

def main():
    """ Tests """
    log = getInput('data/day-7-test.txt')
    res = getPartOneSolution(log)
    assert res == 95437, 'Part one test is incorrect'
    res = getPartTwoSolution(log)
    assert res == 24933642, 'Part two test is incorrect'


    """ Solutions """
    log = getInput('data/day-7.txt')
    res = getPartOneSolution(log)
    print('Part one solution: {}'.format(res))
    assert res == 1844187, 'Part one solution is incorrect'
    res = getPartTwoSolution(log)
    print('Part two solution: {}'.format(res))

    return 0

if __name__ == '__main__':
    main()