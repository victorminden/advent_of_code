from itertools import product
from pathlib import Path
from typing import Iterator, List, Optional, Set, Tuple

from aoc.util import timing


def neighbors(i: int, j: int, m: int, n: int) -> Iterator[Tuple[int, int]]:
    """Yields tuples of indices of neighbors of (i, j) in the (m, n) grid.

    Neighbors must be adjacent to the original point and diagonals count.
    """
    for (delta_i, delta_j) in product((-1, 0, 1), (-1, 0, 1)):
        if delta_i == 0 and delta_j == 0:
            pass
        ii, jj = i + delta_i, j + delta_j
        if 0 <= ii < m and 0 <= jj < n:
            yield ii, jj


def increase_all(octopods: List[List[int]]) -> List[List[int]]:
    return [[v + 1 for v in line] for line in octopods]


def will_flash(octopus: int) -> bool:
    return octopus > 9


def any_flashers(octopods: List[List[int]], used: Set[Tuple[int, int]]) -> bool:
    m, n = len(octopods), len(octopods[0])
    for (i, j) in product(range(m), range(n)):
        if (i, j) in used:
            continue
        if will_flash(octopods[i][j]):
            return True
    return False


def simulate_flashes(
    octopods: List[List[int]], steps: int
) -> Tuple[int, Optional[int]]:
    """Returns the number of total flashes and the first synchronized step.

    The first synchronized step will be None if the octopods did not synchronize
    up to step "steps".
    """
    flash_count = 0
    m, n = len(octopods), len(octopods[0])
    for step in range(steps):
        octopods = increase_all(octopods)
        used = set()
        while any_flashers(octopods, used):
            for (i, j) in product(range(m), range(n)):
                if (i, j) in used:
                    continue
                if not will_flash(octopods[i][j]):
                    continue
                for (ii, jj) in neighbors(i, j, m, n):
                    octopods[ii][jj] += 1
                used.add((i, j))
        for (i, j) in used:
            octopods[i][j] = 0
        flash_count += len(used)
        if len(used) == m * n:
            return flash_count, step + 1

    return flash_count, None


def part1(octopods: List[List[int]], steps: int = 100) -> int:
    return simulate_flashes(octopods, steps)[0]


def part2(octopods: List[List[int]], steps: int = 1000) -> int:
    sync_step = simulate_flashes(octopods, steps)[1]
    if sync_step is None:
        raise RuntimeError("Did not simulate enough steps.")
    return sync_step


def main() -> None:
    octopods: List[List[int]] = []
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        octopods = [[int(c) for c in line.strip()] for line in file]

    with timing("Part 1"):
        solution = part1(octopods)
    print(solution)

    with timing("Part 2"):
        solution = part2(octopods)
    print(solution)


if __name__ == "__main__":
    main()
