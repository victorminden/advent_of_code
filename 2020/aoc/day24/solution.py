from typing import List, Tuple, Set
from pathlib import Path
import collections

import numpy as np

from aoc.util import timing


HexPath = List[str]
TileCoord = Tuple[int, int, int]

_DELTA_R = {
    'e': np.array([1, -1 , 0]),
    'w': np.array([-1, 1 , 0]),
    'ne': np.array([1, 0 , -1]),
    'sw': np.array([-1, 0 , 1]),
    'nw': np.array([0, 1 , -1]),
    'se': np.array([0, -1 , 1]),
}


def part1(paths: List[HexPath]) -> int:
    return len(_initial_black_tiles(paths))


def _initial_black_tiles(paths: List[HexPath]) -> Set[TileCoord]:
    black_tiles = set()
    for path in paths:
        coord = tuple(sum(_DELTA_R[i] for i in path))
        if coord in black_tiles:
            black_tiles.remove(coord)
        else:
            black_tiles.add(coord)
    return black_tiles


def part2(paths: List[HexPath], num_days=100) -> int:
    black_tiles = _initial_black_tiles(paths)

    for day in range(num_days):
        neighbors_of_old_black_tiles = collections.defaultdict(int)
        for tile in black_tiles:
            for neighbor in _neighbors(tile):
                neighbors_of_old_black_tiles[neighbor] += 1

        new_black_tiles = set()
        for tile, count in neighbors_of_old_black_tiles.items():
            if count == 2 and tile not in black_tiles:
                new_black_tiles.add(tile)

        new_white_tiles = set()
        for tile in black_tiles:
            if tile not in neighbors_of_old_black_tiles or neighbors_of_old_black_tiles[tile] > 2:
                new_white_tiles.add(tile)

        black_tiles -= new_white_tiles
        black_tiles |= new_black_tiles

    return len(black_tiles)


def _neighbors(tile: TileCoord):
    return map(tuple, [np.array(tile) + dr for dr in _DELTA_R.values()])


def main() -> None:
    paths = []
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        for line in file:
            path = line.replace('e', 'e ').replace('w', 'w ').strip().split()
            paths.append(path)

    with timing("Part 1"):
        solution = part1(paths)
    print(solution)

    with timing("Part 2"):
        solution = part2(paths, num_days=100)
    print(solution)


if __name__ == "__main__":
    main()
