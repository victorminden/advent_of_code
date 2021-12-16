from heapq import heappop, heappush
from itertools import product
from pathlib import Path
from typing import List, TypeAlias

from aoc.util import timing

Grid: TypeAlias = List[List[int]]


def part1(grid: Grid) -> int:
    m = len(grid)
    n = len(grid[0])
    costs = {(i, j): float("inf") for i in range(m) for j in range(n)}
    costs[(0, 0)] = 0
    unvisited = []
    for v in costs:
        heappush(unvisited, (costs[v], v))

    while unvisited:
        cost, u = heappop(unvisited)
        if u == (m - 1, n - 1):
            return cost
        ui, uj = u
        for v in ((ui - 1, uj), (ui + 1, uj), (ui, uj - 1), (ui, uj + 1)):
            vi, vj = v
            if not (0 <= vi < m) or not (0 <= vj < n):
                continue
            if (new_cost := cost + grid[vi][vj]) < costs[v]:
                costs[v] = new_cost
                # Cheat: don't try to modify a priority queue, just add a new
                # entry with the lower cost.  Modifying a priority queue leads
                # you down a bad road.  Shout out to some random reddit comment
                # that suggested this.
                heappush(unvisited, (new_cost, v))


def part2(grid: Grid, k: int = 5) -> int:
    m = len(grid)
    n = len(grid[0])
    larger_grid: Grid = [[None for _ in range(k * n)] for _ in range(k * m)]
    for copy_i, copy_j in product(range(k), range(k)):
        for i, j in product(range(m), range(n)):
            new_i, new_j = (i + copy_i * m, j + copy_j * n)
            new_v = grid[i][j] + copy_i + copy_j
            while new_v > 9:
                new_v -= 9
            larger_grid[new_i][new_j] = new_v

    return part1(larger_grid)


def main() -> None:
    grid: Grid = []
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        for line in file:
            grid.append(list(map(int, line.strip())))

    with timing("Part 1"):
        solution = part1(grid)
    print(solution)

    with timing("Part 2"):
        solution = part2(grid)
    print(solution)


if __name__ == "__main__":
    main()
