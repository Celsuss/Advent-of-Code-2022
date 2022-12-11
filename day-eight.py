import numpy as np

def isVisible(target_tree, tree_line):
    for tree in tree_line:
        if tree >= target_tree:
            return False
    return True

def getPartOneSolution(grid):
    n_exterior_visible_trees = 0

    """ Get exterior trees """
    n_exterior_visible_trees += grid[0,1:-1].shape[0]
    n_exterior_visible_trees += grid[-1,1:-1].shape[0]
    n_exterior_visible_trees += grid[:,0].shape[0]
    n_exterior_visible_trees += grid[:,-1].shape[0]

    """ Get N visible interior trees """
    n_interior_visible_trees = 0
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[i])-1):
            node = grid[i][j]
            if node > 0 and \
                (isVisible(node, grid[i,:j]) or \
                isVisible(node, grid[i,j+1:]) or \
                isVisible(node, grid[:i,j]) or \
                isVisible(node, grid[i+1:,j])):
                n_interior_visible_trees += 1

    return n_exterior_visible_trees + n_interior_visible_trees

def getViewDistance(target_tree, tree_line):
    for i in range(len(tree_line)):
        if tree_line[i] >= target_tree:
            break
    return i+1

def getScenicScore(grid, i, j):
    node = grid[i][j]
    left_view_distance = getViewDistance(node, np.flip(grid[i,:j]))
    right_view_distance = getViewDistance(node, grid[i,j+1:])
    up_view_distance = getViewDistance(node, np.flip(grid[:i,j]))
    down_view_distance = getViewDistance(node, grid[i+1:,j])

    return left_view_distance * right_view_distance * up_view_distance * down_view_distance

def getPartTwoSolution(grid):
    best_scenic_score = 0

    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[i])-1):
            scenic_score = getScenicScore(grid, i, j)
            if scenic_score > best_scenic_score:
                best_scenic_score = scenic_score

    return best_scenic_score

def getInput(path):
    def convertStrGridToIntGrid(grid):
        i_grid = []
        for row in grid:
            i_row = []
            for c in row:
                if c != '\n':
                    i_row.append(int(c))
            i_grid.append(i_row)
        return np.array(i_grid)
            

    f = open(path)
    grid = f.readlines()
    grid = convertStrGridToIntGrid(grid)
    return grid

def main():
    """ Tests """
    grid = getInput('data/day-8-test.txt')
    res = getPartOneSolution(grid)
    assert res == 21, 'Part one test is incorrect'
    res = getPartTwoSolution(grid)
    assert res == 8, 'Part two test is incorrect'

    """ Solutions """
    grid = getInput('data/day-8.txt')
    res = getPartOneSolution(grid)
    print('Part one solution: {}'.format(res))
    assert res == 1533, 'Part one is incorrect'
    res = getPartTwoSolution(grid)
    print('Part two solution: {}'.format(res))

    return 0

if __name__ == '__main__':
    main()