from typing import List, Tuple
from pathlib import Path

from aoc.util import timing


Expression = str


class DumbInt:
    # Swap addition and multiplication so that they have opposite precedence.
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        self.val *= other.val
        return self

    def __mul__(self, other):
        self.val += other.val
        return self


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


def _evaluate_expression_part2(expression: Expression) -> int:
    # Convert + to * and convert * to +.
    expression_flipped = expression.translate(str.maketrans("+*", "*+"))
    for i in range(10):
        expression_flipped = expression_flipped.replace(str(i), 'DumbInt(' + str(i) + ')')
    return eval(expression_flipped).val


def part2(expressions: List[Expression]) -> int:
    return sum(_evaluate_expression_part2(e) for e in expressions)


def main() -> None:
    expressions: List[Expression] = []
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        for line in file:
            expressions.append(line.strip())

    with timing("Part 1"):
        solution = part1(expressions)
    print(solution)

    with timing("Part 2"):
        solution = part2(expressions)
    print(solution)


if __name__ == "__main__":
    main()
