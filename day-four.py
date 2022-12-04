import numpy as np

def isFullyContained(start_1, end_1, start_2, end_2):
    if start_1 >= start_2 and \
        end_1 <= end_2:
        return True
    elif start_2 >= start_1 and \
        end_2 <= end_1:
        return True
    return False

def getRangeInt(pair):
    start, end = pair.split('-')
    return int(start), int(end)

def getPartOneSolution(pairs: np.array):
    n_fully_contains = 0

    for pair in pairs:
        pair = pair.split(',')
        start_1, end_1 = getRangeInt(pair[0])
        start_2, end_2 = getRangeInt(pair[1])

        if isFullyContained(start_1, end_1, start_2, end_2):
            n_fully_contains += 1

    return n_fully_contains

def isOverlapping(start_1, end_1, start_2, end_2):
    if start_1 > end_2:
        return False
    elif end_1 < start_2:
        return False
    return True

def getPartTwoSolution(pairs: np.array):
    n_overlap_pairs = 0

    for pair in pairs:
        pair = pair.split(',')
        start_1, end_1 = getRangeInt(pair[0])
        start_2, end_2 = getRangeInt(pair[1])
        if isOverlapping(start_1, end_1, start_2, end_2):
            n_overlap_pairs += 1

    return n_overlap_pairs

def main():
    """ Tests """
    pairs = np.genfromtxt('data/day-4-test.txt', dtype=str)
    res = getPartOneSolution(pairs)
    assert(res == 2)
    res = getPartTwoSolution(pairs)
    assert(res == 4)
    

    """ Solutions """
    pairs = np.genfromtxt('data/day-4.txt', dtype=str)
    res = getPartOneSolution(pairs)
    print('Part one solution: {}'.format(res))
    res = getPartTwoSolution(pairs)
    print('Part two solution: {}'.format(res))

if __name__ == '__main__':
    main()