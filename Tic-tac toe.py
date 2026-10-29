def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for column in range(3):
        if all(board[row][column] == player for row in range(3)):
            return True

    return all(board[index][index] == player for index in range(3)) or all(
        board[index][2 - index] == player for index in range(3)
    )


def evaluate(board):
    # Returns +10 if AI wins, -10 if Human wins, 0 if draw/ongoing
    if check_win(board, 'X'): return 10
    if check_win(board, 'O'): return -10
    return 0

def minimax(board, depth, is_maximizing):
    score = evaluate(board)
    
    # Base cases: If the game is over, return the score
    if score == 10: return score - depth  # Subtract depth to prefer quicker wins
    if score == -10: return score + depth # Add depth to prolong the game if losing
    if not any('_' in row for row in board): return 0

    if is_maximizing:
        best_score = -float('inf')
        for r in range(3):
            for c in range(3):
                if board[r][c] == '_':
                    board[r][c] = 'X' # Make move
                    score = minimax(board, depth + 1, False)
                    board[r][c] = '_' # Undo move (Backtrack)
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for r in range(3):
            for c in range(3):
                if board[r][c] == '_':
                    board[r][c] = 'O' # Make move
                    score = minimax(board, depth + 1, True)
                    board[r][c] = '_' # Undo move
                    best_score = min(score, best_score)
        return best_score