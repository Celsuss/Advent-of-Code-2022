import numpy as np

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

move_scores = {
    rock: 1,
    paper: 2,    
    scissors: 3
}

moves =  {
    'A': rock,
    'B': paper,
    'C': scissors,
    'X': rock,
    'Y': paper,
    'Z': scissors
}

def isWinner(my_move, other_move):
    my = moves[my_move]
    other = moves[other_move]

    if my == rock and other == scissors:
        return True
    elif my == paper and other == rock:
        return True
    elif my == scissors and other == paper:
        return True

    return False

def getScore(my_move, other_move):
    victory = isWinner(my_move, other_move)
    draw = False
    if victory is False:
        other_victory = isWinner(other_move, my_move)
        draw = isWinner(other_move, my_move) == False

    victor_score = 6 if victory is True else 0
    draw_score = 3 if draw is True else 0
    move_score = move_scores[moves[my_move]]
    score = move_scores[moves[my_move]] + victor_score + draw_score
    return score

def getTotalScore(moves):
    score_sum = 0
    for move in moves:
        score = getScore(move[1], move[0])
        score_sum += score
        
    return score_sum

def partOneTest(moves):
    score = getTotalScore(moves)
    assert(score == 15)

def partOne(moves):
    score = getTotalScore(moves)
    print('Part one solution: {}'.format(score))

def main():
    moves = np.genfromtxt('data/day-2-test.txt', dtype=str)
    partOneTest(moves)

    moves = np.genfromtxt('data/day-2.txt', dtype=str)
    partOne(moves)

    return 0

if __name__ == '__main__':
    main()