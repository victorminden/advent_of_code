from typing import List
from pathlib import Path
from functools import lru_cache
import collections


from advent_of_code.util import timing


def part1(adaptors: List[int]) -> int:
    c = collections.Counter(a - b for (a, b) in zip(adaptors[1:], adaptors))
    return c[1] * c[3]


def part2(adaptors: List[int]) -> int:
    @lru_cache(maxsize=None)
    def num_valid(idx: int, last: int) -> int:
        if adaptors[idx] > last + 3:
            # Invalid path, cannot get to the end from here.
            return 0
        if idx == len(adaptors) - 1:
            # Valid path, we are at the end.
            return 1
        # Could skip this adaptor, or not.
        return num_valid(idx + 1, last) + num_valid(idx + 1, adaptors[idx])

    return num_valid(idx=1, last=0)


def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        adaptors = [int(line) for line in file]
    adaptors.extend([0, max(adaptors) + 3])
    adaptors.sort()

    with timing("Part 1"):
        solution = part1(adaptors)
    print(solution)

    with timing("Part 2"):
        solution = part2(adaptors)
    print(solution)


if __name__ == "__main__":
    main()
