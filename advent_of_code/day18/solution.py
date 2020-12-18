from typing import List, Tuple, Dict
from pathlib import Path
import copy
import itertools
import collections

from advent_of_code.util import timing


Expression = str


def _evaluate_expression(expression: Expression) -> Tuple[int, Expression]:
    # Assume no two-character tokens.
    tokens = expression.replace(" ", "")
    value = 0
    last_op = '+'
    while tokens:
        token, tokens = tokens[0], tokens[1:]
        if token in ('+', '*'):
            last_op = token
            continue

        if token == '(':
            next_value, tokens = _evaluate_expression(tokens)
        elif token.endswith(')'):
            # Close expression.
            return value, tokens
        else:
            next_value = token
        if last_op == '+':
            value += int(next_value)
        elif last_op == '*':
            value *= int(next_value)
            
    return value, tokens


def part1(expressions: List[Expression]) -> int:
    return sum(_evaluate_expression(e)[0] for e in expressions)


def part2(expressions: List[Expression]) -> int:
    return 0


def main() -> None:
    expressions: List[Expression] = []
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        for line in file:
            expressions.append(line.strip())

    with timing("Part 1"):
        solution = part1(expressions)
    print(solution)

    # with timing("Part 2"):
    #     solution = part2(initial_state)
    # print(solution)


if __name__ == "__main__":
    main()
