
class TreeNode:
    def __init__(self, val: int, x: int, y: int) -> None:
        self.val = val
        self.nodes = []
        self.x = x
        self.y = y

def solvePartOne(grid):

    return 0

""" Load data functions """

def convertCharToInt(c):
    if c == 'S':
        return 1
    elif c == 'Z':
        return 26
    n = ord(c) - 96
    return 0

def appendTreeNode(parent_node: TreeNode, node_val: int, x: int, y: int, que):
    # TODO: Make sure you don't add parent node
    if parent_node.val - node_val > 1:
        return
    node = TreeNode(node_val, x, y)
    parent_node.nodes.append(node)
    que.append(node)

def createTree(grid):
    root_node = TreeNode(grid[0][0], 0, 0)
    que = [root_node]

    while len(que) > 0:
        node = que[0]
        que.pop(0)
        x, y = node.x, node.y

        if x > 0:
            left_val = grid[y][x-1]
            appendTreeNode(node, left_val, x, y, que)
        if x < len(grid[y]):
            right_val = grid[y][x+1]
            appendTreeNode(node, right_val, x, y, que)
        if y > 0:
            up_val = grid[y-1][x]
            appendTreeNode(node, up_val, x, y, que)
        if y < len(grid):
            down_val = grid[y+1][x]
            appendTreeNode(node, down_val, x, y, que)


        continue

    return 0

def getInput(path):
    with open(path) as f:
        lines = f.readlines()
    grid = [c for line in lines for c in line]
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