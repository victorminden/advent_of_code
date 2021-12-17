from itertools import product
from pathlib import Path
from typing import Dict, Optional, Tuple, TypeAlias

from aoc.util import timing

Target: TypeAlias = Dict[str, Tuple[int, int]]


def apex_height_before_target(u: int, v: int, target: Target) -> Optional[int]:
    """Returns the apex height if the target is hit, or None."""
    # This is pretty ugly in my book, but it is Friday and I'm not going to
    # clean it up.
    ymin, ymax = target["y"]
    xmin, xmax = target["x"]
    x, y = (0, 0)
    apex = 0
    while y > ymin:
        x += u
        y += v
        apex = max(apex, y)
        u -= 1 if u != 0 else 0
        v -= 1
        if ymin <= y <= ymax and xmin <= x <= xmax:
            return apex


def part1(target: Target) -> int:
    _, xmax = target["x"]
    # Make the assumption that target x range is positive.
    # Can fix this later but it is true for us and example.
    # Also assume apex height is greater than -999, and that
    # the maximum vertical velocity possible is 500.
    # We could bound these things formally, but it is almost the weekend.
    max_y = -999
    for u in range(xmax + 1):
        for v in reversed(range(500)):
            if (new_y := apex_height_before_target(u, v, target)) is not None:
                max_y = max(max_y, new_y)
                break
    return max_y


def part2(target: Target) -> int:
    good_velocities = set()
    _, xmax = target["x"]
    ymin, _ = target["y"]
    # Make the assumption that target x range is positive.
    # Can fix this later but it is true for us and example.
    # Also assume the maximum vertical velocity possible is 500.
    # We could bound this things formally, but it is almost the weekend.
    for u in range(xmax + 1):
        for v in reversed(range(ymin, 500)):
            if apex_height_before_target(u, v, target) is not None:
                good_velocities.add((u, v))
    return len(good_velocities)


def main() -> None:
    target = None
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        xyvals = file.readline().strip().split(":")[1].strip()
        xvals, yvals = xyvals.split(", ")
        xmin, xmax = xvals.strip("x=").split("..")
        ymin, ymax = yvals.strip("y=").split("..")
        target = {
            "x": (int(xmin), int(xmax)),
            "y": (int(ymin), int(ymax)),
        }

    with timing("Part 1"):
        solution = part1(target)
    print(solution)

    with timing("Part 2"):
        solution = part2(target)
    print(solution)


if __name__ == "__main__":
    main()
