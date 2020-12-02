import sys
from advent_of_code.day1.solution import main as day1
from advent_of_code.day2.solution import main as day2


def run_main_for_day(day: int) -> None:
    if day == 1:
        day1()
    elif day == 2:
        day2()
    else:
        raise NotImplementedError(f"No solution found for day {day}")


if __name__ == "__main__":
    try:
        day = int(sys.argv[1])
    except (IndexError, ValueError):
        print("Use `python run_day.py n` to run the solution for day n (integer)")
        exit(0)

    run_main_for_day(day)
