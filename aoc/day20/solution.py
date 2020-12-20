from typing import List, Dict
import copy
from pathlib import Path
import re
from functools import reduce

from aoc.util import timing


def borders(tile):
    _borders = [
        tile[0, :].flatten(),
        tile[-1, :].flatten(),
        tile[:, 0].flatten(),
        tile[:, -1].flatten(),
    ]
    _borders.extend([np.flip(b, axis=0) for b in _borders])
    return _borders


def can_match(tile_a, tile_b):
    for ba in borders(tile_a):
        for bb in borders(tile_b):
            if np.all(ba == bb):
                return True
    return False


def part1(tiles) -> int:
    counts = {}
    for tile_idx in tiles:
        count = 0
        for other in tiles:
            if other == tile_idx:
                continue
            if can_match(tiles[tile_idx], tiles[other]):
                count += 1
        counts[tile_idx] = count
    return reduce(lambda a,b: a * b, [k for k,c in counts.items() if c == 2])



def part2() -> int:
    return 0


import numpy as np


def main() -> None:
    tiles = {}
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        for tile in file.read().split('\n\n')[:-1]:
            tile_id, tile_body = tile.split('\n', maxsplit=1)
            tile_id = int(tile_id.strip().split(' ')[1][:-1])
            tile_array = np.zeros((10, 10), dtype=np.bool)
            for i, row in enumerate(tile_body.split('\n')):
                for j, c in enumerate(row.strip()):
                    tile_array[i, j] = c == '#'
            tiles[tile_id] = tile_array

    with timing("Part 1"):
        solution = part1(tiles)
    print(solution)

    # with timing("Part 2"):
    #     solution = part2(rules, messages)
    # print(solution)


if __name__ == "__main__":
    main()
