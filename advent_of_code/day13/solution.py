from typing import List, Tuple
from pathlib import Path

from advent_of_code.util import timing


def part1(x) -> int:
    return 0


def part2(x) -> int:
    return 0


def main() -> None:
    #with open(Path(__file__).parent.joinpath("input.txt")) as file:
    #    for line in file:
    #
    #    my_input = [line for line in file]

    n = 1015292
    m = "19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,743,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,643,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23"
    #m = "17,x,13,19"
    #m = "1789,37,47,1889"
    m = m.split(",")
    m = [(i,int(j)) for (i,j) in enumerate(m) if j != 'x']
    M = 1
    t = 0
    for (i, j) in m:
        M *= j
    for (i,j) in m:
        b = M // j
        for bp in range(M):
            if (bp * b) % j == 1:
                break
        #bp = (-b % j)
        t += (-i) * (b*bp) % M
    remainder = t % M
    for (i,j) in m:
        print((t % j, j - i))
        print((t + i) % j)
        print(i% j )
        #print(((t + M) % j, i))
    print(remainder)
    print(t)
    print(M)
    # earliest = 100000000
    # time = 1000000000000000000000
    # for i in m:
    #     if i == 'x':
    #         continue
    #     i = int(i)
    #     for j in range(n):
    #         if j * i >= n:
    #             time = min(time, j * i - n)
    #             if time == j * i - n:
    #                 earliest = i
    #
    # print((earliest, time, earliest * time))
    #t = remainder
    #tmax = 1202161486
    #print([(tmax % j, -i % j) for (i,j) in m ] )
    print(m)
    print([(t + i) % j == 0 for (i, j) in m])

    # while True:
    #     found_gud = True
    #     for i, j in m:
    #         if i > j:
    #             gud = (t + i) / j
    #             if not gud:
    #                 found_gud = False
    #     if found_gud:
    #         break
    #     if not t % 1000000:
    #         print(t)
    #         #print(tmp)
    #     t += M

    print(t)
    print(t+M)
    print(t+2*M)
    print(t + 3*M)


    # with timing("Part 1"):
    #     solution = part1(my_input)
    # print(solution)
    #
    # with timing("Part 2"):
    #     solution = part2(my_input)
    # print(solution)


if __name__ == "__main__":
    main()
