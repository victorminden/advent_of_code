from pathlib import Path
from typing import List, Set, Tuple, TypeAlias

from aoc.util import timing


Marks: TypeAlias = Set[Tuple[int, int]]
Folds: TypeAlias = List[Tuple[int, int]]


def reflect(value: int, fold_point: int) -> int:
    return value - 2 * abs(fold_point - value) if value > fold_point else value


def fold(marks: Marks, folds: Folds) -> Marks:
    for (dir, coord) in folds:
        next_marks = set()
        for (x, y) in marks:
            if dir == 0:
                x = reflect(x, coord)
            else:
                y = reflect(y, coord)
            next_marks.add((x, y))
        marks = next_marks
    return next_marks


def part1(marks: Marks, folds: Folds) -> int:
    return len(fold(marks, folds[0:1]))


def print_marks(marks: Marks) -> None:
    xmin = min(x for (x, _) in marks)
    xmax = max(x for (x, _) in marks)
    ymin = min(y for (_, y) in marks)
    ymax = max(y for (_, y) in marks)

    print("")
    for y in range(ymin, ymax + 1):
        line = ""
        for x in range(xmin, xmax + 1):
            line += "#" if (x, y) in marks else "."
        print(line)
    print("")


def part2(marks: Marks, folds: Folds) -> None:
    print_marks(fold(marks, folds))


def main() -> None:
    marks = set()
    folds = []
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        for line in file:
            if "," in line:
                x, y = line.strip().split(",")
                marks.add((int(x), int(y)))
            elif "fold" in line:
                dir, coord = line.strip().split()[-1].split("=")
                folds.append((0 if dir == "x" else 1, int(coord)))

    with timing("Part 1"):
        solution = part1(marks, folds)
    print(solution)

    with timing("Part 2"):
        solution = part2(marks, folds)
    print(solution)


if __name__ == "__main__":
    main()
