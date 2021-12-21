from functools import cache
from itertools import product
from typing import Tuple

from aoc.util import timing


class Player:
    """A player keeps track of their position and score in the game."""

    def __init__(self, position: int, score: int = 0) -> None:
        self._position: int = position
        self._score: int = score

    def move(self, n_spaces: int) -> "Player":
        """Moves the player around the circular track and records the score.

        This method does not mutate the current Player.
        """
        new_position = (self._position + n_spaces - 1) % 10 + 1
        new_score = self._score + new_position
        return Player(new_position, new_score)

    def score(self) -> int:
        """Returns the score."""
        return self._score

    def to_tuple(self) -> Tuple[int, int]:
        """Converts the Player to an int-tuple.

        This is much easier than trying to figure out how to use the cache
        decorator on the Player class.
        """
        return (self._position, self._score)


class DeterministicDie:
    """A die that deterministically rolls 1..100 over and over."""

    def __init__(self) -> None:
        self._prev_val = 100
        self._total_rolls = 0

    def roll(self, n: int = 1) -> int:
        """Rolls n copies of the die and sums the pips."""
        v = 0
        for _ in range(n):
            self._prev_val = self._prev_val % 100 + 1
            v += self._prev_val
        self._total_rolls += n
        return v

    def total_rolls(self) -> int:
        """Returns the total number of historical rolls."""
        return self._total_rolls


def part1(p1_pos: int, p2_pos: int) -> int:
    p1 = Player(p1_pos)
    p2 = Player(p2_pos)
    die = DeterministicDie()
    target_score = 1000

    while True:
        p1 = p1.move(die.roll(3))
        if p1.score() >= target_score:
            return p2.score() * die.total_rolls()

        p2 = p2.move(die.roll(3))
        if p2.score() >= target_score:
            return p1.score() * die.total_rolls()


@cache
def dirac_game(
    current_tuple: Tuple[int, int], other_tuple: Tuple[int, int]
) -> Tuple[int, int]:
    """Returns the number of wins of the respective players.

    Assumes that the score of the current player does not meet or exceed the
    target.
    """
    if Player(*other_tuple).score() >= 21:
        return (0, 1)

    a_wins, b_wins = (0, 0)
    for i, j, k in product((1, 2, 3), repeat=3):
        # Flip players to switch whose turn it is.
        new_b_wins, new_a_wins = dirac_game(
            other_tuple, Player(*current_tuple).move(i + j + k).to_tuple()
        )
        a_wins += new_a_wins
        b_wins += new_b_wins

    return a_wins, b_wins


def part2(p1_pos: int, p2_pos: int) -> int:
    return max(dirac_game((p1_pos, 0), (p2_pos, 0)))


def main() -> None:
    # Hard code the tiny input instead of parsing it.
    p1_pos, p2_pos = 2, 7

    with timing("Part 1"):
        solution = part1(p1_pos, p2_pos)
    print(solution)

    with timing("Part 2"):
        solution = part2(p1_pos, p2_pos)
    print(solution)


if __name__ == "__main__":
    main()
