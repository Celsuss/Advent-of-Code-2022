import numpy as np
import pandas as pd

def getData(path):
    calories = [[]]
    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            if line == '\n':
                calories.append([])
                continue

            val = int(line[:-1]) if '\n' in line else int(line)
            calories[-1].append(val)

    return calories

def getCaloriesSum(calories):
    calories_sum = [sum(row) for row in calories]
    return calories_sum

def partOne(path):
    calories = getData(path)
    cals_sum = getCaloriesSum(calories)
    max_cal = max(cals_sum)
    return max_cal

def partTwo(path):
    calories = getData(path)
    cals_sum = getCaloriesSum(calories)
    top_n = 3
    total_max_cal = 0
    for i in range(top_n):
        max_cal = max(cals_sum)
        total_max_cal += max_cal
        cals_sum.remove(max_cal)
    return total_max_cal

def main():
    """ Part one test """
    res = partOne('data/day-1-test.txt')
    assert(res == 24000)

    """ Part one """
    res = partOne('data/day-1.txt')
    print('Part 1 solution: {}'.format(res))

    """ Part two test """
    res = partTwo('data/day-1-test.txt')
    assert(res == 45000)

    """ Part two """
    res = partTwo('data/day-1.txt')
    print('Part 2 solution: {}'.format(res))

    return 0

if __name__ == '__main__':
    main()