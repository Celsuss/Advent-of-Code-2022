
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

def processMove(move, head_pos, tail_pos, visited_locations: set):
    visited_locations.add((0,0))
    steps = move[1]
    direction = move[0]
    for i in range(steps):
        head_pos = getNewHeadLocation(direction, head_pos)
        tail_pos = getNewTailLocation(head_pos, tail_pos)
        if tail_pos not in visited_locations:
            visited_locations.add(tail_pos)

    return head_pos, tail_pos

def getVisitedLocations(moves, x=0, y=0):
    visited_locations = set()
    head_pos = (x, y)
    tail_pos = (x, y)

    for move in moves:
        head_pos, tail_pos = processMove(move, head_pos, tail_pos, visited_locations)
        continue

    return len(visited_locations)

def getPartOneSolution(moves):
    visited_locations = getVisitedLocations(moves)
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

    """ Solutions """
    moves = getInput('data/day-9.txt')
    res = getPartOneSolution(moves)
    print('Part one solution: {}'.format(res))

    return 0

if __name__ == '__main__':
    main()