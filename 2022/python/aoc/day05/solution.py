from copy import deepcopy
from itertools import islice
from pathlib import Path

from aoc.util import timing

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
        instructions = []
        stacks = [[] for _ in range(9)]
        for i, line in enumerate(file):
            if i in range(8):
                for i, boxed_item in enumerate(batched(line, len('[X] '))):
                    item = "".join(boxed_item).strip(" []\n")
                    if not item: continue
                    stacks[i].append(item)
            elif line.startswith("move"):
                _, num, _, src, _, dst = line.split(" ")
                instructions.append((int(num), int(src) - 1, int(dst) - 1))

    original_stacks = [s[::-1] for s in stacks]

    with timing("Part 1"):
        stacks = deepcopy(original_stacks)
        for num, src, dst in instructions:
            stacks[dst].extend(reversed(stacks[src][-num:]))
            stacks[src] = stacks[src][:-num]
        solution = "".join(s[-1] for s in stacks)
    print(solution)

    with timing("Part 2"):
        stacks = deepcopy(original_stacks)
        for num, src, dst in instructions:
            stacks[dst].extend(stacks[src][-num:])
            stacks[src] = stacks[src][:-num]
        solution = "".join(s[-1] for s in stacks)
    print(solution)


if __name__ == "__main__":
    main()
