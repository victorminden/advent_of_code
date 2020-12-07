from typing import DefaultDict, List, Tuple
from pathlib import Path
from collections import defaultdict
import re


def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        rules = [line.strip() for line in file]

    bags = defaultdict(list)
    bags_reverse = defaultdict(list)
    for line in rules:
        src_str, dsts_str = line.split("contain", maxsplit=1)
        src = re.match(r"([\w\s]*) bags", src_str)[1]
        dsts = re.findall(r"(\d+) ([\w\s]*) bag", dsts_str.strip())

        for (n_bags, bag) in dsts:
            # Build the reverse graph.
            bags_reverse[bag].append(src)
            # Build the forward graph.
            bags[src].append((int(n_bags), bag))

    # Part 1
    already_searched = set()
    can_hold = set()
    yet_to_process = ["shiny gold"]
    while yet_to_process:
        # Get the next bag to visit.
        bag = yet_to_process.pop()
        already_searched.add(bag)
        next_bags = bags_reverse[bag]
        if next_bags:
            can_hold.update(next_bags)
            yet_to_process.extend([b for b in next_bags if b not in already_searched])
    print(len(can_hold))

    # Part 2
    print(hold_how_many("shiny gold", bags) - 1)


def hold_how_many(bag: str, bags: DefaultDict[str, List[Tuple[int, str]]]) -> int:
    return 1 if not bags[bag] else 1 + sum(n * hold_how_many(b, bags) for (n, b) in bags[bag])


if __name__ == "__main__":
    main()
