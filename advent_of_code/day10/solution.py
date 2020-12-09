from typing import List, Dict, Tuple
from pathlib import Path
import collections


from advent_of_code.util import timing


def part1(adaptors: List[int]) -> int:
    c = collections.Counter(a - b for (a, b) in zip(adaptors[1:], adaptors))
    return c[1] * c[3]


def _num_valid(adaptors: List[int], *, idx: int, last: int, memo: Dict[Tuple[int, int], int]) -> int:
    key = (idx, last)
    if key in memo:
        # Short circuit.
        return memo[key]
    if adaptors[idx] > last + 3:
        memo[key] = 0
    elif idx == len(adaptors) - 1:
        memo[key] = 1
    else:
        memo[key] = _num_valid(adaptors, idx=idx + 1, last=adaptors[idx], memo=memo)
        memo[key] += _num_valid(adaptors, idx=idx + 1, last=last, memo=memo)

    return memo[key]


def part2(adaptors: List[int]) -> int:
    return _num_valid(adaptors, idx=1, last=0, memo={})


def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        adaptors = [int(line) for line in file]
    adaptors.extend([0, max(adaptors) + 3])
    adaptors.sort()

    with timing("Part 1"):
        solution = part1(adaptors)
    print(solution)

    with timing("Part 2"):
        solution = part2(adaptors)
    print(solution)


if __name__ == "__main__":
    main()
