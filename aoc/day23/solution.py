from typing import List
from aoc.util import timing


def part1(cups: List[int], num_moves: int = 100) -> List[int]:
    cups = cups.copy()
    max_cup = len(cups) + 1
    for move in range(num_moves):
        current, cups = cups[0], cups[1:]
        pick_up, cups = cups[0:3], cups[3:]
        dest_val = current - 1
        while True:
            try:
                dest = cups.index(dest_val)
                break
            except ValueError:
                dest_val = (dest_val - 1) % max_cup
        for i, p in enumerate(pick_up):
            cups.insert(dest + i + 1, p)
        cups.append(current)
    return cups


def part2(cups: List[int], num_moves: int = 10000000) -> int:
    max_cup = len(cups) + 1
    current = cups[0]

    # Turn cups into a "linked list".
    cups = {c: cups[(i + 1) % len(cups)] for i, c in enumerate(cups)}

    for move in range(num_moves):
        pick_up = [cups[current], cups[cups[current]], cups[cups[cups[current]]]]
        # Fix the linked list.
        cups[current] = cups[pick_up[-1]]

        # Find the destination for stitching.
        dest = current - 1
        while dest == 0 or dest in pick_up:
            dest = (dest - 1) % max_cup

        # Stitch "pick_up" into the linked list.
        cups[pick_up[-1]] = cups[dest]
        cups[dest] = pick_up[0]
        current = cups[current]

    return cups[1] * cups[cups[1]]


def main() -> None:
    # test_cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
    cups = [2, 4, 7, 8, 1, 9, 3, 5, 6]
    with timing("Part 1"):
        solution = part1(cups, 100)
    # Must manually read out numbers from 1 "clockwise", excluding 1.
    print(solution)

    cups.extend(range(10, 1000000 + 1))
    with timing("Part 2"):
        solution = part2(cups, 10000000)
    print(solution)


if __name__ == "__main__":
    main()
