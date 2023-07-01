from pathlib import Path

from aoc.util import timing


def find_start(buffer: str, k: int) -> int:
    """
    Return the index of the first character preceded by k unique characters.
    (uses one-based indexing)
    """
    # Look at an element and its k-1 following elements, and find the first time
    # they are all unique.
    shifted_buffers = (buffer[i:] for i in range(k))
    iteration_space = enumerate(zip(*shifted_buffers))
    # We wanted to look at preceding elements in reality, so shift result by k.
    return k + next(i for (i, x) in iteration_space if len(set(x)) == k)


def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        buffer = file.read()

    with timing("Part 1"):
        solution = find_start(buffer, k=4)
    print(solution)

    with timing("Part 2"):
        solution = find_start(buffer, k=14)
    print(solution)


if __name__ == "__main__":
    main()
