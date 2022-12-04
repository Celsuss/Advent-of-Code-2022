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

        continue

    return n_fully_contains

def main():
    """ Tests """
    pairs = np.genfromtxt('data/day-4-test.txt', dtype=str)
    res = getPartOneSolution(pairs)
    assert(res == 2)
    

    """ Solutions """
    pairs = np.genfromtxt('data/day-4.txt', dtype=str)
    res = getPartOneSolution(pairs)
    print('Part one solution: {}'.format(res))

    return 0

if __name__ == '__main__':
    main()