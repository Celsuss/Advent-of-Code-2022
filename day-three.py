import numpy as np

def getSharedItem(items1, items2):
    items1_dict = set(items1)
    for item2 in items2:
        if item2 in items1_dict:
            return item2

    return None

def getItemPriority(item: str):
    l = ord(item) - 96
    u = ord(item) - 64 + 26

    if item.islower():
        return ord(item) - 96
    return ord(item) - 64 + 26

def getPartOneSolution(backpacks):
    priority_sum = 0
    for backpack in backpacks:
        mid_point = int(len(backpack) / 2)
        items1 = backpack[:mid_point]
        items2 = backpack[mid_point:]
        assert(len(items1) == len(items2))

        shared = getSharedItem(items1, items2)
        priority = getItemPriority(shared)
        priority_sum += priority

        continue

    return priority_sum

def main():
    """ Tests """
    backpacks = np.genfromtxt('data/day-3-test.txt', dtype=str)
    res = getPartOneSolution(backpacks)
    assert(res == 157)

    """ Solutions """
    backpacks = np.genfromtxt('data/day-3.txt', dtype=str)
    res = getPartOneSolution(backpacks)
    print('Part one solution: {}'.format(res))

    return 0

if __name__ == '__main__':
    main()