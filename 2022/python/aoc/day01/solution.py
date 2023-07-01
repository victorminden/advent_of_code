from pathlib import Path

from aoc.util import timing


def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        stacks = file.read().split("\n\n")[:-1]
        for i, stack in enumerate(stacks):
            stacks[i] = list(map(int, stack.split("\n")))

    with timing("Part 1"):
        solution = max(sum(s) for s in stacks)
    print(solution)

    with timing("Part 2"):
        solution = sum(sorted(sum(s) for s in stacks)[-3:])
    print(solution)


if __name__ == "__main__":
    main()
