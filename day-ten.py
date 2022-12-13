import numpy as np

NOOP = 'noop'
ADDX = 'addx'

OPERATIONS_CYCLES = {
    NOOP: 1,
    ADDX: 2
}

def updateSignalStrength(cycle, x, cycles, signal_strengths):
    if cycle not in cycles:
        return
    t = cycle * x
    signal_strengths.append(cycle * x)

def parseInstruction(instruction):
    if NOOP in instruction:
        return NOOP, None
    val = int(instruction.split(' ')[1])
    return ADDX, val

def getSignalStrength(instructions, x, cycles):
    signal_strengths = []
    cycle = 0
    tick = 1

    for instruction in instructions:
        inst, val = parseInstruction(instruction)
        if inst is NOOP:
            cycle += tick
            updateSignalStrength(cycle, x, cycles, signal_strengths)
        else:
            cycle += tick
            updateSignalStrength(cycle, x, cycles, signal_strengths)
            cycle += tick
            updateSignalStrength(cycle, x, cycles, signal_strengths)
            x += val

    return sum(signal_strengths)

def getPartOneSolution(instructions):
    x = 1
    cycles = [20, 60, 100, 140, 180, 220]
    signal_strength = getSignalStrength(instructions, x, cycles)
    return signal_strength

def updateScreen(screen, cycle, render_x, x):
    if abs(render_x - x) >= 2:
        return
    screen[cycle] = '#'

def updateRenderPosition(cycle, render_x, width):
    cycle += 1
    render_x += 1
    if render_x >= width:
        render_x = 0
    return cycle, render_x

def printScreen(screen):
    line = ''
    for row in screen:
        for c in row:
            if c == '#':
                line += '█'
            else:
                line += ' '
        print('{}'.format(line))
        line = ''

def getPartTwoSolution(instructions):
    width, height = 40, 6
    screen = ['.'] * (height * width)
    x = 1
    cycle = 0
    render_x = 0

    for instruction in instructions:
        inst, val = parseInstruction(instruction)
        if inst is NOOP:
            updateScreen(screen, cycle, render_x, x)
            cycle, render_x = updateRenderPosition(cycle, render_x, width)
        else:
            updateScreen(screen, cycle, render_x, x)
            cycle, render_x = updateRenderPosition(cycle, render_x, width)

            updateScreen(screen, cycle, render_x, x)
            x += val
            cycle, render_x = updateRenderPosition(cycle, render_x, width)

    return np.array(screen).reshape((height, width))
    

def getInput(path):
    f = open(path)
    lines = f.readlines()
    return lines

def main():
    """ Tests """
    instructions = getInput('data/day-10-test.txt')
    res = getPartOneSolution(instructions)
    assert res == 13140, 'Part one test is incorrect'
    res = getPartTwoSolution(instructions)

    """ Solution """
    instructions = getInput('data/day-10.txt')
    res = getPartOneSolution(instructions)
    print('Part one solution: {}'.format(res))
    assert res == 14340, 'Part one solution is incorrect'
    res = getPartTwoSolution(instructions)
    print('Part two solution:')
    printScreen(res)

    return 0

if __name__ == '__main__':
    main()