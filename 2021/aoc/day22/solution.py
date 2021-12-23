from dataclasses import dataclass
from itertools import product
from pathlib import Path
from typing import List, Optional, Set, Tuple

from aoc.util import timing


@dataclass
class Region:
    xmin: int = 0
    xmax: int = 0
    ymin: int = 0
    ymax: int = 0
    zmin: int = 0
    zmax: int = 0

@dataclass
class Instruction:
    is_on: bool = False
    region: Region = None


def part1(instructions: List[Instruction]) -> int:
    lit_cubes: Set[Tuple[int, int, int]] = set()
    for i in instructions:
        r = i.region
        if not (-50 <= r.xmin <= 50 and -50 <= r.xmax <= 50):
            continue
        if not (-50 <= r.ymin <= 50 and -50 <= r.ymax <= 50):
            continue
        if not (-50 <= r.zmin <= 50 and -50 <= r.zmax <= 50):
            continue

        xr = range(r.xmin, r.xmax + 1)
        yr = range(r.ymin, r.ymax + 1)
        zr = range(r.zmin, r.zmax + 1)
        for (x, y, z) in product(xr, yr, zr):
            if i.is_on:
                lit_cubes.add((x, y, z))
            else:
                lit_cubes -= {(x, y, z)}
    return len(lit_cubes)


def intersect(r: Region, s: Region) -> Optional[Region]:
    t = Region(
        max(r.xmin, s.xmin), min(r.xmax, s.xmax),
        max(r.ymin, s.ymin), min(r.ymax, s.ymax),
        max(r.zmin, s.zmin), min(r.zmax, s.zmax))
    # If you forget to check that the regions actually intersect then you are
    # going to have a bad time.
    if not t.xmin <= t.xmax or not t.ymin <= t.ymax or not t.zmin <= t.zmax:
        return None
    return t


def volume(r: Region) -> int:
    return (r.xmax - r.xmin + 1) * (r.ymax - r.ymin + 1) * (r.zmax - r.zmin + 1)


def part2(instructions: List[Instruction]) -> int:
    # If you try to use a set instead of a list you are going to have a bad
    # time.
    regions: List[Tuple[int, Region]] = []
    for i in instructions:
        updated_regions = regions.copy()
        r = i.region

        # Adds a positive region if the region is on, neglect to add any region
        # if the region is off.  Don't explicitly add negative regions here or
        # you're going to have a bad time.
        if i.is_on:
            updated_regions.append((1, r))

        for weight, old_r in regions:
            # If the region from the instruction intersects an old region that
            # exists, insert a "neutralizing" region that flips the weight of
            # the contribution from the old region.  Essentially, introduce the
            # idea of negative cubes.
            if new_region := intersect(r, old_r):
                updated_regions.append((-weight, new_region))

        regions = updated_regions

    size = 0
    for weight, r in regions:
        size += weight * volume(r)
    return size


def main() -> None:
    instructions = []
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        for line in file:
            on_off, region = line.split()
            is_on = on_off == 'on'
            x_region, y_region, z_region = region.split(',')
            xmin, xmax = x_region.split('..')
            xmin, xmax = int(xmin[2:]), int(xmax)
            ymin, ymax = y_region.split('..')
            ymin, ymax = int(ymin[2:]), int(ymax)
            zmin, zmax = z_region.split('..')
            zmin, zmax = int(zmin[2:]), int(zmax)
            region = Region(xmin, xmax, ymin, ymax, zmin, zmax)
            instructions.append(Instruction(is_on, region))

    with timing("Part 1"):
        solution = part1(instructions)
    print(solution)

    with timing("Part 2"):
        solution = part2(instructions)
    print(solution)


if __name__ == "__main__":
    main()
