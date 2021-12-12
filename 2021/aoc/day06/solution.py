from collections import Counter
from typing import TypeAlias

from aoc.util import timing


# Represent timers as a map with keys and values (k, v) such that there are `v`
# timers that have a current timer value of `k`.
# This allows using constant space instead of appending to the end of a list
# like the example does.
Timers: TypeAlias = Counter[int]


def simulate(timers: Counter[int]) -> Counter[int]:
    """Returns a new counter following the rules of lanternfish reproduction.

    When a timer hits 0, it spawns a new fish with a timer of 8.  The 0-timered
    fish also resets to 6.  All other timers just count down by 1.
    """
    new_timers = Counter({8: timers[0]})
    for (k, v) in timers.items():
        new_k = k - 1 if k > 0 else 6
        new_timers.update({new_k: v})
    return new_timers


def part1(timers: Counter[int], days: int = 80) -> int:
    timers = timers.copy()
    for _ in range(days):
        timers = simulate(timers)
    return timers.total()


def part2(timers: Counter[int]) -> int:
    return part1(timers, 256)


def main() -> None:
    # Input is small-ish today, so let's be lazy and include it in the source.
    timers = [1,1,1,2,1,1,2,1,1,1,5,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,4,1,1,1,1,3,
        1,1,3,1,1,1,4,1,5,1,3,1,1,1,1,1,5,1,1,1,1,1,5,5,2,5,1,1,2,1,1,1,1,3,4,1,
        1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,5,4,1,1,1,1,1,5,1,2,4,1,1,1,1,1,3,3,2,1,
        1,4,1,1,5,5,1,1,1,1,1,2,5,1,4,1,1,1,1,1,1,2,1,1,5,2,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,3,1,1,3,1,3,1,4,1,5,4,1,1,2,1,1,5,1,
        1,1,1,1,5,1,1,1,1,1,1,1,1,1,4,1,1,4,1,1,1,1,1,1,1,5,4,1,2,1,1,1,1,1,1,1,
        1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,4,1,1,1,2,1,4,1,1,1,1,1,1,1,1,1,4,2,1,2,1,
        1,4,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,3,2,1,4,1,5,1,1,1,4,5,1,1,1,1,1,1,5,1,
        1,5,1,2,1,1,2,4,1,1,2,1,5,5,3]
    timers = Counter(timers)

    with timing("Part 1"):
        solution = part1(timers)
    print(solution)

    with timing("Part 2"):
        solution = part2(timers)
    print(solution)


if __name__ == "__main__":
    main()
