import sys
from aoc.day01.solution import main as day01
from aoc.day02.solution import main as day02
from aoc.day03.solution import main as day03
from aoc.day04.solution import main as day04
from aoc.day05.solution import main as day05
from aoc.day06.solution import main as day06
from aoc.day07.solution import main as day07
from aoc.day08.solution import main as day08
from aoc.day09.solution import main as day09
from aoc.day10.solution import main as day10
from aoc.day11.solution import main as day11
from aoc.day12.solution import main as day12
from aoc.day13.solution import main as day13
from aoc.day14.solution import main as day14
from aoc.day15.solution import main as day15
from aoc.day16.solution import main as day16
from aoc.day17.solution import main as day17
from aoc.day18.solution import main as day18
from aoc.day19.solution import main as day19


def run_main_for_day(day: int) -> None:
    if day == 1:
        day01()
    elif day == 2:
        day02()
    elif day == 3:
        day03()
    elif day == 4:
        day04()
    elif day == 5:
        day05()
    elif day == 6:
        day06()
    elif day == 7:
        day07()
    elif day == 8:
        day08()
    elif day == 9:
        day09()
    elif day == 10:
        day10()
    elif day == 11:
        day11()
    elif day == 12:
        day12()
    elif day == 13:
        day13()
    elif day == 14:
        day14()
    elif day == 15:
        day15()
    elif day == 16:
        day16()
    elif day == 17:
        day17()
    elif day == 18:
        day18()
    elif day == 19:
        day19()
    else:
        raise NotImplementedError(f"No solution found for day {day}")


if __name__ == "__main__":
    try:
        day = int(sys.argv[1])
    except (IndexError, ValueError):
        print("Use `python run_day.py day` to run the solution for day `day` (integer)")
        exit(0)

    run_main_for_day(day)
