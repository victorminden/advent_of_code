from typing import Set, Tuple
from pathlib import Path
import collections

from aoc.util import timing


def part1(deck1, deck2) -> int:
    while deck1 and deck2:
        c1, c2 = deck1.popleft(), deck2.popleft()
        if c1 > c2:
            deck1.extend([c1, c2])
        else:
            deck2.extend([c2, c1])
    winning_deck = deck1 if deck1 else deck2

    return sum((i + 1) * c for i, c in enumerate(reversed(winning_deck)))


def part2() -> int:
    return 0


def main() -> None:
    deck1 = collections.deque()
    deck2 = collections.deque()
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        file.readline()
        for line in file:
            if line == '\n':
                break
            deck1.append(int(line))
        file.readline()
        for line in file:
            if line == '\n':
                break
            deck2.append(int(line))
    with timing("Part 1"):
        solution = part1(deck1, deck2)
    print(solution)

    with timing("Part 2"):
        solution = part2()
    print(solution)


if __name__ == "__main__":
    main()
