from typing import List, Tuple, Union
from pathlib import Path
import collections
import copy
import re
import enum
import itertools

from advent_of_code.util import timing


class InstructionType(enum.Enum):
    MASK = enum.auto()
    MEMORY = enum.auto()


Instruction = Union[Tuple[InstructionType, str], Tuple[InstructionType, str, str]]


def _make_binary_chars_from_int_string(int_string: str, list_len: int) -> List[str]:
    binary_chars = ['0' for _ in range(list_len)]
    for i, c in enumerate(reversed(bin(int(int_string))[2:])):
        binary_chars[-i - 1] = c
    return binary_chars


def part1(instructions: List[Instruction]) -> int:
    memory = collections.defaultdict(int)
    mask = None
    for inst_type, *inst in instructions:
        if inst_type == InstructionType.MASK:
            mask = inst[0]
            continue

        address_string, value_string = inst
        binary_chars = _make_binary_chars_from_int_string(value_string, len(mask))
        for (i, c) in enumerate(mask):
            if c == 'X':
                continue
            binary_chars[i] = c
        memory[address_string] = int("".join(binary_chars), 2)

    return sum(memory.values())


def part2(instructions: List[Instruction]) -> int:
    memory = collections.defaultdict(int)
    mask = None
    for inst_type, *inst in instructions:
        if inst_type == InstructionType.MASK:
            mask = inst[0]
            continue

        address_string, value_string = inst
        binary_chars = _make_binary_chars_from_int_string(address_string, len(mask))
        for (i, c) in enumerate(mask):
            if c != '0':
                binary_chars[i] = c

        x_idxs = [i for i, c in enumerate(binary_chars) if c == 'X']
        for x_vals in itertools.product(["0", "1"], repeat=len(x_idxs)):
            for idx, val in zip(x_idxs, x_vals):
                binary_chars[idx] = val
            address = int("".join(binary_chars), 2)
            memory[address] = int(value_string)

    return sum(memory.values())


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

    with timing("Part 2"):
        solution = part2(instructions)
    print(solution)


if __name__ == "__main__":
    main()
