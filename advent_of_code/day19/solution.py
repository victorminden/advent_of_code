from typing import List, Dict
import copy
from pathlib import Path
import re

from advent_of_code.util import timing


def part1(rules: Dict[str, str], messages: List[str]) -> int:
    rules = copy.deepcopy(rules)

    def has_digit(s: str) -> bool:
        return any(c.isdigit() for c in s)

    while has_digit(rules["0"]):
        good_key, good_value = next((k, v) for (k, v) in rules.items() if not has_digit(v))
        for k, v in rules.items():
            rules[k] = re.sub(rf"\b{good_key}\b", f"({good_value})", v)
        del rules[good_key]
        
    pattern = re.compile(rules["0"].replace('"', '').replace(' ', ''))
    return sum(pattern.fullmatch(m) is not None for m in messages)


def part2(rules: Dict[str, str], messages: List[str]) -> int:
    rules = copy.deepcopy(rules)
    rules["8"] = "42 | 42 42 | 42 42 42 | 42 42 42 42 | 42 42 42 42 42 | 42 42 42 42 42 42 | 42 42 42 42 42 42 42"
    rules["11"] = "42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31 | 42 42 42 42 42 31 31 31 31 31"
    return part1(rules, messages)


def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        rules_str, messages_str = file.read().split('\n\n')

    rules = {}
    for rule in rules_str.split("\n"):
        k, v = rule.split(":")
        rules[k] = v.strip()

    messages = messages_str.strip().split("\n")

    with timing("Part 1"):
        solution = part1(rules, messages)
    print(solution)

    with timing("Part 2"):
        solution = part2(rules, messages)
    print(solution)


if __name__ == "__main__":
    main()
