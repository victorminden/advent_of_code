from typing import List
import collections

from advent_of_code.util import timing


def part1(numbers: List[int], last_turn: int = 2020) -> int:
    turns = collections.defaultdict(lambda: collections.deque(maxlen=2))
    for i, n in enumerate(numbers):
        turns[n].append(i)

    n = numbers[-1]
    for turn in range(len(numbers), last_turn):
        try:
            n = turns[n][-1] - turns[n][-2]
        except IndexError:
            # This is fine.
            n = 0
        turns[n].append(turn)
    return n


def part2(numbers: List[int]) -> int:
    # This takes ~ 30 seconds.  Maybe we will optimize it later.
    return part1(numbers, last_turn=30000000)


def main() -> None:
    numbers = [14, 3, 1, 0, 9, 5]

    with timing("Part 1"):
        solution = part1(numbers)
    print(solution)

    with timing("Part 2"):
        solution = part2(numbers)
    print(solution)


if __name__ == "__main__":
    main()
