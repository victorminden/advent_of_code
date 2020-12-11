from typing import List
from pathlib import Path
from functools import lru_cache
import collections
from copy import deepcopy
import numpy as np
from scipy.signal import convolve2d


from advent_of_code.util import timing

_NEIGHBORS_FILTER = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=np.int64)


def part1(seats: np.ndarray) -> int:
    while True:
        neighbor_sums = convolve2d((seats == '#'), _NEIGHBORS_FILTER, mode='same', fillvalue=0)
        coming = np.logical_and(neighbor_sums == 0, seats == 'L')
        going = np.logical_and(neighbor_sums >= 4.0, seats == '#')
        if not np.any(coming) and not np.any(going):
            break
        seats[coming] = '#'
        seats[going] = 'L'
        print(seats)

    return np.sum(seats == '#')


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
        seats = np.array([list(line.strip()) for line in file], dtype='str')

    with timing("Part 1"):
        solution = part1(seats)
    print(solution)

    # with timing("Part 2"):
    #     solution = part2(adaptors)
    # print(solution)


if __name__ == "__main__":
    main()
