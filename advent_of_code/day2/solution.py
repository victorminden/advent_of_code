from typing import Iterable, List, Tuple, Generator
from pathlib import Path

from advent_of_code.util import timing


def parse_rule(rule: str) -> Tuple[int, int, str]:
    min_count, max_count = map(int, rule.split()[0].split('-'))
    return min_count, max_count, rule[-1]


def part1_generator(passwords: Iterable[List[str]]) -> Generator[bool, Iterable[List[str]], None]:
    for rule, password in passwords:
        i, j, a = parse_rule(rule)
        yield i <= password.count(a) <= j


def part2_generator(passwords: Iterable[List[str]]) -> Generator[bool, Iterable[List[str]], None]:
    for rule, password in passwords:
        i, j, a = parse_rule(rule)
        # XOR.
        yield (password[i] == a) != (password[j] == a)


def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        passwords = [line.split(':') for line in file]

    with timing("Part 1"):
        solution = sum(part1_generator(passwords))
    print(solution)

    with timing("Part 2"):
        solution = sum(part2_generator(passwords))
    print(solution)


if __name__ == "__main__":
    main()
