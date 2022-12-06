
def getData(path):
    def getNCrates(lines):
        for i in range(len(lines)-1):
            if lines[i+1] == '\n':
                n_columns = lines[i][-3]
                return int(n_columns)
        return 0
    
    def getCrates(lines, n_crates):
        crates = [[] for i in range(n_crates)]

        for line in lines:
            for i in range(n_crates):
                item = line[(i*4)+1]
                if item.isdigit():
                    return crates

                if item != ' ':
                    crates[i].append(item)

        return crates
    
    def getMoves(lines):
        moves = []
        for line in lines:
            if line[:4] != 'move':
                continue

            line_moves = line.split(' ')
            moves.append([int(line_moves[1]), int(line_moves[3]),
                            int(line_moves[5])])

        return moves

    with open(path) as f:
        lines = f.readlines()
        n_crates = getNCrates(lines)
        crates = getCrates(lines, n_crates)
        moves = getMoves(lines)

    return crates, moves

def getDayOneSolution(crates, moves):
    reverseCrates(crates)
    for n_crates, start_crate, target_crate in moves:
        for i in range(n_crates):
            crate = crates[start_crate-1].pop()
            crates[target_crate-1].append(crate)
            continue

    return getTopCratesStr(crates)

def reverseCrates(crates):
    for crate in crates:
        crate = crate.reverse()

def getTopCratesStr(crates):
    out = ''
    for crate in crates:
        out += crate[-1]
    return out

def main():
    """ Tests """
    crates, moves = getData('data/day-5-test.txt')
    res = getDayOneSolution(crates[:], moves)
    assert(res == 'CMZ')

    """ Solutions """
    crates, moves = getData('data/day-5.txt')
    res = getDayOneSolution(crates[:], moves)
    print('Part one solution: {}'.format(res))

    return 0

if __name__ == '__main__':
    main()