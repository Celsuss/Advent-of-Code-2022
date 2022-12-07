

def isUnique(stack):
    chars = set()
    for c in stack:
        if c in chars:
            return False
        chars.add(c)

    return True

def getIndexOfFirstNRepeating(buffer_full, n):
    buffer = buffer_full[:n]
    for i in range(n, len(buffer_full)):
        if isUnique(buffer):
            return i

        buffer = buffer[1:]
        buffer = buffer + buffer_full[i]

    return 0

def getPartOneSolution(buffer):
    return getIndexOfFirstNRepeating(buffer, 4)

def getPartTwoSolution(buffer):
    return getIndexOfFirstNRepeating(buffer, 14)

def getBuffer(path):
    with open(path) as f:
        buffer = f.readlines()[0]
    return buffer

def main():
    """ Tests """
    buffer = getBuffer('data/day-6-test.txt')
    res = getPartOneSolution(buffer)
    assert(res == 7)
    res = getPartTwoSolution(buffer)
    assert(res == 19)

    """ Solutions """
    buffer = getBuffer('data/day-6.txt')
    res = getPartOneSolution(buffer)
    print('Part one solution: {}'.format(res))
    assert(res == 1655)

    res = getPartTwoSolution(buffer)
    print('Part two solution: {}'.format(res))
    assert(res == 2665)

    return 0

if __name__ == '__main__':
    main()