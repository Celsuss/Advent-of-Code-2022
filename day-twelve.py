
class TreeNode:
    def __init__(self, val: int, x: int, y: int, parent, is_target=False) -> None:
        self.val = val
        self.nodes = []
        self.x = x
        self.y = y
        self.parent = parent
        self.is_target = is_target

def traverseTree(node: TreeNode, steps: int, shortest_path: int):
    if node.is_target is True and \
        (steps < shortest_path or shortest_path == -1):
        shortest_path = steps
        return shortest_path

    for s_n in node.nodes:
        shortest_path = traverseTree(s_n, steps+1, shortest_path)

    return shortest_path

def aStar(grid):

    return 0

def solvePartOne(root_node):
    steps = traverseTree(root_node, 0, -1)

    return steps

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
    elif c == 'E':
        return 26
    n = ord(c) - 96
    return n

def appendTreeNode(parent_node: TreeNode, node_val: int, x: int, y: int, que, is_final):
    if isVisited(parent_node, x, y) or \
        parent_node.val - node_val < -1:
        return
    node = TreeNode(node_val, x, y, parent_node, is_final)
    parent_node.nodes.append(node)
    que.append(node)

def createTree(grid):
    # def inspectNode(x, y, node, que):
    #     is_final = True if grid[y][x-1] == 'E' else False
    #     val = convertCharToInt(grid[y][x])
    #     appendTreeNode(node, val, x, y, que, is_final)

    root_node = TreeNode(1, 0, 0, None)
    que = [root_node]

    while len(que) > 0:
        node = que[0]
        que.pop(0)
        x, y = node.x, node.y

        if x > 0:
            is_final = True if grid[y][x-1] == 'E' else False
            left_val = convertCharToInt(grid[y][x-1])
            appendTreeNode(node, left_val, x-1, y, que, is_final)
        if x < len(grid[y]) - 1:
            is_final = True if grid[y][x+1] == 'E' else False
            right_val = convertCharToInt(grid[y][x+1])
            appendTreeNode(node, right_val, x+1, y, que, is_final)
        if y > 0:
            is_final = True if grid[y-1][x] == 'E' else False
            up_val = convertCharToInt(grid[y-1][x])
            appendTreeNode(node, up_val, x, y-1, que, is_final)
        if y < len(grid) - 1:
            is_final = True if grid[y+1][x] == 'E' else False
            down_val = convertCharToInt(grid[y+1][x])
            appendTreeNode(node, down_val, x, y+1, que, is_final)

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
    root_node = getInput('data/day-12-test.txt')
    res = solvePartOne(root_node)
    assert res == 31, 'Part one test is incorrect, \
                        is {} but should be 31'.format(res)

    """ Solutions """
    grid = getInput('data/day-12.txt')
    res = solvePartOne(grid)
    print('Part one solution: {}'.format(res))

    return 0

if __name__ == '__main__':
    main()