from pathlib import Path

from aoc.util import timing

score1 = {
    ("A", "X"): 4,
    ("A", "Y"): 8,
    ("A", "Z"): 3,
    ("B", "X"): 1,
    ("B", "Y"): 5,
    ("B", "Z"): 9,
    ("C", "X"): 7,
    ("C", "Y"): 2,
    ("C", "Z"): 6,
}

score2 = {
    ("A", "X"): 3,
    ("A", "Y"): 4,
    ("A", "Z"): 8,
    ("B", "X"): 1,
    ("B", "Y"): 5,
    ("B", "Z"): 9,
    ("C", "X"): 2,
    ("C", "Y"): 6,
    ("C", "Z"): 7,
}

def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        rounds = [tuple(line.split()) for line in file]

    with timing("Part 1"):
        solution = sum(score1[round] for round in rounds)
    print(solution)

    with timing("Part 2"):
        solution = sum(score2[round] for round in rounds)
    print(solution)


if __name__ == "__main__":
    main()
