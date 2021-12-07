from pathlib import Path
from statistics import median
from typing import List

from aoc.util import timing


def part1(crab_subs: List[int]) -> int:
    """Uses the fact that the median solves the L1-centering probem."""
    return sum(abs(x - int(median(crab_subs))) for x in crab_subs)


def fancy_distance(x: int, center: int) -> int:
    """Computes a distance such that each unit of displacement costs more."""
    d = abs(x - center)
    return int(d * (d + 1) / 2)


def sum_of_distances(xs: List[int], center: int) -> int:
    """Returns the sum of fancy distances from each x to the center."""
    return sum(fancy_distance(x, center) for x in xs)


def part2(crab_subs: List[int]) -> int:
    candidates = range(min(crab_subs), max(crab_subs) + 1)
    return min(map(lambda c: sum_of_distances(crab_subs, c), candidates))


def main() -> None:
    crab_submarines: List[int] = []
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        crab_submarines = list(map(int, file.read().split(",")))

    with timing("Part 1"):
        solution = part1(crab_submarines)
    print(solution)

    with timing("Part 2"):
        solution = part2(crab_submarines)
    print(solution)


if __name__ == "__main__":
    main()
