import operator

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

class Monkey:
    def __init__(self, items=None, operation=None, test=None, \
                    if_true=None, if_false=None) -> None:
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.n_inspections = 0
        pass

def processInspection(item, operation):
    if 'old' in operation[1]:
        return item * item
    op = OPERATORS[operation[0]]
    val = int(operation[1])
    return op(item, val)

def processMonkeyInspections(monkey, monkeys, can_divide=True):
    for item in monkey.items:
        monkey.n_inspections += 1
        item = processInspection(item, monkey.operation)
        if can_divide:
            item = int(item / 3)
        if item % monkey.test == 0:
            monkeys[monkey.if_true].items.append(item)
        else:
            monkeys[monkey.if_false].items.append(item)

        continue

    monkey.items = []
    return

def processMonkeys(monkeys, n_rounds, can_divide=True):
    for i in range(n_rounds):
        for monkey in monkeys:
            processMonkeyInspections(monkey, monkeys, can_divide)
            continue
        continue

    return monkeys


def getTopNActiveMonkeys(monkeys, n):
    top_monkeys = []
    def getTopActiveMonkey(monkeys):
        top = -1
        top_monkey = None
        for monkey in monkeys:
            if monkey.n_inspections > top and monkey not in top_monkeys:
                top = monkey.n_inspections
                top_monkey = monkey

        return top_monkey


    for i in range(n):
        top_monkeys.append(
            getTopActiveMonkey(monkeys)
        )

    return top_monkeys

def getPartOneSolution(monkeys):
    monkeys = processMonkeys(monkeys, 20)
    top_monkeys = getTopNActiveMonkeys(monkeys, 2)
    return top_monkeys[0].n_inspections * top_monkeys[1].n_inspections

def getPartTwoSolution(monkeys):
    monkeys = processMonkeys(monkeys, 10000, can_divide=False)
    top_monkeys = getTopNActiveMonkeys(monkeys, 2)
    return top_monkeys[0].n_inspections * top_monkeys[1].n_inspections

def getInput(path):
    def parseItems(items):
        items = items.split(',')
        out = []
        for item in items:
            out.append(int(item))
        return out

    f = open(path)
    lines = f.readlines()
    monkeys = []

    i = 0
    while i < len(lines):
        items = parseItems(lines[i+1].split(':')[1])
        operations = lines[i+2].split(' ')[-2:]
        test = int(lines[i+3].split(' ')[-1])
        if_true = int(lines[i+4].split(' ')[-1])
        if_false = int(lines[i+5].split(' ')[-1])
        monkeys.append(
            Monkey(items, operations, test, if_true, if_false)
        )

        i += 7
        continue

    return monkeys

def main():
    """ Tests """
    monkeys = getInput('data/day-11-test.txt')
    res = getPartOneSolution(monkeys)
    assert res == 10605, 'Part one test is incorrect'

    monkeys = getInput('data/day-11-test.txt')
    res = getPartTwoSolution(monkeys)
    assert res == 2713310158, 'Part two test is incorrect'
    print('Tests done')

    """ Solutions """
    monkeys = getInput('data/day-11.txt')
    res = getPartOneSolution(monkeys)
    print('Part one solution: {}'.format(res))
    assert res == 78960

    monkeys = getInput('data/day-11.txt')
    res = getPartTwoSolution(monkeys)
    print('Part two solution: {}'.format(res))

    return 0


if __name__ == '__main__':
    main()