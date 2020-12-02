from typing import Iterable, List
from collections import Counter
from pathlib import Path

from advent_of_code.util import timing


class Rule:
    def __init__(self, rule: str) -> None:
        self._letter = rule[-1]
        min_count, max_count = rule.split()[0].split('-')
        self._min = int(min_count)
        self._max = int(max_count)

    def is_valid(self, password: str) -> bool:
        count = Counter(password)[self._letter]
        return self._min <= count <= self._max


class SecondRule(Rule):
    def is_valid(self, password: str) -> bool:
        # Extra space in input --> don't worry about off-by-one in 1-indexed min/max.
        count = Counter((password[self._min], password[self._max]))[self._letter]
        return count == 1


def part1(passwords: Iterable[List[str]]) -> int:
    return sum((Rule(rule).is_valid(password) for rule, password in passwords))


def part2(passwords: Iterable[List[str]]) -> int:
    return sum((SecondRule(rule).is_valid(password) for rule, password in passwords))


def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        passwords = [line.split(':') for line in file]

    with timing("Part 1"):
        solution = part1(passwords)
    print(solution)

    with timing("Part 2"):
        solution = part2(passwords)
    print(solution)


if __name__ == "__main__":
    main()
