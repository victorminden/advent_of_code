from typing import List, Tuple, DefaultDict
from pathlib import Path
from collections import defaultdict

from advent_of_code.util import timing


OpCode = str
Arg = int
Instruction = Tuple[OpCode, Arg]


def part1(instructions: List[Instruction], sp: int = 0) -> Tuple[int, bool]:
    acc = 0
    visited = set()
    while sp not in visited and sp < len(instructions):
        visited.add(sp)
        inst, arg = instructions[sp]
        inc = 1
        if inst == "nop":
            pass
        elif inst == "acc":
            acc += arg
        elif inst == "jmp":
            inc = arg
        sp += inc
    return acc, sp == len(instructions)


def _find_reachable(start: int, predecessors: DefaultDict[int, List[int]], reachable: List[int]) -> None:
    # Argument `reachable` is modified and used as an output parameter.
    reachable.append(start)
    for node in predecessors[start]:
        _find_reachable(node, predecessors, reachable)


def part2(instructions: List[Instruction]) -> int:
    predecessors = defaultdict(list)
    for sp, (inst, arg) in enumerate(instructions):
        inc = 1 if inst == "nop" or inst == "acc" else arg
        predecessors[sp + inc].append(sp)
    reachable = []
    _find_reachable(len(instructions), predecessors, reachable)
    good_nodes = set(reachable)

    acc, sp = 0, 0
    while sp < len(instructions):
        inst, arg = instructions[sp]
        inc = 1
        if inst == "nop":
            if sp + arg in good_nodes:
                return acc + part1(instructions, sp + arg)[0]
        elif inst == "acc":
            acc += arg
        elif inst == "jmp":
            inc = arg
            if sp + 1 in good_nodes:
                return acc + part1(instructions, sp + 1)[0]
        sp += inc

    raise RuntimeError("Could not swap any jmp/nop to find a non-looping program!")


def main() -> None:
    instructions: List[Instruction] = []
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        for line in file:
            op, arg = line.strip().split(maxsplit=1)[:2]
            instructions.append((op, int(arg)))

    with timing("Part 1"):
        solution = part1(instructions)[0]
    print(solution)

    with timing("Part 2"):
        solution = part2(instructions)
    print(solution)


if __name__ == "__main__":
    main()
