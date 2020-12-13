from typing import List, Tuple
from pathlib import Path
import functools

from advent_of_code.util import timing

BusIndex = int
BusId = int
Bus = Tuple[BusIndex, BusId]


def _additive_inverse_mod_p(x: int, p: int) -> int:
    return p - (x % p)


def _multiplicative_inverse_mod_p(x: int, p: int) -> int:
    # Assumes p is prime, uses Fermat.
    return x ** (p-2)


def part1(start_time: int, buses: List[Bus]) -> int:
    # Pair the bus id with the waiting time for that bus.
    ids_and_times = ((bus_id, _additive_inverse_mod_p(x=start_time, p=bus_id)) for (_, bus_id) in buses)
    # Find the bus that will come first, and the time you will have to wait for it.
    best_id_and_time = min(ids_and_times, key=lambda id_and_time: id_and_time[1])
    return best_id_and_time[0] * best_id_and_time[1]


def _chinese_remainder_theorem(remainders: List[int], primes: List[int]) -> int:
    big_p = functools.reduce(lambda a, b: a * b, primes, 1)  # Not a prime, but notationally often called "P".
    x = sum(r * (big_p // p) * _multiplicative_inverse_mod_p(big_p // p, p) for r, p in zip(remainders, primes))
    return x % big_p


def part2(buses: List[Bus]) -> int:
    return _chinese_remainder_theorem(
        remainders=[-index for (index, _) in buses],
        primes=[b_id for (_, b_id) in buses],
    )


def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        lines = file.readlines()
    earliest_time = int(lines[0])
    buses: List[Bus] = [(index, int(bus_id)) for (index, bus_id) in enumerate(lines[1].split(",")) if bus_id != 'x']

    with timing("Part 1"):
        solution = part1(earliest_time, buses)
    print(solution)

    with timing("Part 2"):
        solution = part2(buses)
    print(solution)


if __name__ == "__main__":
    main()
