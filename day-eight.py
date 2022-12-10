import numpy as np

def isVisible(target_tree, tree_line):
    for tree in tree_line:
        if tree >= target_tree:
            return False
    return True

def getPartOneSolution(grid):
    grid = np.array(grid)
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

def getInput(path):
    def convertStrGridToIntGrid(grid):
        i_grid = []
        for row in grid:
            i_row = []
            for c in row:
                if c != '\n':
                    i_row.append(int(c))
            i_grid.append(i_row)
        return i_grid
            

    f = open(path)
    grid = f.readlines()
    grid = convertStrGridToIntGrid(grid)
    return grid

def main():
    """ Tests """
    grid = getInput('data/day-8-test.txt')
    res = getPartOneSolution(grid)
    assert res == 21, 'Part one test is incorrect'

    """ Solutions """
    grid = getInput('data/day-8.txt')
    res = getPartOneSolution(grid)
    print('Part one solution: {}'.format(res))
    assert res == 1533, 'Part one is incorrect'

    return 0

if __name__ == '__main__':
    main()