
posTuple = tuple((int, int))
chrGrid = list[list[chr]]

class Node:
    def __init__(self, pos: posTuple, height: int) -> None:
        self.pos = pos
        self.height = height
        self.g = 0
        self.h = 0
        self.f = 0

nodeList = list[Node]

def getHeight(pos: posTuple, grid: chrGrid):
    return grid[pos[1]][pos[0]]

def isAccessible(current: int, target: int) -> bool:
    if target - current <= 1:
        return True
    return False

def getG(parent_node: Node) -> int:
    """ g = move cost from starting node to node """
    return parent_node.g + 1

def getH(node_pos: posTuple, target_pos: posTuple) -> int:
    """ h = estimate cost from node to target node (manhattan distance) """
    return abs(node_pos[0] - target_pos[0]) + abs(node_pos[1] - target_pos[1])

def getF(node: Node) -> int:
    """ f = sum(g, h)"""
    return node.g + node.h

def addNeighbors(pos: posTuple, height: int, grid: chrGrid) -> nodeList:
    """ Return node with lowest F Cost """
    neighbors = []
    top_n_pos = (pos[0], pos[1]-1)
    right_n_pos = (pos[0]+1, pos[1])
    bot_n_pos = (pos[0], pos[1]+1)
    left_n_pos = (pos[0]-1, pos[1])

    if top_n_pos[1] >= 0 and \
        isAccessible(height, getHeight(top_n_pos, grid)):
        neighbors.append(Node(top_n_pos, getHeight(top_n_pos, grid)))

    if right_n_pos[0] <= len(grid[0])-1 and \
        isAccessible(height, getHeight(right_n_pos, grid)):
        neighbors.append(Node(right_n_pos, getHeight(right_n_pos, grid)))

    if bot_n_pos[1] <= len(grid)-1 and \
        isAccessible(height, getHeight(bot_n_pos, grid)):
        neighbors.append(Node(bot_n_pos, getHeight(bot_n_pos, grid)))

    if left_n_pos[0] >= 0 and \
        isAccessible(height, getHeight(left_n_pos, grid)):
        neighbors.append(Node(left_n_pos, getHeight(left_n_pos, grid)))

    return neighbors

def getNodeWithLowerFScore(nodes: nodeList, node: Node):
    for n in nodes:
        if n.pos == node.pos:
            if n.f <= node.f:
                return n
            else:
                break
    return None

def getLowestFScoreNode(nodes: nodeList):
    """ Return node with lowest F Score """
    if len(nodes) == 0:
        return None
    res = nodes[0]
    for node in nodes[1:]:
        if node.f < res.f:
            res = node
    return res

def aStar(grid: chrGrid, start: posTuple, target: posTuple):
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
    start_node = Node(start, getHeight(start, grid))
    open_list = [start_node]
    closed_list = []

    while len(open_list) > 0:
        node = getLowestFScoreNode(open_list)
        open_list.remove(node)
        neighbors = addNeighbors(node.pos, node.height, grid)
        for neighbor in neighbors:
            if neighbor.pos == target:
                return node.g + 1

            neighbor.g = getG(node)
            neighbor.h = getH(node.pos, target)
            neighbor.f = getF(neighbor)
            if getNodeWithLowerFScore(open_list, neighbor) is None and \
                getNodeWithLowerFScore(closed_list, neighbor) is None:
                open_list.append(neighbor)

        closed_list.append(node)

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
                start = (j, i)
            elif c == 'E':
                target = (j, i)

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
    grid, start, target = getInput('data/day-12.txt')
    res = solvePartOne(grid, start, target)
    print('Part one solution: {}'.format(res))
    assert res == 504, 'Part one is incorrect, \
                        is {} but should be 504'.format(res)

    return 0

if __name__ == '__main__':
    main()