from typing import Iterable, List, Tuple
from pathlib import Path

from aoc.util import timing

Rule = Tuple[int, int, str]


def parse_rule(rule: str) -> Rule:
    min_count, max_count = map(int, rule.split()[0].split('-'))
    return min_count, max_count, rule[-1]


def part1(passwords: Iterable[Tuple[Rule, str]]) -> int:
    return sum((i <= password.count(a) <= j for (i, j, a), password in passwords))


def part2(passwords: Iterable[Tuple[Rule, str]]) -> int:
    # Rule was expressed in 1-based indexing.
    return sum(((password[i - 1] == a) != (password[j - 1] == a) for (i, j, a), password in passwords))


def main() -> None:
    passwords: List[Tuple[Rule, str]] = []
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        for line in file:
            rule, password = line.split(':')
            passwords.append((parse_rule(rule), password.lstrip()))

    with timing("Part 1"):
        solution = part1(passwords)
    print(solution)

    with timing("Part 2"):
        solution = part2(passwords)
    print(solution)


if __name__ == "__main__":
    main()
