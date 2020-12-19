import sys
from aoc.day1.solution import main as day1
from aoc.day2.solution import main as day2
from aoc.day3.solution import main as day3
from aoc.day4.solution import main as day4
from aoc.day5.solution import main as day5
from aoc.day6.solution import main as day6
from aoc.day7.solution import main as day7
from aoc.day8.solution import main as day8
from aoc.day9.solution import main as day9
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
        day1()
    elif day == 2:
        day2()
    elif day == 3:
        day3()
    elif day == 4:
        day4()
    elif day == 5:
        day5()
    elif day == 6:
        day6()
    elif day == 7:
        day7()
    elif day == 8:
        day8()
    elif day == 9:
        day9()
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
