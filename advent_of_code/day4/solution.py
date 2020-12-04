import re
from pathlib import Path

from advent_of_code.util import timing


def _validate_digits(s, num_digits=4, min_val=0, max_val=float('inf')):
    return len(s) == num_digits and min_val <= int(s) <= max_val


def _validate_height(s):
    if s.endswith('cm'):
        return _validate_digits(s[:-2], 3, 150, 193)
    if s.endswith('in'):
        return _validate_digits(s[:-2], 2, 59, 76)
    return False


VALIDATIONS = {
    'byr': lambda s: _validate_digits(s, 4, 1920, 2002),
    'iyr': lambda s: _validate_digits(s, 4, 2010, 2020),
    'eyr': lambda s: _validate_digits(s, 4, 2020, 2030),
    'hgt': _validate_height,
    'hcl': lambda s: re.fullmatch('#[0-9a-f]{6}', s) is not None,
    'ecl': lambda s: s in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    'pid': lambda s: _validate_digits(s, 9)
}


def _passports_with_all_keys(passports):
    return filter(lambda p: set(VALIDATIONS.keys()).issubset(p), passports)


def part1(passports):
    return len(list(_passports_with_all_keys(passports)))


def part2(passports):
    return sum(
        map(
            lambda p: all(VALIDATIONS.get(k, lambda s: True)(v) for k, v in p.items()),
            _passports_with_all_keys(passports),
        )
    )


def main():
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
