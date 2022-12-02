import numpy as np

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
lose = 'Lose'
draw = 'Draw'
win = 'Win'

moves_scores_dict = {
    rock: 1,
    paper: 2,    
    scissors: 3
}

def isWinner(my_move, other_move, moves_dict):
    my = moves_dict[my_move]
    other = moves_dict[other_move]

    if my == rock and other == scissors:
        return True
    elif my == paper and other == rock:
        return True
    elif my == scissors and other == paper:
        return True

    return False

def getScore(my_move, other_move, moves_dict):
    victory = isWinner(my_move, other_move, moves_dict)
    draw = False
    if victory is False:
        other_victory = isWinner(other_move, my_move, moves_dict)
        draw = isWinner(other_move, my_move, moves_dict) == False

    victor_score = 6 if victory is True else 0
    draw_score = 3 if draw is True else 0
    score = moves_scores_dict[moves_dict[my_move]] + victor_score + draw_score
    return score

def getTotalScore(moves, moves_dict):
    score_sum = 0
    for move in moves:
        score = getScore(move[1], move[0], moves_dict)
        score_sum += score
        
    return score_sum

def partOneTest(moves, moves_dict):
    score = getTotalScore(moves, moves_dict)
    assert(score == 15)

def partOne(moves, moves_dict):
    score = getTotalScore(moves, moves_dict)
    print('Part one solution: {}'.format(score))

def getWinningMove(move):
    if move == rock:
        return paper
    elif move == paper:
        return scissors
    elif move == scissors:
        return rock

def getLosingMove(move):
    if move == rock:
        return scissors
    elif move == paper:
        return rock
    elif move == scissors:
        return paper

def getBestMoves(moves, moves_dict):
    best_moves = []
    for move in moves:
        opponent_move = moves_dict[move[0]]
        condition = moves_dict[move[1]]
        if condition == win:
            best_moves.append(
                getWinningMove(opponent_move)
            )
        elif condition == lose:
            best_moves.append(
                getLosingMove(opponent_move)
            )
        else:
            best_moves.append(opponent_move)

    return best_moves

def partTwoTest(moves, moves_dict):
    best_moves = getBestMoves(moves, moves_dict)
    moves[:,1] = best_moves
    score = getTotalScore(moves, moves_dict)
    assert(score == 12)

def partTwo(moves, moves_dict):
    best_moves = getBestMoves(moves, moves_dict)
    moves[:,1] = best_moves
    score = getTotalScore(moves, moves_dict)
    print('Part two solution: {}'.format(score))

def main():
    moves_part_one_dict =  {
        'A': rock,
        'B': paper,
        'C': scissors,
        'X': rock,
        'Y': paper,
        'Z': scissors
    }
    moves_part_two_dict =  {
        'A': rock,
        'B': paper,
        'C': scissors,
        'R': rock,
        'P': paper,
        'S': scissors,
        'X': lose,
        'Y': draw,
        'Z': win
    }

    moves = np.genfromtxt('data/day-2-test.txt', dtype=str)
    partOneTest(moves, moves_part_one_dict)
    partTwoTest(moves, moves_part_two_dict)

    moves = np.genfromtxt('data/day-2.txt', dtype=str)
    partOne(moves, moves_part_one_dict)
    partTwo(moves, moves_part_two_dict)

    return 0

if __name__ == '__main__':
    main()