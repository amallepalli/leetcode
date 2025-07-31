from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    for i in range(len(board)):
        rowDup = {}
        for j in range(len(board[0])):
            if (board[i][j] == '.'):
                continue
            if (rowDup.get(board[i][j]) != None):
                return False
            else:
                rowDup[board[i][j]] = 1

    for j in range(len(board[0])):
        colDup = {}
        for i in range(len(board)):
            if (board[i][j] == '.'):
                continue
            if (colDup.get(board[i][j]) != None):
                return False
            else:
                colDup[board[i][j]] = 1
    
    for i in range(0, len(board), 3):
        for j in range(0, len(board), 3):
            boxDup = {}
            for k in range(j, j + 3, 1):
                for l in range(i, i+3, 1):
                    if(board[k][l] == '.'):
                        continue
                    if(boxDup.get(board[k][l]) != None):
                        return False
                    else:
                        boxDup[board[k][l]] = 1
    return True
    
board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]



print(isValidSudoku(board))
