from typing import List, Set
from pathlib import Path

Person = Set[str]
Group = List[Person]


def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        lines = [line.strip() for line in file.read().split('\n\n')]

    groups: List[Group] = [[set(person) for person in group.split('\n')] for group in lines]

    print("Part 1: ")
    print(sum(len(set.union(*group)) for group in groups))
    print("Part 2: ")
    print(sum(len(set.intersection(*group)) for group in groups))


if __name__ == "__main__":
    main()
