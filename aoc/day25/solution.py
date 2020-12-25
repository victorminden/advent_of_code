
import itertools


from aoc.util import timing


def part1(pub1: int, pub2: int) -> int:
    return pow(pub2, _loop_size(pub1), 20201227)


def _loop_size(pub: int) -> int:
    n = 1
    for i in itertools.count():
        if n == pub:
            return i
        n = (7 * n) % 20201227


def main() -> None:
    pub1, pub2 = 19774466, 7290641

    with timing("Part 1"):
        solution = part1(pub1, pub2)
    print(solution)


if __name__ == "__main__":
    main()
