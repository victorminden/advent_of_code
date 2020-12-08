from typing import List, Tuple
from pathlib import Path

from advent_of_code.util import timing


OpCode = str
Arg = int
Instruction = Tuple[OpCode, Arg]


def part1(instructions: List[Instruction]) -> Tuple[int, bool]:
    acc = 0
    sp = 0
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


def part2(instructions: List[Instruction]) -> int:
    for i, (op, arg) in enumerate(instructions):
        if op == "acc":
            continue
        if op == "nop":
            instructions[i] = ("jmp", arg)
        else:
            instructions[i] = ("nop", arg)
        acc, done = part1(instructions)
        if done:
            return acc
        instructions[i] = (op, arg)
    raise RuntimeError("Problem could not be solved!")


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
