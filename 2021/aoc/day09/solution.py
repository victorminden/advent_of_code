from itertools import product
from pathlib import Path
from typing import Iterator, List, Tuple

from aoc.util import timing


def neighbors(i: int, j: int, m: int, n: int) -> Iterator[Tuple[int, int]]:
    """Yields tuples of indices of neighbors of (i, j) in the (m, n) grid.

    Neighbors must be adjacent to the original point and diagonals do not
    count.
    """
    if i > 0:
        yield i - 1, j
    if i < m - 1:
        yield i + 1, j
    if j > 0:
        yield i, j - 1
    if j < n - 1:
        yield i, j + 1


def low_points(zs: List[List[int]]) -> Iterator[Tuple[int, int]]:
    """Yields points in zs that are less than all their neighbors."""
    m, n = len(zs), len(zs[0])
    for (i, j) in product(range(m), range(n)):
        if all(zs[i][j] < zs[ii][jj] for (ii, jj) in neighbors(i, j, m, n)):
            yield i, j


def part1(zs: List[List[int]]) -> int:
    return sum(1 + zs[i][j] for (i, j) in low_points(zs))


def part2(zs: List[List[int]]) -> int:
    # For each point, determine which basin it ultimatly flows into.
    basins_by_low_point = {(i, j): [] for (i, j) in low_points(zs)}
    m, n = len(zs), len(zs[0])
    for (i0, j0) in product(range(m), range(n)):
        # Value 9 Does not flow anywhere, so just skip 9s.
        if zs[i0][j0] == 9:
            continue

        # Every other value is guaranteed to eventually flow to a basin.
        # Simulate this to find which basin.
        i, j = i0, j0
        while (i, j) not in basins_by_low_point:
            for (ii, jj) in neighbors(i, j, m, n):
                if zs[ii][jj] < zs[i][j]:
                    i, j = ii, jj
        basins_by_low_point[(i, j)].append((i0, j0))

    # Figure out the sizes of the three largest basins and multiply them
    # together to generate the final answer.
    sorted_sizes = list(
        sorted(map(lambda x: len(x), basins_by_low_point.values())))
    return sorted_sizes[-3] * sorted_sizes[-2] * sorted_sizes[-1]


def main() -> None:
    heights: List[List[int]] = []
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        for line in file:
            heights.append(list(map(lambda x: int(x), line.strip())))

    with timing("Part 1"):
        solution = part1(heights)
    print(solution)

    with timing("Part 2"):
        solution = part2(heights)
    print(solution)


if __name__ == "__main__":
    main()
