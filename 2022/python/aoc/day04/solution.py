from pathlib import Path

from aoc.util import timing


def to_range(x):
    # Integer ranges in cpython are nice, so exploit that.
    lo, hi = x.split("-")
    return range(int(lo), int(hi) + 1)


def is_inside(a, b):
    return min(a) in b and max(a) in b


def overlaps(a, b):
    return min(a) in b or max(a) in b


def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        sections = []
        for line in file:
            a, b = line.strip().split(",")
            sections.append((to_range(a), to_range(b)))

    with timing("Part 1"):
        solution = sum(is_inside(a, b) or is_inside(b, a) for (a, b) in sections)
    print(solution)

    with timing("Part 2"):
        solution = sum(overlaps(a, b) or overlaps(b, a) for (a, b) in sections)
    print(solution)


if __name__ == "__main__":
    main()
