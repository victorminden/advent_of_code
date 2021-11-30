from itertools import accumulate
from pathlib import Path
from typing import List

from aoc.util import timing


def part1(numbers: List[int]) -> int:
    """Returns the number of times numbers[j] > numbers[j - 1]."""
    return sum(b > a for (a, b) in zip(numbers, numbers[1:]))


def windowed_sum(numbers: List[int], window_size: int = 3) -> List[int]:
    """Returns a "windowed sum" over the list of numbers.

    The k-th output is the same as if it had been given by summing the input
    list from numbers[k] to numbers[k + window_size].  This is performed using
    the standard cumulative sum algorithm that exploits the fact that partial
    sums of a list are the same as differences between elements in the cumsum of
    that list.
    """
    cumsum = list(accumulate(numbers))
    return [b - a for (a, b) in zip(cumsum, cumsum[window_size:])]


def part2(numbers: List[int]) -> int:
    """Returns the number of times the windowed sum of the list increases.

    A windowed sum is a sum over adjacent elements in the list.
    """
    return part1(windowed_sum(numbers, window_size=3))


def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        numbers = [int(line) for line in file]

    with timing("Part 1"):
        solution = part1(numbers)
    print(solution)

    with timing("Part 2"):
        solution = part2(numbers)
    print(solution)


if __name__ == "__main__":
    main()
