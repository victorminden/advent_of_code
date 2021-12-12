from collections import Counter
from pathlib import Path
from typing import List, Tuple, TypeAlias

from aoc.util import timing


def min_max(a: int, b: int) -> Tuple[int, int]:
    """Returns the min and max, in that order."""
    return min(a, b), max(a, b)


def sign(x: int) -> int:
    """Returns the sign of x, with sign(0) == 0."""
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


Point: TypeAlias = Tuple[int, int]


class LineSegment:
    """A class for representing line segments.

    The methods are only guaranteed to work properly for line segments that are
    horizontal, vertical, or 45 degrees, but no validation is performed.
    """

    def __init__(self, start: Point, end: Point) -> None:
        self._start = start
        self._end = end

    def is_axis_aligned(self) -> bool:
        """Returns True if the line is horizontal or vertical, else False."""
        return self._start[0] == self._end[0] or self._start[1] == self._end[1]

    def integer_points(self) -> List[Point]:
        """Returns a list of all integer points on the line segment.

        Only works on line segments that are horizontal, vertical, or 45
        degrees.
        """
        x, y = self._start
        xf, yf = self._end
        dx, dy = (sign(xf - x), sign(yf - y))
        points = [(x, y)]
        while (x, y) != (xf, yf):
            x += dx
            y += dy
            points.append((x, y))
        return points

    def __repr__(self) -> str:
        return f"LineSegment({self._start} -> {self._end})"


def str2line(file_line: str) -> LineSegment:
    """Creates a LineSegment from a string of the form "a,b -> c,d"."""
    start, end = file_line.strip().split(" -> ")
    start = tuple(map(int, start.split(",")))
    end = tuple(map(int, end.split(",")))
    return LineSegment(start, end)


def part1(lines: List[LineSegment]) -> int:
    counter = Counter()
    for line in filter(lambda x: x.is_axis_aligned(), lines):
        counter.update(line.integer_points())
    return sum(1 for k in counter if counter[k] > 1)


def part2(lines: List[LineSegment]) -> int:
    counter = Counter()
    for line in lines:
        counter.update(line.integer_points())
    return sum(1 for k in counter if counter[k] > 1)


def main() -> None:
    lines: List[LineSegment] = []
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        lines = list(map(str2line, file.readlines()))

    with timing("Part 1"):
        solution = part1(lines)
    print(solution)

    with timing("Part 2"):
        solution = part2(lines)
    print(solution)


if __name__ == "__main__":
    main()
