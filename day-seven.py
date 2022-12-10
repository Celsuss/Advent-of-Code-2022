
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
            # print('Added node {}'.format(dir_node._name))

        elif line[:4] == '$ ls':
            # List directory content
            files, dirs, i = parseLsCommand(log, i+1)
            stack[-1]._files = files
            # stack[-1]._dirs = dirs

    return root_node, dirs_que

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
    root_node, dirs_que = getDirStructure(log)
    
    size_sum = 0
    for node in dirs_que:
        dir_size = getDirectoryNodeSum(node)
        if dir_size <= size_limit:
            size_sum += dir_size

        continue

    return size_sum

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
    print('Part one solution: {}'.format(res))

    return 0

if __name__ == '__main__':
    main()