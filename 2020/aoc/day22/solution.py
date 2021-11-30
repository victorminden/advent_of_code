from typing import Tuple
from pathlib import Path
import collections
from itertools import islice
from aoc.util import timing

Deck = collections.deque


def part1(deck1: Deck, deck2: Deck) -> int:
    while deck1 and deck2:
        c1, c2 = deck1.popleft(), deck2.popleft()
        if c1 > c2:
            deck1.extend([c1, c2])
        else:
            deck2.extend([c2, c1])
    winning_deck = deck1 if deck1 else deck2

    return sum((i + 1) * c for i, c in enumerate(reversed(winning_deck)))


def recursive_combat(deck1: Deck, deck2: Deck) -> Tuple[int, Deck]:
    previous_rounds = set()
    winner = None
    while deck1 and deck2:
        winner = None
        decks = tuple(deck1), tuple(deck2)
        if decks in previous_rounds:
            winner = 1
            break
        previous_rounds.add(decks)
        c1, c2 = deck1.popleft(), deck2.popleft()
        if len(deck1) >= c1 and len(deck2) >= c2:
            # Recursive combat.
            winner = recursive_combat(Deck(islice(deck1, 0, c1)), Deck(islice(deck2, 0, c2)))[0]
            if winner == 1:
                deck1.extend([c1, c2])
            else:
                deck2.extend([c2, c1])
        else:
            if c1 > c2:
                deck1.extend([c1, c2])
            else:
                deck2.extend([c2, c1])
    if winner == 1:
        winning_deck = deck1
    else:
        winner = 1 if deck1 else 2
        winning_deck = deck1 if deck1 else deck2
    return winner, winning_deck


def part2(deck1: Deck, deck2: Deck) -> int:
    return sum((i + 1) * c for i, c in enumerate(reversed(recursive_combat(deck1, deck2)[1])))


def main() -> None:
    deck1 = collections.deque()
    deck2 = collections.deque()
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        file.readline()
        for line in file:
            if line == '\n':
                break
            deck1.append(int(line))
        file.readline()
        for line in file:
            if line == '\n':
                break
            deck2.append(int(line))

    with timing("Part 1"):
        solution = part1(Deck(deck1), Deck(deck2))
    print(solution)

    with timing("Part 2"):
        solution = part2(deck1, deck2)
    print(solution)


if __name__ == "__main__":
    main()
