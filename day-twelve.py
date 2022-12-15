
class TreeNode:
    def __init__(self, val: int, x: int, y: int, parent) -> None:
        self.val = val
        self.nodes = []
        self.x = x
        self.y = y
        self.parent = parent

def traverseTree(node, target_val)

def solvePartOne(grid):

    return 0

""" Load data functions """

def isVisited(node: TreeNode, x, y):
    while node is not None:
        if node.x == x and node.y == y:
            return True
        node = node.parent
    return False

def convertCharToInt(c):
    if c == 'S':
        return 1
    elif c == 'Z':
        return 26
    n = ord(c) - 96
    return n

def appendTreeNode(parent_node: TreeNode, node_val: int, x: int, y: int, que):
    if isVisited(parent_node, x, y) or \
        parent_node.val - node_val < -1:
        return
    node = TreeNode(node_val, x, y, parent_node)
    parent_node.nodes.append(node)
    que.append(node)

def createTree(grid):
    # TODO: NEED TO HANDLE EXIT NODE
    root_node = TreeNode(1, 0, 0, None)
    que = [root_node]

    while len(que) > 0:
        node = que[0]
        que.pop(0)
        x, y = node.x, node.y

        if x > 0:
            left_val = convertCharToInt(grid[y][x-1])
            appendTreeNode(node, left_val, x-1, y, que)
        if x < len(grid[y]) - 1:
            right_val = convertCharToInt(grid[y][x+1])
            appendTreeNode(node, right_val, x+1, y, que)
        if y > 0:
            up_val = convertCharToInt(grid[y-1][x])
            appendTreeNode(node, up_val, x, y-1, que)
        if y < len(grid) - 1:
            down_val = convertCharToInt(grid[y+1][x])
            appendTreeNode(node, down_val, x, y+1, que)

    return root_node

def getInput(path):
    with open(path) as f:
        lines = f.readlines()
    grid = []
    for line in lines:
        grid.append([c for c in line if c != '\n'])
    return createTree(grid)

""" Main """

def main():
    """ Tests """
    grid = getInput('data/day-12-test.txt')
    res = solvePartOne(grid)
    assert res == 31, 'Part one test is incorrect, \
                        is {} but should be 31'.format(res)

    """ Solutions """
    grid = getInput('data/day-12-test.txt')
    res = solvePartOne(grid)
    print('Part one solution: {}'.format(res))

    return 0

if __name__ == '__main__':
    main()