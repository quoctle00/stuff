"""
Tic Tac Toe Player
"""

import math
from re import L
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0

    if terminal(board):
        return EMPTY

    # check which player will play next if terminal position is not reached

    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == X:
                x = x+1
            elif board[i][j] == O:
                o = o+1
    if x > o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # returns the possible positions in (i,j) form if its not a terminal position

    if terminal(board):
        return EMPTY

    value = []

    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == EMPTY:
                value.append((i, j))

    return value


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result = copy.deepcopy(board)

    result[action[0]][action[1]] = player(board)

    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # returns if there is a match row wise or column wise or diagonally
    # returns None if there is no winner

    for i in range(0, len(board)):
        x = 0
        o = 0
        for j in range(0, len(board[i])):
            if board[i][j] == X:
                x = x+1
            elif board[i][j] == O:
                o = o+1
        if x == 3:
            return 'X'
        elif o == 3:
            return 'O'

    for j in range(0, len(board[0])):
        x = 0
        o = 0
        for i in range(0, len(board)):
            if board[i][j] == X:
                x = x+1
            elif board[i][j] == O:
                o = o+1

        if x == 3:
            return 'X'
        elif o == 3:
            return 'O'

    i, j, x, o = 0, 0, 0, 0

    while (i < 3 and j < 3):
        if board[i][j] == X:
            x = x+1
        elif board[i][j] == O:
            o = o+1
        i = i+1
        j = j+1

    if x == 3:
        return 'X'
    elif o == 3:
        return 'O'

    i, j, x, o = 0, 2, 0, 0

    while (i < 3 and j > -1):
        if board[i][j] == X:
            x = x+1
        elif board[i][j] == O:
            o = o+1
        i = i+1
        j = j-1

    if x == 3:
        return 'X'
    elif o == 3:
        return 'O'

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # This function returns true if there is a winner or if it is a tie
    # It will return false if the game is still in progress

    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == EMPTY:
                if winner(board) != None:
                    return True
                else:
                    return False

    return True


def score(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        w = winner(board)
        if w != None:
            if w == X:
                return 1
            else:
                return -1
        else:
            return 0

    return EMPTY


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # if the board is in terminal state then return None
    #
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = maxval(board)
            return move
        else:
            value, move = minval(board)
            return move


def maxval(board):

    # if the board has reached its terminal state then return the score (1 if X has won, -1 if O has won, else 0 if it is a tie)
    if terminal(board):
        return score(board), None

    # Set the value to -infinity and move to None initially
    val = float('-inf')
    move = None
    for action in actions(board):

        a, act = minval(result(board, action))
        if a > val:
            val = a
            move = action
            if val == 1:
                return val, move

    return val, move


def minval(board):
    if terminal(board):
        return score(board), None

    val = float('inf')
    move = None
    for action in actions(board):

        a, act = maxval(result(board, action))
        if a < val:
            val = a
            move = action
            if val == -1:
                return val, move

    return val, move
