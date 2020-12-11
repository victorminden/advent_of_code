from typing import List
from pathlib import Path
from functools import lru_cache
import collections
from copy import deepcopy
import numpy as np
from scipy.signal import convolve2d


from advent_of_code.util import timing

_NEIGHBORS_FILTER = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=np.int64)
_NEIGHBORS_OFFSETS = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
    [1, 1],
    [-1, -1],
    [1, -1],
    [-1, 1],
]

def part1(seats: np.ndarray) -> int:
    while True:
        neighbor_sums = convolve2d((seats == '#'), _NEIGHBORS_FILTER, mode='same', fillvalue=0)
        coming = np.logical_and(neighbor_sums == 0, seats == 'L')
        going = np.logical_and(neighbor_sums >= 4.0, seats == '#')
        if not np.any(coming) and not np.any(going):
            break
        seats[coming] = '#'
        seats[going] = 'L'

    return np.sum(seats == '#')


def part2(seats: np.ndarray) -> int:
    (m, n) = seats.shape
    while True:
        visible_seats = np.zeros((m,n), dtype=np.int64)
        for i in range(m):
            for j in range(n):
                for oi, oj in _NEIGHBORS_OFFSETS:
                    d = 1
                    ii = i + d * oi
                    jj = j + d * oj
                    while ii in range(m) and jj in range(n):
                        if seats[ii, jj] == '#':
                            visible_seats[i, j] += 1
                            break
                        if seats[ii, jj] != '.':
                            break
                        d += 1
                        ii = i + d * oi
                        jj = j + d * oj
        #print(visible_seats)
        coming = np.logical_and(visible_seats == 0, seats == 'L')
        going = np.logical_and(visible_seats >= 4.9, seats == '#')
        if not np.any(coming) and not np.any(going):
            break
        seats[coming] = '#'
        seats[going] = 'L'
        #print(seats)
    return np.sum(seats == '#')



def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        seats = np.array([list(line.strip()) for line in file], dtype='str')

    with timing("Part 1"):
        solution = part1(seats.copy())
    print(solution)

    with timing("Part 2"):
        solution = part2(seats)
    print(solution)


if __name__ == "__main__":
    main()
