"""
Tic Tac Toe Player
"""

import math
import copy as cp

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
    
    # If the game is over, it is nobody's turn
    if terminal(board):
        return None 
    
    # If the board is the initial state or there are an odd number of squares remaining, return X
    elif board == initial_state() or sum(row.count(EMPTY) for row in board) % 2 != 0:
        return X 
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # First check if the game is already over. Otherwise, calculate actions
    if terminal(board):
        return None
    else:
        # Initialize set of actions
        actions = set()

        # Iterate over squares and add its index to the set of actions if its empty
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    actions.add((i, j))
        return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Raise an exception if the action is not in the possible actions
    if action not in actions(board):
        raise Exception("Invalid Move")

    # Store whose turn it is
    turn = player(board) 

    # Store a deepcopy of the board
    new_board = cp.deepcopy(board)

    # Unpack the action
    i, j = action
    
    # Copy each square from the board onto a new board
    for k in range(3):
        for l in range(3):
            new_board[k][l] = board[k][l]

    # Set the square corresponding to the action to "X" or "O", depending on whose turn it is
    new_board[i][j] = turn

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    # Check for horizontal wins
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O
        else:
            # No horizontal wins, move on
            pass

    # Check for vertical wins 
    for j in range(3):
        if all(board[i][j] == X for i in range(3)):
            return X 
        elif all(board[i][j] == O for i in range(3)):
            return O
        else:
            pass

    # Check for diagonal wins 
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O
        else:
            pass
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == X:
            return X
        elif board[0][2] == O:
            return O
        else:
            return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # Game is over if there is a winner or there are no EMPTY cells
    return True if winner(board) is not None or sum(row.count(EMPTY) for row in board) == 0 else False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    victor = winner(board)
    if victor == X:
        return 1 
    elif victor == O:
        return -1
    else:
        return 0
            
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # No best move if the game is over
    if terminal(board):
        return None
    

    elif player(board) == X:
        v0 = -math.inf
        for action in actions(board):
            # Store max value of a particular action
            v = max_value(result(board, action))
            if v > v0:
                # Store it as the best move and continue the loop
                v0 = v 
                best_move = action 
        return best_move 
    
    # Similarly
    elif player(board) == O:
        v0 = math.inf
        for action in actions(board):
            v = min_value(result(board, action))
            if v < v0:
                v0 = v 
                best_move = action
        return best_move
    else:
        return None
    
def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf 
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board) 
    v = math.inf 
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v