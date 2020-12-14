from typing import List, Tuple, Union
from pathlib import Path
import collections
import re
import enum

from advent_of_code.util import timing


class InstructionType(enum.Enum):
    MASK = enum.auto()
    MEMORY = enum.auto()


Instruction = Union[Tuple[InstructionType, str], Tuple[InstructionType, str, str]]


def _make_binary_list_from_int_string(int_string: str, list_len: int) -> List[str]:
    binary_values = ['0' for _ in range(list_len)]
    for i, c in enumerate(reversed(bin(int(int_string))[2:])):
        binary_values[-i - 1] = c
    return binary_values


def part1(instructions: List[Instruction]) -> int:
    memory = collections.defaultdict(int)
    mask = None
    for inst_type, *inst in instructions:
        if inst_type == InstructionType.MASK:
            mask = inst[0]
            continue
        addr, val = inst
        binary_values = _make_binary_list_from_int_string(val, len(mask))

        for (i, c) in enumerate(mask):
            if c == 'X':
                continue
            binary_values[i] = c
        memory[addr] = int("".join(binary_values), 2)

    return sum(memory.values())


# def part2(buses: List[Bus]) -> int:
#     return 0


def main() -> None:
    instructions = []
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        for line in file:
            line = line.strip()
            mask_instruction = re.match(r"mask = ([X01]+)", line)
            if mask_instruction:
                instructions.append((InstructionType.MASK, mask_instruction[1]))
                continue
            mem_instruction = re.match(r"mem\[(\d+)\] = (\d+)", line)
            if mem_instruction:
                instructions.append((InstructionType.MEMORY, mem_instruction[1], mem_instruction[2]))
                continue
            raise RuntimeError

    with timing("Part 1"):
        solution = part1(instructions)
    print(solution)

   # with timing("Part 2"):
   #     solution = part2(buses)
   # print(solution)


if __name__ == "__main__":
    main()
