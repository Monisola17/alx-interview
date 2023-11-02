#!/usr/bin/python3
""" N queens puzzle, challenge of placing N non attacking queens
on a NxN chessboard
This program solves the N queens problem """

import sys


def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print()

def solve_nqueens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def solve(col):
        if col == n:
            solutions.append([row[:] for row in board])
            return

        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                solve(col + 1)
                board[i][col] = 0

    solve(0)
    return solutions

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print_solution(solution)

if __name__ == "__main__":
    main()

