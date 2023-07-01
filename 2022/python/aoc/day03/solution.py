from itertools import islice
from pathlib import Path

from aoc.util import timing


def score(a: str) -> str:
    score = 0
    if a.isupper():
        score += 26
        a = a.lower()
    score += ord(a) - ord('a') + 1
    return score


def batched(iterable, n):
    "Batch data into lists of length n. The last batch may be shorter."
    #https://docs.python.org/3/library/itertools.html
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while (batch := list(islice(it, n))):
        yield batch


def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        sacks = [line.strip() for line in file]

    with timing("Part 1"):
        solution = sum(score(c) for s in sacks for c in set.intersection(set(s[:len(s)//2]), set(s[len(s)//2:])))
    print(solution)

    with timing("Part 2"):
        solution = sum(score(c) for group in batched(sacks, 3) for c in set.intersection(*map(set, group)))
    print(solution)


if __name__ == "__main__":
    main()
