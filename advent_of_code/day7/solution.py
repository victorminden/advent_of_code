from typing import Set
from pathlib import Path
import string
from collections import defaultdict

from advent_of_code.util import timing


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
        rules = [line.strip() for line in file]

    bags = defaultdict(list)
    for line in rules:
        # Build the reverse graph.
        src, dsts = line.split("contain")
        src = src.strip()
        dsts = dsts.split(",")
        for dst in dsts:
            dst = dst.translate(str.maketrans('', '', string.punctuation))
            n, d = dst.split(maxsplit=1)
            d = d.strip()
            if d.endswith('s'):
                d = d[:-1]

            bags[d].append(src[:-1])

    searched = set()
    can_hold = set()
    to_process = ["shiny gold bag"]
    while to_process:
        bag = to_process[-1]
        to_process = to_process[:-1]
        searched.add(bag)
        nxt = bags[bag]
        if nxt:
            can_hold.update(nxt)
            to_process.extend([b for b in nxt if b not in searched])
    print(len(can_hold))

    # Part 2
    bags = defaultdict(list)
    for line in rules:
        # Build the reverse graph.
        src, dsts = line.split("contain")
        src = src.strip()
        dsts = dsts.split(",")
        if dsts[0].strip() == "no other bags.":
            continue
        for dst in dsts:
            dst = dst.translate(str.maketrans('', '', string.punctuation))
            n, d = dst.split(maxsplit=1)
            d = d.strip()
            if d.endswith('s'):
                d = d[:-1]
            bags[src[:-1]].append((int(n), d))
    print(hold_how_many("shiny gold bag", bags) - 1)


def hold_how_many(bag: str, bags) -> int:
    if not bags[bag]:
        return 1
    return 1 + sum(n * hold_how_many(b, bags) for (n, b) in bags[bag])


if __name__ == "__main__":
    main()
