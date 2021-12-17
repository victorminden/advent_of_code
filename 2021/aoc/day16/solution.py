from io import StringIO
from math import prod
from pathlib import Path
from typing import TypeAlias

from aoc.util import timing

Transmission: TypeAlias = str


def hex2bin(hex: str) -> str:
    # Adapted this from a few different StackOverflow discussions.
    return bin(int(hex, 16))[2:].zfill(4 * len(hex))


def bin2int(bin: str) -> int:
    return int(bin, 2)


def parse_packet(bitstream: StringIO, is_part2=False) -> int:
    # Took the idea of using a StringIO from a reddit comment.
    version = bin2int(bitstream.read(3))
    type_id = bin2int(bitstream.read(3))

    if type_id == 4:
        # Parse a literal value.
        literal_bits = ""
        while bin2int(bitstream.read(1)) == 1:
            literal_bits += bitstream.read(4)
        # There is one more set of 4 bits after the "0" bit.
        # If you happen to miss this then you will have a bad time.
        literal_bits += bitstream.read(4)
        return bin2int(literal_bits) if is_part2 else version
    else:
        # Parse an operator.
        operands = []
        length_type_id = bin2int(bitstream.read(1))
        if length_type_id == 1:
            # Parse a certain number of *operands*.
            length_in_packets = bin2int(bitstream.read(11))
            for _ in range(length_in_packets):
                operands.append(parse_packet(bitstream, is_part2))
        else:
            # Parse a certain number of *bits* making up all operands.
            length_in_bits = bin2int(bitstream.read(15))
            # StringIO is odd.  The current position is *definitely* actually
            # in units of "characters" but the documentation for the generic
            # TextIO describes it as being in units of "opaque numbers".
            # It appears that this has been a subject of discussion among the
            # developers, but for now let's just use knowledge of
            # https://github.com/python/cpython/blob/HEAD/Modules/_io/stringio.c#L477
            start_position = bitstream.tell()
            while bitstream.tell() < start_position + length_in_bits:
                operands.append(parse_packet(bitstream, is_part2))

    if not is_part2:
        # Operands represent the sum of the "version" field for the whole
        # expression subtree.
        return version + sum(operands)

    match type_id:
        case 0:
            return sum(operands)
        case 1:
            return prod(operands)
        case 2:
            return min(operands)
        case 3:
            return max(operands)
        case 5:
            return operands[0] > operands[1]
        case 6:
            return operands[0] < operands[1]
        case 7:
            return operands[0] == operands[1]
        case _:
            raise RuntimeError("Ruh-roh!")


def part1(transmission: Transmission) -> int:
    return parse_packet(StringIO(hex2bin(transmission)))


def part2(transmission: Transmission) -> int:
    return parse_packet(StringIO(hex2bin(transmission)), is_part2=True)


def main() -> None:
    transmission: Transmission = ""
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        transmission = file.readline().strip()

    with timing("Part 1"):
        solution = part1(transmission)
    print(solution)

    with timing("Part 2"):
        solution = part2(transmission)
    print(solution)


if __name__ == "__main__":
    main()
