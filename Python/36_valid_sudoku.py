def checkRows(board):
    for row in board:
        present = {}
        for val in row:
            if val != ".":
                if val not in present:
                    present[val] = 1
                else:
                    return False
    return True

def checkColumns(board):
    for column in range(9):
        present = {}
        for row in range(9):
            if board[column][row] != ".":
                if board[column][row] not in present:
                    present[board[column][row]] = 1
                else:
                    return False
    return True

def checkBlocks(board):
    for i in range(3):
        for r in range(3):
            block = {}
            for row in range(3):
                for column in range(3):
                    val = board[(i*3)+row][(r*3)+column]
                    if val != ".":
                        if val not in block:
                            block[val] = 1
                        else:
                            return False
    return True


def isValidSukodu(board):
    # check rows
    for row in board:
        present = {}
        for val in row:
            if val != ".":
                if val not in present:
                    present[val] = 1
                else:
                    return False

    # check columns
    for row in range(9):
        present = {}
        for column in range(9):
            if board[column][row] != ".":
                if board[column][row] not in present:
                    present[board[column][row]] = 1
                else:
                    return False

    # check blocks
    for i in range(3):
        for r in range(3):
            block = {}
            for row in range(3):
                for column in range(3):
                    val = board[(i*3)+row][(r*3)+column]
                    if val != ".":
                        if val not in block:
                            block[val] = 1
                        else:
                            return False
    return True

board = [[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]

print(isValidSukodu(board))