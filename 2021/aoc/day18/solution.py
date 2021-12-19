# I killed multiple hours on a typo part1, so we're not cleaning this up.
# The idea of representing things as a flat list instead of a tree is something
# I took from reddit because I thought it was cute to avoid building any sort
# of tree for this problem, but it does make the actual implementation ugly.

from math import ceil, floor
from pathlib import Path
from typing import List

from aoc.util import timing


class SFNumber:
    def __init__(self, numbers: List[str | int]) -> None:
        self.numbers: List[str | int] = numbers
        self._reduce()

    @staticmethod
    def from_str(numbers_str: str) -> None:
        numbers: List[str | int] = []
        for c in numbers_str:
            numbers.append(int(c) if c in "1234567890" else c)
        return SFNumber(numbers)

    def _explode(self, i: int) -> None:
        old_pair = self.numbers[i + 1], self.numbers[i + 3]

        try:
            left = next(
                j
                for j in range(i - 1, 0, -1)
                if isinstance(self.numbers[j], int)
            )
            self.numbers[left] += old_pair[0]
        except StopIteration:
            pass

        try:
            n = len(self.numbers)
            right = next(
                j for j in range(i + 4, n) if isinstance(self.numbers[j], int)
            )
            self.numbers[right] += old_pair[1]
        except StopIteration:
            pass

        # [a,b] -> 0
        self.numbers = self.numbers[:i] + [0] + self.numbers[i + 5 :]

    def _split(self, i: int) -> None:
        v = self.numbers[i]
        lo, hi = floor(v / 2), ceil(v / 2)
        # a -> [b,c]
        new_pair = ["[", lo, ",", hi, "]"]
        self.numbers = self.numbers[:i] + new_pair + self.numbers[i + 1 :]

    def _reduce(self) -> None:
        depth = 0
        for i, c in enumerate(self.numbers):
            if c == "[":
                depth += 1
                if depth == 5:
                    self._explode(i)
                    self._reduce()
                    return
            elif c == "]":
                depth -= 1

        for i, c in enumerate(self.numbers):
            if not isinstance(c, int):
                continue
            if c >= 10:
                self._split(i)
                self._reduce()
                return

    def __add__(self, other: "SFNumber") -> "SFNumber":
        return SFNumber(["["] + self.numbers + [","] + other.numbers + ["]"])

    def __repr__(self) -> str:
        s = "SF(" + "".join(str(c) for c in self.numbers) + ")"
        return s

    def magnitude(self) -> int:
        s = "".join(str(c) for c in self.numbers)
        return eval(
            s.replace("[", "3*(").replace(",", ")+2*(").replace("]", ")")
        )


def part1(sf_numbers: List[SFNumber]) -> int:
    number = sf_numbers[0]
    for other in sf_numbers[1:]:
        number = number + other

    return number.magnitude()


def part2(numbers: List[SFNumber]) -> int:
    max_mag = 0
    for a in numbers:
        for b in numbers:
            if a.numbers == b.numbers:
                continue
            max_mag = max(max_mag, (a + b).magnitude())
    return max_mag


def main() -> None:
    sf_numbers: List[SFNumber] = []
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        for line in file:
            sf_numbers.append(SFNumber.from_str(line.strip()))

    with timing("Part 1"):
        solution = part1(sf_numbers)
    print(solution)

    with timing("Part 2"):
        solution = part2(sf_numbers)
    print(solution)


if __name__ == "__main__":
    main()
