from typing import List, Tuple, Optional
from pathlib import Path
from copy import deepcopy
import itertools


from aoc.util import timing

Neighbor = Tuple[int, int]
SeatMap = List[List[str]]
NeighborMap = List[List[Neighbor]]

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


def _neighbors_of_ij(seat_map: SeatMap, i: int, j: int, max_scale: int) -> List[Neighbor]:
    neighbors = []
    m, n = len(seat_map), len(seat_map[0])
    for delta_i, delta_j in _NEIGHBORS_OFFSETS:
        # Use max_scale + 1 for inclusive range
        for scale in range(1, max_scale + 1):
            ii = i + scale * delta_i
            jj = j + scale * delta_j
            if ii not in range(m) or jj not in range(n):
                # Off the edge.
                break
            if seat_map[ii][jj] == 'L':
                # Found the first seat in this direction.
                neighbors.append((ii, jj))
                break
    return neighbors


def _neighbor_map(seat_map: SeatMap, max_scale: Optional[int] = None) -> NeighborMap:
    neighbor_map = [[] for _ in seat_map]
    m, n = len(seat_map), len(seat_map[0])
    if max_scale is None:
        max_scale = max(m, n)
    for i, j in itertools.product(range(m), range(n)):
        neighbor_map[i].append(_neighbors_of_ij(seat_map, i, j, max_scale))
    return neighbor_map


def part1(seat_map: SeatMap) -> int:
    return _simulate(seat_map, neighbor_map=_neighbor_map(seat_map, max_scale=1), occupancy_limit=4)


def _simulate(seat_map: SeatMap, neighbor_map: NeighborMap, occupancy_limit: int) -> int:
    m, n = len(seat_map), len(seat_map[0])
    seat_map = deepcopy(seat_map)
    new_seats = deepcopy(seat_map)
    while True:
        for i, j in itertools.product(range(m), range(n)):
            num_occupied = sum(seat_map[nbr_i][nbr_j] == '#' for nbr_i, nbr_j in neighbor_map[i][j])
            if num_occupied == 0 and seat_map[i][j] == 'L':
                # Coming.
                new_seats[i][j] = '#'
            elif num_occupied >= occupancy_limit and seat_map[i][j] == '#':
                # Going.
                new_seats[i][j] = 'L'
            else:
                new_seats[i][j] = seat_map[i][j]
        if new_seats == seat_map:
            break
        seat_map, new_seats = new_seats, seat_map
    return sum(seat_map[i][j] == '#' for i in range(m) for j in range(n))


def part2(seat_map: SeatMap) -> int:
    return _simulate(seat_map, neighbor_map=_neighbor_map(seat_map, max_scale=None), occupancy_limit=5)


def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        seat_map = [list(line.strip()) for line in file]

    with timing("Part 1"):
        solution = part1(seat_map)
    print(solution)

    with timing("Part 2"):
        solution = part2(seat_map)
    print(solution)


if __name__ == "__main__":
    main()
