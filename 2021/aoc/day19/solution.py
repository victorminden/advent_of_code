from itertools import product
from pathlib import Path
from typing import Iterator, List, Set, Tuple, TypeAlias

from aoc.util import timing

ALL_AXES = {0, 1, 2}
ALL_SIGNS = {1, -1}
MIN_MATCHES = 12

Point = Tuple[int, int, int]
Scanner: TypeAlias = Set[Point]
SignedAxis: TypeAlias = Tuple[int, int]
Rotation: TypeAlias = Tuple[SignedAxis, SignedAxis, SignedAxis]

# Keep track of the coordinates for each found scanner.
# Be lazy and use a global for this purpose, because it is a small hack needed
# for part 2 only and we don't want to run the whole brute force again.
_scanner_coordinates: List[Point] = []


def rotations() -> Iterator[Rotation]:
    """Yields all valid 3D rotations of XYZ.

    Map X to 0, Y to 1, Z to 2, and then use the right-hand rule.
    """
    for axis0, sign0 in product(ALL_AXES, ALL_SIGNS):
        for axis1, sign1 in product(ALL_AXES - {axis0}, ALL_SIGNS):
            axis2 = (ALL_AXES - {axis0, axis1}).pop()
            # First ignore the signs and just compute i X j == k etc., then
            # use linearity to incorporate the extra signs.
            sign2 = 1 if (axis0, axis1) in {(0, 1), (1, 2), (2, 0)} else -1
            sign2 = sign2 * sign0 * sign1
            yield (axis0, sign0), (axis1, sign1), (axis2, sign2)


def rotate_scanner(scanner: Scanner, rotation: Rotation) -> Scanner:
    (i, isign), (j, jsign), (k, ksign) = rotation
    rotated = set()
    for beacon in scanner:
        rotated_beacon = isign * beacon[i], jsign * beacon[j], ksign * beacon[k]
        rotated.add(rotated_beacon)
    return rotated


def shift_scanner(scanner: Scanner, shift: Tuple[int, int, int]) -> Scanner:
    shifted = set()
    for x, y, z in scanner:
        shifted.add((x + shift[0], y + shift[1], z + shift[2]))
    return shifted


def match_one_more(
    matched_beacons: List[Point], unmatched: List[Scanner]
) -> None:
    for unmatched_scanner in unmatched:
        # Try to rotate and shift unmatched scanner to overlap.
        for rotation in rotations():
            rotated = rotate_scanner(unmatched_scanner, rotation)
            for b1, b2 in product(rotated, matched_beacons):
                shift = b2[0] - b1[0], b2[1] - b1[1], b2[2] - b1[2]
                shifted = shift_scanner(rotated, shift)
                common_beacons = matched_beacons.intersection(shifted)
                if len(common_beacons) >= MIN_MATCHES:
                    matched_beacons.update(shifted)
                    unmatched.remove(unmatched_scanner)
                    # For part 2 only, need the scanner coordinates.
                    _scanner_coordinates.append(shift)
                    return


def part1(scanners: List[Scanner]) -> int:
    matched_beacons: Set[Point] = scanners[0]
    unmatched_scanners: List[Scanner] = scanners[1:]
    while unmatched_scanners:
        match_one_more(matched_beacons, unmatched_scanners)
    return len(matched_beacons)


def part2(scanners: List[Scanner]) -> int:
    del scanners
    max_distance = 0
    for a, b in product(_scanner_coordinates, _scanner_coordinates):
        distance = abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])
        max_distance = max(distance, max_distance)
    return max_distance


def main() -> None:
    scanners: List[Scanner] = []
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        for line in file:
            if not line.strip():
                continue
            if "scanner" in line:
                scanners.append(set())
            else:
                beacon = tuple(map(int, line.strip().split(",")))
                scanners[-1].add(beacon)

    with timing("Part 1"):
        solution = part1(scanners)
    print(solution)

    with timing("Part 2"):
        solution = part2(scanners)
    print(solution)


if __name__ == "__main__":
    main()
