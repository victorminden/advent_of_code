from typing import List, Tuple
from pathlib import Path

from advent_of_code.util import timing

Instruction = Tuple[str, int]


class Vec:
    def __init__(self, x=0, y=0):
        self._vec = [x, y]

    def __getitem__(self, item):
        return self._vec[item]

    def __setitem__(self, key, value):
        self._vec[key] = value

    def __add__(self, other):
        return Vec(self[0] + other[0], self[1] + other[1])

    def __sub__(self, other):
        return Vec(self[0] - other[0], self[1] - other[1])

    def __rmul__(self, other):
        return Vec(other * self[0], other * self[1])


_DIRECTIONS = {
    'N': Vec(0, 1),
    'S': Vec(0, -1),
    'E': Vec(-1, 0),
    'W': Vec(1, 0),
}

_MAP_PLUS_90 = {
    'N': 'E',
    'S': 'W',
    'E': 'S',
    'W': 'N'
}

_MAP_MINUS_90 = {
    'N': 'W',
    'S': 'E',
    'E': 'N',
    'W': 'S'
}


def part1(instructions: List[Instruction]) -> int:
    position = Vec(0, 0)
    heading = 'E'
    for inst, c in instructions:
        if inst in ['N', 'S', 'E', 'W']:
            position += c * _DIRECTIONS[inst]
        elif inst == 'F':
            position += c * _DIRECTIONS[heading]
        elif inst == 'L':
            while c != 0:
                heading = _MAP_MINUS_90[heading]
                c -= 90
        elif inst == 'R':
            while c != 0:
                heading = _MAP_PLUS_90[heading]
                c -= 90
    return abs(position[0]) + abs(position[1])


def part2(instructions: List[Instruction]) -> int:
    heading = Vec(-10, 1)
    ship_position = Vec(0, 0)
    for inst, c in instructions:
        if inst in ['N', 'S', 'E', 'W']:
            heading += c * _DIRECTIONS[inst]
            continue
        if inst == 'F':
            ship_position += c * heading
            continue
        if inst == 'L':
            while c != 0:
                heading[0], heading[1] = heading[1], -heading[0]
                c -= 90
        elif inst == 'R':
            while c != 0:
                heading[0], heading[1] = -heading[1], heading[0]
                c -= 90
    return abs(ship_position[0]) + abs(ship_position[1])


def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        instructions = [(line[0], int(line[1:])) for line in file]

    with timing("Part 1"):
        solution = part1(instructions)
    print(solution)

    with timing("Part 2"):
        solution = part2(instructions)
    print(solution)


if __name__ == "__main__":
    main()
