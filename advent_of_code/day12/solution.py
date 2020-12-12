from typing import List, Tuple
from pathlib import Path
import numpy as np

from advent_of_code.util import timing

Instruction = Tuple[str, int]

_DIRECTIONS = {
    'N': np.array([0, 1]),
    'S': np.array([0, -1]),
    'E': np.array([-1, 0]),
    'W': np.array([1, 0]),
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
    position = np.array([0, 0], dtype=np.int64)
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
    waypoint_position = np.array([-10, 1], dtype=np.int64)
    ship_position = np.array([0, 0], dtype=np.int64)
    for inst, c in instructions:
        if inst in ['N', 'S', 'E', 'W']:
            waypoint_position += c * _DIRECTIONS[inst]
            continue
        displacement = waypoint_position - ship_position
        if inst == 'F':
            ship_position += c * displacement
            waypoint_position += c * displacement
            continue
        if inst == 'L':
            while c != 0:
                displacement[0], displacement[1] = displacement[1], -displacement[0]
                c -= 90
        elif inst == 'R':
            while c != 0:
                displacement[0], displacement[1] = -displacement[1], displacement[0]
                c -= 90
        waypoint_position = ship_position + displacement
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
