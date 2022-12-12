
def getNewHeadLocation(direction, pos):
    if direction == 'R':
        pos = (pos[0] + 1, pos[1])
    elif direction == 'L':
        pos = (pos[0] - 1, pos[1])
    elif direction == 'U':
        pos = (pos[0], pos[1] + 1)
    elif direction == 'D':
        pos = (pos[0], pos[1] - 1)

    return pos

def getNewTailLocation(head_pos, tail_pos):
    def clamp(num, min_value, max_value):
        return max(min(num, max_value), min_value)

    """ Only move tail if head is distance is >=2 """
    if head_pos == tail_pos or \
        (abs(head_pos[0] - tail_pos[0]) < 2 and
        abs(head_pos[1] - tail_pos[1]) < 2):
        return tail_pos

    direction = (clamp(head_pos[0] - tail_pos[0], -1, 1),
                clamp(head_pos[1] - tail_pos[1], -1, 1))
    tail_pos = (tail_pos[0] + direction[0],
                tail_pos[1] + direction[1])
    return tail_pos

def processMove(move, rope, visited_locations: set):
    visited_locations.add((0,0))
    steps = move[1]
    direction = move[0]

    for i in range(steps):
        rope[0] = getNewHeadLocation(direction, rope[0])
        for i in range(1, len(rope)):
            rope[i] = getNewTailLocation(rope[i-1], rope[i])

        tail_pos = rope[-1]
        if tail_pos not in visited_locations:
            visited_locations.add(tail_pos)

    # return head_pos, tail_pos

def getVisitedLocations(moves, rope):
    visited_locations = set()

    for move in moves:
        processMove(move, rope, visited_locations)
        continue

    return len(visited_locations)

def getPartOneSolution(moves):
    rope = [(0,0) for i in range(2)]
    visited_locations = getVisitedLocations(moves, rope)
    return visited_locations

def getPartTwoSolution(moves):
    rope = [(0,0) for i in range(10)]
    visited_locations = getVisitedLocations(moves, rope)
    return visited_locations

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
    res = getPartTwoSolution(moves)
    assert res == 1, 'Part two test is incorrect'

    """ Solutions """
    moves = getInput('data/day-9.txt')
    res = getPartOneSolution(moves)
    print('Part one solution: {}'.format(res))
    assert res == 6745, 'Part one is incorrect'
    res = getPartTwoSolution(moves)
    print('Part two solution: {}'.format(res))
    assert res == 2793, 'Part two is incorrect'

    return 0

if __name__ == '__main__':
    main()