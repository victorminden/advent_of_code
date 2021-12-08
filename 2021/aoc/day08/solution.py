from pathlib import Path
from typing import Dict, List, Set, TypeAlias

from aoc.util import timing


Digits: TypeAlias = List[str]
DigitLines: TypeAlias = List[Digits]


def easy_digits(digits: Digits) -> Digits:
    return list(filter(lambda d: len(d) in {2, 3, 4, 7}, digits))


def part1(output_lines: DigitLines) -> int:
    digits: Digits = [d for line in output_lines for d in line]
    return len(easy_digits(digits))


def easy_digits_map(digits: Digits) -> Dict[int, Set[str]]:
    len2digit = {
        2: 1,
        3: 7,
        4: 4,
        7: 8,
    }
    return {
        len2digit[len(d)]: set(d) for d in digits if d in easy_digits(digits)}


def decode_outputs(in_digits: Digits, out_digits: Digits) -> List[int]:
    decoded: Dict[str, str] = {}

    # Fill in the easy digits.
    known = easy_digits_map(in_digits)
    # By inspection, can determine 'a'.
    decoded['a'] = known[7] - known[1]
    # "3" is the unique digit that has 3 segments more than "1".
    for d in in_digits:
        putative_3 = set(d)
        if len(putative_3 - known[1]) == 3:
            known[3] = putative_3
            break
    # By inspection, can determine 'b', 'g', and 'd'.
    decoded['b'] = known[4] - known[7] - known[3]
    decoded['g'] = known[3] - known[4] - known[7]
    decoded['d'] = known[3] - known[1] - decoded['a'] - decoded['g']
    # If we remove all known segments from all digits, there will be one unique
    # digit with one remaining segment.  That segment is 'f'.
    for d in in_digits:
        putative_f = set(d)
        for v in decoded.values():
            putative_f -= v
        if len(putative_f) == 1:
            decoded['f'] = putative_f
            break
    # By inspection, can determine 'c'.
    decoded['c'] = known[1] - decoded['f']
    # If we remove all known segments from all digits, there will be one unique
    # digit with one remaining segment.  That segment is 'e'.
    for d in in_digits:
        putative_e = set(d)
        for v in decoded.values():
            putative_e -= v
        if len(putative_e) == 1:
            decoded['e'] = putative_e
            break

    assert len(decoded) == 7, "Logic snafu!"

    digit2segment: Dict[int, str] = {
        0: "abcefg",
        1: "cf",
        2: "acdeg",
        3: "acdfg",
        4: "bcdf",
        5: "abdfg",
        6: "abdefg",
        7: "acf",
        8: "abcdefg",
        9: "abcdfg",
    }

    # Find an analogue of digit2segment where the values are the corresponding
    # decodings of the values in digit2segment.
    digit2decoded: Dict[int, Set[str]] = {}
    for k, v in digit2segment.items():
        digit2decoded[k] = set()
        for seg in v:
            digit2decoded[k].add(list(decoded[seg])[0])

    # Find the corresponding decoded digit for each output.
    # To convert a list of ints to a multi-digit int, do gross string
    # processing.
    outputs = []
    for d in out_digits:
        for k, v in digit2decoded.items():
            if set(d) == v:
                outputs.append(str(k))
                break
    return int(''.join(outputs))


def part2(input_lines: DigitLines, output_lines: DigitLines) -> int:
    total = 0
    for (in_digits, out_digits) in zip(input_lines, output_lines):
        total += decode_outputs(in_digits, out_digits)
    return total


def main() -> None:
    input_lines: DigitLines = []
    output_lines: DigitLines = []
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        for line in file:
            in_str, out_str = line.split("|")
            input_lines.append(in_str.split())
            output_lines.append(out_str.split())

    with timing("Part 1"):
        solution = part1(output_lines)
    print(solution)

    with timing("Part 2"):
        solution = part2(input_lines, output_lines)
    print(solution)


if __name__ == "__main__":
    main()
