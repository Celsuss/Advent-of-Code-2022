
class Node:
    def __init__(self, pos: tuple(int, int)) -> None:
        self.pos = pos
        self.G = None
        self.H = None
        self.F = None

def isAccessible(current: int, target: int) -> bool:
    if target - current <= 1:
        return True
    return False

def getG(parent_node: Node) -> int:
    """ g = move cost from starting node to node """
    return parent_node.g + 1

def getH(node_pos: tuple(int, int), target_pos: tuple(int, int)) -> int:
    """ h = estimate cost from node to target node (manhattan distance) """
    return (target_pos[0] - node_pos[0]) + (target_pos[1] - node_pos[1])

def getF(g: int, h: int) -> int:
    """ f = sum(g, h)"""
    return g + h

def getNextNode(open_list: list[list[Node]]):
    """ Return node with lowest F Cost """

def aStar(grid: list[list[chr]], start: tuple(int, int), target: tuple(int, int)):
    """
    A*
    1. Get node N with lowest F score in open list
    2. Remove node N from open list
    3. For each neighbor to node N
        3.1. If neighbor is target then stop
        3.2. Calculate G, H, F for neighbor
        3.3. Ignore if neighbor already exists with lower F score in open or closed
        3.4. Add neighbor to open list
    4. Push node N to closed list
    """
    open_list = [grid[start[0]][start[1]]]
    closed_list = []

    while len(open_list) > 0:
        node = open_list.pop(0)


        continue

    return 0

def solvePartOne(grid, start, target):
    return aStar(grid, start, target)

""" Load data functions """

def convertCharToInt(c):
    if c == 'S':
        return 1
    elif c == 'E':
        return 26
    n = ord(c) - 96
    return n

def getGridFromInput(lines):
    grid = []
    for line in lines:
        grid_row = []
        for c in line:
            grid_row.append(convertCharToInt(c))
        grid.append(grid_row)

    return grid

def getStartAndTarget(lines):
    start = None
    target = None

    for i in range(len(lines)):
        line = lines[i]
        for j in range(len(line)):
            c = line[j]
            if c == 'S':
                start = (i, j)
            elif c == 'E':
                target = (i, j)

    return start, target

def getInput(path):
    with open(path) as f:
        lines = f.readlines()

    lines = [line[:-1] if '\n' in line else line for line in lines]     # Remove '\n'
    grid = getGridFromInput(lines)
    start, target = getStartAndTarget(lines)
    return grid, start, target

""" Main """

def main():
    """ Tests """
    grid, start, target = getInput('data/day-12-test.txt')
    res = solvePartOne(grid, start, target)
    assert res == 31, 'Part one test is incorrect, \
                        is {} but should be 31'.format(res)

    """ Solutions """
    grid = getInput('data/day-12-test.txt')
    res = solvePartOne(grid)
    print('Part one solution: {}'.format(res))

    return 0

if __name__ == '__main__':
    main()