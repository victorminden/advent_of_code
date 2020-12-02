# Day 1: Better solution for fun (previously: nested for loops)
# Assume that it is okay to repeat a number when forming the subset sum (select with replacement) since problem is
# underspecified.
from typing import Set
from pathlib import Path

from advent_of_code.util import timing


def part1(numbers: Set[int], target_sum: int = 2020) -> int:
    for n in numbers:
        if target_sum - n in numbers:
            return (target_sum - n) * n
    raise RuntimeError(f"Failed to find numbers summing to {target_sum}!")


def part2(numbers: Set[int], target_sum: int = 2020) -> int:
    for n in numbers:
        try:
            return n * part1(numbers, target_sum - n)
        except RuntimeError:
            # This is fine.
            pass
    raise RuntimeError(f"Failed to find numbers summing to {target_sum}!")


def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        numbers = {int(line) for line in file}

    with timing("Part 1"):
        solution = part1(numbers)
    print(solution)

    with timing("Part 2"):
        solution = part2(numbers)
    print(solution)


if __name__ == "__main__":
    main()
