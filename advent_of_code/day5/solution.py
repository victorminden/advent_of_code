from typing import Optional, List, Tuple, Iterable
from pathlib import Path

from advent_of_code.util import timing


BoardingPass = Tuple[str, str]


def _find_seat_1d(search_str: str, low: str, high: str, seat_list: Optional[List[int]] = None) -> int:
    # In retrospect, this is just parsing a binary number and so could be simplified dramatically.
    if seat_list is None:
        seat_list = list(range(2 ** len(search_str)))

    if not search_str:
        return seat_list[0]

    middle = (len(seat_list) + 1) // 2
    if search_str[0] == low:
        s = slice(0, middle)
    elif search_str[0] == high:
        s = slice(middle, None)
    else:
        raise ValueError(f"Unknown input character: {search_str[0]}")

    return _find_seat_1d(search_str[1:], low, high, seat_list[s])


def _find_seat_2d(row: str, col: str) -> int:
    return 8 * _find_seat_1d(row, low='F', high='B') + _find_seat_1d(col, low='L', high='R')


def part1(passes: Iterable[BoardingPass]) -> int:
    return max(map(lambda p: _find_seat_2d(p[0], p[1]), passes))


def part2(passes: Iterable[BoardingPass]) -> int:
    all_seats = set(map(lambda p: _find_seat_2d(p[0], p[1]), passes))
    return next(i+1 for i in all_seats if i+1 not in all_seats)


def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        passes = [(line[:7], line[7:10]) for line in file]

    with timing("Part 1"):
        solution = part1(passes)
    print(solution)

    with timing("Part 2"):
        solution = part2(passes)
    print(solution)


if __name__ == "__main__":
    main()
