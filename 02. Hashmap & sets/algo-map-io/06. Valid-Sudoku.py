def solve(board):
    # 9 x 9 board
    # check each row
    for i in range(0, 9):
        s = set()
        for j in range(0, 9):
            if board[i][j] in s:
                return False
            elif board[i][j] != '.':
                s.add(board[i][j])
    
    # check each column
    for i in range(0, 9):
        s = set()
        for j in range(0, 9):
            if board[j][i] in s:
                return False
            elif board[j][i] != '.':
                s.add(board[j][i])
    
    # check sub boxes
    positions = [
        (0, 0), (0, 3), (0, 6),
        (3, 0), (3, 3), (3, 6),
        (6, 0), (6, 3), (6, 6)
    ]

    for i, j in positions:
        s = set()
        for row in range(i, i + 3):
            for col in range(j, j + 3):
                if board[row][col] in s : 
                    return False
                elif board[row][col] != '.':
                    s.add(board[row][col])
    return True


def main():
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(solve(board))

main()