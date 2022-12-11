
def getPartOneSolution(moves):

    return 0

def getInput(path):
    moves = []
    f = open(path)
    lines = f.readlines()
    for line in lines:
        direction, length = line.split(' ')
        moves.append((direction, int(length)))
    return moves

def main():
    """ Tests """
    moves = getInput('data/day-9-test.txt')
    res = getPartOneSolution(moves)
    assert res == 13, 'Part one test is incorrect'

    """ Solutions """
    moves = getInput('data/day-9.txt')
    res = getPartOneSolution(moves)
    print('Part one solution: {}'.format(res))

    return 0

if __name__ == '__main__':
    main()