from typing import List, Tuple, Optional
from pathlib import Path
from copy import deepcopy
import itertools
import numpy as np

from advent_of_code.util import timing

#dirs = {0: 'E', 30}

def part1(x) -> int:
    curr_pos = np.array([0, 0])
    N = np.array([0, 1])
    S = np.array([0, -1])
    E = np.array([-1, 0])
    W = np.array([1, 0])
    dir = 'E'
    for inst, c in x:
        if inst == 'N':
            curr_pos += c * N
        elif inst == 'S':
            curr_pos += c * S
        elif inst == 'E':
            curr_pos += c * E
        elif inst == 'W':
            curr_pos += c * W
        elif inst == 'F':
            if dir == 'N':
                curr_pos += c * N
            elif dir == 'S':
                curr_pos += c * S
            elif dir == 'E':
                curr_pos += c * E
            elif dir == 'W':
                curr_pos += c * W
        elif inst == 'L':
            while c != 0:
                if dir == 'N':
                    dir = 'W'
                elif dir == 'S':
                    dir = 'E'
                elif dir == 'E':
                    dir = 'N'
                elif dir == 'W':
                    dir = 'S'
                c -= 90
                #print(c)
        elif inst == 'R':
            while c != 0:
                if dir == 'N':
                    dir = 'E'
                elif dir == 'S':
                    dir = 'W'
                elif dir == 'E':
                    dir = 'S'
                elif dir == 'W':
                    dir = 'N'
                c -= 90

    return np.sum(np.abs(curr_pos))


def part2(x) -> int:
    curr_pos = np.array([-10, 1], dtype=np.int64)
    ship_pos = np.array([0, 0], dtype=np.int64)
    N = np.array([0, 1])
    S = np.array([0, -1])
    E = np.array([-1, 0])
    W = np.array([1, 0])
    for inst, c in x:
        if inst == 'N':
            curr_pos += c * N
        elif inst == 'S':
            curr_pos += c * S
        elif inst == 'E':
            curr_pos += c * E
        elif inst == 'W':
            curr_pos += c * W
        elif inst == 'F':
            disp = (curr_pos - ship_pos)
            ship_pos += c * disp
            curr_pos += c * disp
        elif inst == 'L':
            while c != 0:
                disp = (curr_pos - ship_pos)
                disp[0], disp[1] = disp[1], -disp[0]
                curr_pos = ship_pos + disp
                c -= 90
        elif inst == 'R':
            while c != 0:
                disp = (curr_pos - ship_pos)
                disp[0], disp[1] = -disp[1], disp[0]
                curr_pos = ship_pos + disp
                c -= 90
        #print(curr_pos, ship_pos)
    #print(ship_pos)
    return np.sum(np.abs(ship_pos))


def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        x = [(line[0], int(line[1:])) for line in file]

    with timing("Part 1"):
        solution = part1(x)
    print(solution)

    with timing("Part 2"):
        solution = part2(x)
    print(solution)


if __name__ == "__main__":
    main()
