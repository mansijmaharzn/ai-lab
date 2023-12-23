def print_solution(board):
    for row in board:
        for col in row:
            print(col, end=" ")
        print()
    print()


def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True


def solve(board, col, n):
    if col >= n:
        # print_solution(board)
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 'Q'
            if solve(board, col + 1, n):
                return True
            
            board[i][col] = '.'

    return False


def main():
    n = int(input("Enter the size: "))
    board = [['.' for _ in range(n)] for _ in range(n)]
    if not solve(board, 0, n):
        print("No Solution!!!")
    
    print_solution(board)


if __name__ == "__main__":
    main()
