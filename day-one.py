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

            val = int(line[:-1])
            calories[-1].append(val)
            continue
    return calories

def getCaloriesSum(calories):
    calories_sum = [sum(row) for row in calories]
    return calories_sum

def main():
    """ Problem one test """
    calories = getData('data/day-1-test.txt')
    cals_sum = getCaloriesSum(calories)
    max_cal = max(cals_sum)
    assert(max_cal == 24000)

    """ Problem one """
    calories = getData('data/day-1.txt')
    cals_sum = getCaloriesSum(calories)
    max_cal = max(cals_sum)
    print('Max cals: {}'.format(max_cal))

    return 0

if __name__ == '__main__':
    main()