import sys
from advent_of_code.day1.solution import main as day1
from advent_of_code.day2.solution import main as day2
from advent_of_code.day3.solution import main as day3
from advent_of_code.day4.solution import main as day4
from advent_of_code.day5.solution import main as day5
from advent_of_code.day6.solution import main as day6
from advent_of_code.day7.solution import main as day7
from advent_of_code.day8.solution import main as day8
from advent_of_code.day9.solution import main as day9
from advent_of_code.day10.solution import main as day10
from advent_of_code.day11.solution import main as day11
from advent_of_code.day12.solution import main as day12
from advent_of_code.day13.solution import main as day13


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
    else:
        raise NotImplementedError(f"No solution found for day {day}")


if __name__ == "__main__":
    try:
        day = int(sys.argv[1])
    except (IndexError, ValueError):
        print("Use `python run_day.py start_time` to run the solution for day start_time (integer)")
        exit(0)

    run_main_for_day(day)
