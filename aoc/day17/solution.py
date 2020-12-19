from typing import List, Tuple, Dict
from pathlib import Path
import copy
import itertools
import collections

from aoc.util import timing


Coordinate = Tuple[int, ...]


def _neighbors(coord: Coordinate, dim: int) -> List[Coordinate]:
    neighbors = []
    for nbr_offset in itertools.product((-1, 0, 1), repeat=dim):
        if all([i == 0 for i in nbr_offset]):
            continue
        neighbors.append(tuple((a + b for a, b in zip(coord, nbr_offset))))
    return neighbors


def pretty_print(state):
    x_min, x_max = min(k[0] for k in state), max(k[0] for k in state)
    y_min, y_max = min(k[1] for k in state), max(k[1] for k in state)
    z_min, z_max = min(k[2] for k in state), max(k[2] for k in state)

    for k in range(z_min, z_max + 1):
        for i in range(x_min, x_max + 1):
            print(list(state.get((i, j, k), False) for j in range(y_min, y_max + 1)))
        print('\n')


def part1(initial_state: Dict[Coordinate, bool], dim: int = 3) -> int:
    state = {}
    state.update(initial_state)
    for cycle in range(6):
        # Prune the explicit "False" cells.
        state = {k: v for k, v in state.items() if v}
        updates: Dict[Coordinate, bool] = {}
        for coord in state:
            neighbors = _neighbors(coord, dim)
            if state[coord]:
                updates[coord] = sum(state.get(nbr, False) for nbr in neighbors) in (2, 3)
            # The only possible dead cells that can be come alive are neighbors of alive cells, so just check all of
            # those now too.
            for nbr_coord in neighbors:
                neighbors2 = _neighbors(nbr_coord, dim)
                if sum(state.get(nbr, False) for nbr in neighbors2) == 3 and not state.get(nbr_coord, False):
                    updates[nbr_coord] = True
        state.update(updates)

    return sum(state.values())


def part2(initial_state: Dict[Coordinate, bool]) -> int:
    # This takes 90 seconds but who cares.
    initial_state_4d = {
        (i, j, k, 0): v for (i, j, k), v in initial_state.items()
    }
    return part1(initial_state_4d, dim=4)


def main() -> None:
    initial_state: Dict[Coordinate, bool] = {}
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        for i, line in enumerate(file):
            for j, c in enumerate(line.strip()):
                initial_state[(i, j, 0)] = (c == '#')

    with timing("Part 1"):
        solution = part1(initial_state)
    print(solution)

    with timing("Part 2"):
        solution = part2(initial_state)
    print(solution)


if __name__ == "__main__":
    main()
