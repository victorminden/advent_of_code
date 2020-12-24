from typing import List
from pathlib import Path

import numpy as np

from aoc.util import timing


HexPath = List[str]


_DELTA_R = {
    'e': np.array([1, -1 , 0]),
    'w': np.array([-1, 1 , 0]),
    'ne': np.array([1, 0 , -1]),
    'sw': np.array([-1, 0 , 1]),
    'nw': np.array([0, 1 , -1]),
    'se': np.array([0, -1 , 1]),
}


def part1(paths: List[HexPath]) -> int:
    black_tiles = set()
    for path in paths:
        coord = tuple(sum(_DELTA_R[i] for i in path))
        if coord in black_tiles:
            black_tiles.remove(coord)
        else:
            black_tiles.add(coord)
    return len(black_tiles)


def part2() -> int:
    return 0


def main() -> None:
    paths = []
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        for line in file:
            path = line.replace('e', 'e ').replace('w', 'w ').strip().split()
            paths.append(path)

    with timing("Part 1"):
        solution = part1(paths)
    print(solution)

    # with timing("Part 2"):
    #     solution = part2(all_edges, all_ingredients, all_allergens)
    # print(solution)


if __name__ == "__main__":
    main()
