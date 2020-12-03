from typing import Tuple, List
from pathlib import Path
from functools import reduce
import operator

from advent_of_code.util import timing


def part1(trees: List[str], slope: Tuple[int, int] = (3, 1)) -> int:
    return sum((row[(i * slope[0]) % len(row)] == '#' for (i, row) in enumerate(trees[::slope[1]])))


def part2(trees: List[str]) -> int:
    return reduce(operator.mul, (part1(trees, slope) for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))


def main() -> None:
    trees = []
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        for line in file:
            trees.append(line.strip())

    with timing("Part 1"):
        solution = part1(trees)
    print(solution)

    with timing("Part 2"):
        solution = part2(trees)
    print(solution)


if __name__ == "__main__":
    main()
