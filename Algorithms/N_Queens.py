def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []

    def is_safe(row, col):
        for i in range(row):
            if board[i][col] == 1:
                return False

        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def backtrack(row):
        if row == n:
            solutions.append([r[:] for r in board])
            return

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0

    backtrack(0)
    return solutions


n = 4
solutions = solve_n_queens(n)

for sol in solutions:
    for row in sol:
        print(row)
    print()