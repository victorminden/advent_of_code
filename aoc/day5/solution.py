from typing import Set
from pathlib import Path

from aoc.util import timing


BoardingPass = str
Seat = int


def _pass_to_seat(boarding_pass: BoardingPass) -> Seat:
    # Improvement based on the observation that the final seat number is just the implied binary number in decimal.
    # Thanks to @tan.nguyen for pointing this out in discussion.
    return int(boarding_pass.translate(boarding_pass.maketrans('FBLR', '0101')), base=2)


def part2(seats: Set[Seat]) -> Seat:
    return next(i + 1 for i in seats if i + 1 not in seats)


def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        boarding_passes = [line.strip() for line in file]

    with timing("Part 1"):
        solution = max(map(_pass_to_seat, boarding_passes))
    print(solution)

    with timing("Part 2"):
        solution = part2(set(map(_pass_to_seat, boarding_passes)))
    print(solution)


if __name__ == "__main__":
    main()
