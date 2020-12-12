from typing import List, Tuple
from pathlib import Path

from advent_of_code.util import timing

Instruction = Tuple[str, int]


class Vec:
    """A limited 2D vector class to avoid external dependencies."""
    def __init__(self, x=0, y=0):
        self._vec = (x, y)

    def __getitem__(self, item):
        return self._vec[item]

    def __add__(self, other):
        return Vec(self[0] + other[0], self[1] + other[1])

    def __rmul__(self, other):
        return Vec(other * self[0], other * self[1])


_DIRECTIONS = {
    'N': Vec(0, 1),
    'S': Vec(0, -1),
    'E': Vec(-1, 0),
    'W': Vec(1, 0),
}


def _rotate_by_multiple_of_90(vector: Vec, right_or_left: str, angle: int) -> Vec:
    x, y = vector[0], vector[1]
    while angle != 0:
        if right_or_left == 'R':
            x, y = -y, x
        else:
            x, y = y, -x
        angle -= 90
    return Vec(x, y)


def _simulate(instructions: List[Instruction], heading: Vec, is_part2: bool = False) -> int:
    position = Vec(0, 0)
    for inst, c in instructions:
        if inst in ['N', 'S', 'E', 'W']:
            if is_part2:
                heading += c * _DIRECTIONS[inst]
            else:
                position += c * _DIRECTIONS[inst]
        elif inst == 'F':
            position += c * heading
        else:
            heading = _rotate_by_multiple_of_90(heading, inst, c)
    return abs(position[0]) + abs(position[1])


def part1(instructions: List[Instruction]) -> int:
    return _simulate(instructions, heading=_DIRECTIONS['E'], is_part2=False)


def part2(instructions: List[Instruction]) -> int:
    return _simulate(instructions, heading=Vec(-10, 1), is_part2=True)


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
