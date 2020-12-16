from typing import List, Tuple, Union, Dict
from pathlib import Path
import functools

from advent_of_code.util import timing

Rule = Tuple[Tuple[int, int], Tuple[int, int]]
Ticket = Tuple[int, ...]


def _valid_for_rule(num: int, rule: Rule) -> bool:
    return (rule[0][0] <= num <= rule[0][1]) or (rule[1][0] <= num <= rule[1][1])


def _valid_ticket(ticket: Ticket, rules: Dict[str, Rule]) -> int:
    # Returns with int error code.  Assumes at most one bad field.
    for num in ticket:
        good = False
        for _, rule in rules.items():
            good = good or _valid_for_rule(num, rule)
        if not good:
            return num
    return 0


def part1(rules: Dict[str, Rule], nearby: List[Ticket]) -> int:
    return sum(_valid_ticket(ticket, rules) for ticket in nearby)


def part2(rules: Dict[str, Rule], nearby: List[Ticket], you: Ticket) -> int:
    truth_tables = {k: [True] * len(rules) for k in rules}
    for t in nearby:
        if _valid_ticket(t, rules) != 0:
            # Completely invalid ticket.
            continue
        # Check each ticket value against each field rule and update truth table.
        for i, num in enumerate(t):
            for k, rule in rules.items():
                truth_tables[k][i] = truth_tables[k][i] and _valid_for_rule(num, rule)

    # Iteratively remove the field which has only one possible choice.  Simplified problem input.
    correct_mapping = {}
    while truth_tables:
        found_k = None
        found_idx = None
        for k, truth_table in truth_tables.items():
            if sum(truth_tables[k]) == 1:
                found_idx = next(v for v in enumerate(truth_table) if v[1] is True)[0]
                found_k = k
                break
        correct_mapping[found_k] = found_idx
        del truth_tables[found_k]
        for k in truth_tables:
            # None of the other fields can be this index.
            truth_tables[k][found_idx] = False

    return functools.reduce(
        lambda a, b: a * b,
        (you[i] for k, i in correct_mapping.items() if k.startswith("departure")),
    )


def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        ticket_info = file.read()

    rules_str, you_str, nearby_str = ticket_info.split('\n\n')

    rules: Dict[str, Rule] = {}
    for line in rules_str.split('\n'):
        key, range_or_range = line.strip().split(':')
        range1, range2 = range_or_range.strip().split(' or ')
        rules[key] = (
            tuple(map(int, range1.split('-'))),
            tuple(map(int, range2.split('-'))),
        )

    nearby: List[Ticket] = []
    for line in nearby_str.split('\n')[1:-1]:
        nearby.append(tuple(map(int, line.strip().split(','))))

    you: Ticket = tuple(map(int, you_str.split('\n')[1].strip().split(',')))

    with timing("Part 1"):
        solution = part1(rules, nearby)
    print(solution)

    with timing("Part 2"):
        solution = part2(rules, nearby, you)
    print(solution)


if __name__ == "__main__":
    main()
