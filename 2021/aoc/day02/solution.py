from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

from aoc.util import timing


@dataclass
class SubmarineState:
    x: int = 0
    y: int = 0
    aim: int = 0


def part1(directions: List[Tuple[str, int]]) -> int:
    state = SubmarineState()
    for (dir, scale) in directions:
        match dir:
            case "forward":
                state.x += scale
            case "down":
                state.y += scale
            case "up":
                state.y -= scale
    return state.x * state.y


def part2(directions: List[Tuple[str, int]]) -> int:
    state = SubmarineState()
    for (dir, scale) in directions:
        match dir:
            case "forward":
                state.x += scale
                state.y += scale * state.aim
            case "down":
                state.aim += scale
            case "up":
                state.aim -= scale
    return state.x * state.y


def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        directions = (line.split() for line in file)
        directions = [(a, int(b)) for (a, b) in directions]

    with timing("Part 1"):
        solution = part1(directions)
    print(solution)

    with timing("Part 2"):
        solution = part2(directions)
    print(solution)


if __name__ == "__main__":
    main()
