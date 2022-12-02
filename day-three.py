import numpy as np

def getSharedItem(items1, items2):
    items1_dict = set(items1)
    for item2 in items2:
        if item2 in items1_dict:
            return item2

    return None

def getItemPriority(item: str):
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
        priority_sum += getItemPriority(shared)

    return priority_sum

def getSharedBadge(packs):
    pack1_dict = packs[0]
    pack2_dict = packs[1]
    for item in packs[2]:
        if item in pack1_dict and item in pack2_dict:
            return item

    return None

def getPartTwoSolution(backpacks):
    backpacks = backpacks.reshape(-1, 3)
    priority_sum = 0
    for packs in backpacks:
        badge = getSharedBadge(packs)
        priority_sum += getItemPriority(badge)

    return priority_sum

def main():
    """ Tests """
    backpacks = np.genfromtxt('data/day-3-test.txt', dtype=str)
    res = getPartOneSolution(backpacks)
    assert(res == 157)
    res = getPartTwoSolution(backpacks)
    assert(res == 70)

    """ Solutions """
    backpacks = np.genfromtxt('data/day-3.txt', dtype=str)
    res = getPartOneSolution(backpacks)
    assert(res == 8018)
    print('Part one solution: {}'.format(res))
    res = getPartTwoSolution(backpacks)
    assert(res == 2518)
    print('Part two solution: {}'.format(res))

    return 0

if __name__ == '__main__':
    main()