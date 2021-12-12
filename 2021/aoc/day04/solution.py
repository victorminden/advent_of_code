from pathlib import Path
from typing import List, TypeAlias

from aoc.util import timing


BingoBoard: TypeAlias = List[List[int]]
BingoNumbers: TypeAlias = List[int]


def check_win(board: BingoBoard) -> bool:
    """Returns True if any row or column is entirely None."""
    # Check rows for any that are entirely None.
    for row in board:
        if all(x is None for x in row):
            return True

    # Check columns for any that are entirely None.
    for j in range(len(board[0])):
        col = (row[j] for row in board)
        if all(x is None for x in col):
            return True

    return False


def play_board(number: int, board: BingoBoard) -> bool:
    """Plays a single number on the specified bingo board.

    If the number exists on the board, marks that number as played by replacing
    it with None.

    Return True if the play caused the board to win the game, False otherwise.
    """
    for (i, row) in enumerate(board):
        for (j, x) in enumerate(row):
            # x = board[i][j]
            if x == number:
                board[i][j] = None
                return check_win(board)
    return False


def calculate_score(number: int, board: BingoBoard) -> None:
    """Returns the score of the board, assuming it won.

    The score is the sum of the non-None numbers multiplied by the winning
    number.
    """
    return number * sum(val for row in board for val in row if val is not None)


def part1(numbers: BingoNumbers, boards: List[BingoBoard]) -> int:
    for number in numbers:
        for board in boards:
            is_win = play_board(number, board)
            if is_win:
                return calculate_score(number, board)
    raise RuntimeError("Oops.")


def part2(numbers: BingoNumbers, boards: List[BingoBoard]) -> int:
    # Keep track of which boards have already won by storing the index of each
    # winning board in a set.  Don't try to store the boards themselves because
    # they are mutable.
    winning_boards = set()
    for number in numbers:
        for (board_idx, board) in enumerate(boards):
            is_win = play_board(number, board)
            if is_win:
                winning_boards.add(board_idx)
                if len(winning_boards) == len(boards):
                    return calculate_score(number, board)
    raise RuntimeError("Oops.")


def string2ints(string: List[str], sep: str = None) -> List[int]:
    """Splits the input `string` on separator `sep` and converts all to ints.

    Cleans up leading and trailing whitespace in the input first.
    """
    return list(map(int, string.strip().split(sep)))


def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        input_lines = file.readlines()

    # The input is: one line of numbers, then a blank line, then repeatedly
    # 5 lines of a board + 1 blank line.
    numbers: BingoNumbers = string2ints(input_lines[0], sep=",")
    boards: List[BingoBoard] = []

    for i in range(2, len(input_lines), 6):
        board: BingoBoard = []
        for j in range(i, i + 5):
            board.append(string2ints(input_lines[j]))
        boards.append(board)

    with timing("Part 1"):
        solution = part1(numbers, boards)
    print(solution)

    with timing("Part 2"):
        solution = part2(numbers, boards)
    print(solution)


if __name__ == "__main__":
    main()
