from typing import List
from pathlib import Path
import collections

from advent_of_code.util import timing
from advent_of_code.day1.solution import part1 as day1part1


def part1(ciphertext: List[int]) -> int:
    for i, c in enumerate(ciphertext[25:]):
        try:
            day1part1(set(ciphertext[i : i + 25]), target_sum=c)
        except RuntimeError:
            return c


def part2(ciphertext: List[int], target_sum: int) -> int:
    # O(start_time) solution based on discussion with @aaditya.prakash.
    running_sum = 0
    queue = collections.deque()
    numbers = iter(ciphertext)
    while running_sum != target_sum:
        if running_sum < target_sum:
            num = next(numbers)
            queue.append(num)
            running_sum += num
        else:
            running_sum -= queue.popleft()
    return min(queue) + max(queue)


def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        ciphertext = [int(line) for line in file]

    with timing("Part 1"):
        solution1 = part1(ciphertext)
    print(solution1)

    with timing("Part 2"):
        solution = part2(ciphertext, target_sum=solution1)
    print(solution)


if __name__ == "__main__":
    main()
