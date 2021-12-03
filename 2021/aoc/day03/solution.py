from pathlib import Path
from typing import List, TypeAlias

from aoc.util import timing


BinaryInt: TypeAlias = List[int]


def bits2int(bits: BinaryInt) -> int:
    """Returns a regular int representation of the BinaryInt.

    Converts the input list to a string `x` and then just uses `int(x, 2)`.
    """
    return int("".join(map(str, bits)), 2)


def round_right(x: float) -> int:
    """Returns the result of rounding input `x` to the nearest int.

    Unlike the built-in python `round` function, this function always rounds 0.5
    *up*.  In contrast, python rounds to the nearest even integer in this case,
    e.g.:
        >>> round(0.5)
        0
        >>> round(1.5)
        2
    """
    return int(x >= 0.5)


def part1(codes: List[BinaryInt]) -> int:
    candidates = codes.copy()
    n_candidates = len(candidates)
    n_bits = len(candidates[0])
    gamma_rate, epsilon_rate = [], []
    for i in range(n_bits):
        count = sum(code[i] for code in candidates)
        bit = round_right(count / n_candidates)
        gamma_rate.append(bit)
        epsilon_rate.append(1 - bit)

    return bits2int(gamma_rate) * bits2int(epsilon_rate)


def part2(codes: List[BinaryInt]) -> int:
    candidates = codes.copy()
    n_candidates = len(candidates)
    n_bits = len(candidates[0])
    for i in range(n_bits):
        count = sum(code[i] for code in candidates)
        bit = round_right(count / n_candidates)
        candidates = list(filter(lambda c: c[i] == bit, candidates))
        n_candidates = len(candidates)
        if n_candidates == 1:
            break
    ox_rate = candidates[0]

    candidates = codes.copy()
    n_candidates = len(candidates)
    for i in range(n_bits):
        count = sum(code[i] for code in candidates)
        bit = round_right(count / n_candidates)
        candidates = list(filter(lambda c: c[i] != bit, candidates))
        n_candidates = len(candidates)
        if n_candidates == 1:
            break
    co2_rate = candidates[0]

    return bits2int(ox_rate) * bits2int(co2_rate)


def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        codes: List[BinaryInt] = [
            [int(b) for b in line.strip()] for line in file]

    with timing("Part 1"):
        solution = part1(codes)
    print(solution)

    with timing("Part 2"):
        solution = part2(codes)
    print(solution)


if __name__ == "__main__":
    main()
