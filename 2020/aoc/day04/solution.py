import re
from typing import Dict, Iterator
from pathlib import Path

from aoc.util import timing


Passport = Dict[str, str]


def _good_int(s: str, num_digits: int = 4, min_val: int = 0, max_val: int = float('inf')) -> bool:
    return len(s) == num_digits and min_val <= int(s) <= max_val


def _good_height(s: str) -> bool:
    return (s.endswith('cm') and _good_int(s[:-2], 3, 150, 193)) or (s.endswith('in') and _good_int(s[:-2], 2, 59, 76))


VALIDATIONS = {
    'byr': lambda s: _good_int(s, 4, 1920, 2002),
    'iyr': lambda s: _good_int(s, 4, 2010, 2020),
    'eyr': lambda s: _good_int(s, 4, 2020, 2030),
    'hgt': _good_height,
    'hcl': lambda s: re.fullmatch('#[0-9a-f]{6}', s) is not None,
    'ecl': lambda s: s in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    'pid': lambda s: _good_int(s, 9)
}


def _passports_with_all_keys(passports: Iterator[Passport]) -> Iterator[Passport]:
    return filter(lambda p: set(VALIDATIONS.keys()).issubset(p), passports)


def part1(passports: Iterator[Passport]) -> int:
    return sum(map(lambda p: 1, _passports_with_all_keys(passports)))


def part2(passports: Iterator[Passport]) -> int:
    return sum(
        map(
            lambda p: all(VALIDATIONS.get(k, lambda s: True)(v) for k, v in p.items()),
            _passports_with_all_keys(passports),
        )
    )


def main() -> None:
    passports = []
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        for kcv_list in map(lambda x: x.split(), file.read().split('\n\n')):
            passports.append({k: v for k, v in map(lambda x: x.split(':'), kcv_list)})

    with timing("Part 1"):
        solution = part1(passports)
    print(solution)

    with timing("Part 2"):
        solution = part2(passports)
    print(solution)


if __name__ == "__main__":
    main()
