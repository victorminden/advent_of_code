from pathlib import Path
from statistics import median
from typing import List

from aoc.util import timing


def flip_bracket(c: str) -> str:
    """Returns the matching bracket for the given input bracket."""
    return c.translate(str.maketrans("()[]{}<>", ")(][}{><"))


def corruption_score(line: str) -> int:
    """Returns a score for the line if it is corrupted, or zero otherwise."""
    BRACKET_SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}
    stack = []
    for c in line:
        if c in "([{<":
            stack.append(c)
        elif c != flip_bracket(stack.pop()):
            return BRACKET_SCORE[c]
    return 0


def part1(lines: List[str]) -> int:
    return sum(corruption_score(line) for line in lines)


def completion_score(line: str) -> int:
    """Returns a score for the line assuming it is not corrupted."""
    stack = []
    for c in line:
        if c in "([{<":
            stack.append(c)
        else:
            stack.pop()

    BRACKET_SCORE = {")": 1, "]": 2, "}": 3, ">": 4}
    score = 0
    for c in reversed(stack):
        score = score * 5 + BRACKET_SCORE[flip_bracket(c)]
    return score


def part2(lines: List[str]) -> int:
    return median(
        completion_score(line) for line in lines if corruption_score(line) == 0
    )


def main() -> None:
    lines = []
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        lines = [line.strip() for line in file]

    with timing("Part 1"):
        solution = part1(lines)
    print(solution)

    with timing("Part 2"):
        solution = part2(lines)
    print(solution)


if __name__ == "__main__":
    main()
