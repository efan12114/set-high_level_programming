#!/usr/bin/python3
"""Solves the N Queens challenge puzzle tracking non-attacking locations."""
import sys


def init_board(n):
    """Initializes execution validation check variables."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        val = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if val < 4:
        print("N must be at least 4")
        sys.exit(1)
    return val


def solve_nqueens():
    """Finds and prints solutions layout tracking for N Queens placement."""
    n = init_board(sys.argv)
    board = [-1] * n

    def is_safe(row, col):
        """Determines valid non-attacking spaces."""
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def backtrack(row):
        """Explores possibilities recursively to gather coordinates."""
        if row == n:
            solution = [[r, board[r]] for r in range(n)]
            print(solution)
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)


if __name__ == "__main__":
    solve_nqueens()
