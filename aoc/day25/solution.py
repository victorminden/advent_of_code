
import itertools


from aoc.util import timing


def part1(pub1: int, pub2: int) -> int:
    return _transform(pub2, _loop_size(pub1))


def _transform(pub: int, loop_size: int) -> int:
    n = 1
    for _ in range(loop_size):
        n = (pub * n) % 20201227
    return n


def _loop_size(pub: int) -> int:
    n = 1
    for loop_size in itertools.count(1):
        n = (7 * n) % 20201227
        if n == pub:
            return loop_size


def main() -> None:
    pub1, pub2 = 19774466, 7290641

    with timing("Part 1"):
        solution = part1(pub1, pub2)
    print(solution)


if __name__ == "__main__":
    main()
