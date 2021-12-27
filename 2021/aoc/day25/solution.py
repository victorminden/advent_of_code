# Don't even bother to clean this up.
from copy import deepcopy
from itertools import product
from pathlib import Path
from typing import List

from aoc.util import timing


def show(cucumbers):
    for line in cucumbers:
        print("".join(line))
    print('\n')


def part1(cucumbers: List[List[str]]) -> int:
    m = len(cucumbers)
    n = len(cucumbers[0])
    newer_cucumbers = None

    counter = 0

    while True:
        counter += 1
        new_cucumbers = deepcopy(cucumbers)
        for i, j in product(range(m), range(n)):
            if cucumbers[i][j] != '>':
                continue
            j_dst = (j + 1) % n
            if cucumbers[i][j_dst] == '.':
                new_cucumbers[i][j_dst] = '>'
                new_cucumbers[i][j] = '.'

        newer_cucumbers = deepcopy(new_cucumbers)
        for (i, j) in product(range(m), range(n)):
            if new_cucumbers[i][j] != 'v':
                continue
            i_dst = (i + 1) % m
            if new_cucumbers[i_dst][j] == '.':
                newer_cucumbers[i_dst][j] = 'v'
                newer_cucumbers[i][j] = '.'
        if cucumbers == newer_cucumbers:
            return counter
        cucumbers = deepcopy(newer_cucumbers)


def part2(cucumbers: List[List[str]]) -> int:
    return 0


def main() -> None:
    cucumbers: List[List[str]] = []
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        for line in file:
            cucumbers.append(list(line.strip()))

    with timing("Part 1"):
        solution = part1(cucumbers)
    print(solution)

    with timing("Part 2"):
        solution = part2(cucumbers)
    print(solution)


if __name__ == "__main__":
    main()
