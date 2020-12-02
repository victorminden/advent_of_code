import sys
from advent_of_code.day1.solution import main as day1


def run_main_for_day(day: int) -> None:
    if day == 1:
        day1()
    else:
        raise NotImplementedError(f"No solution found for day {day}")


if __name__ == "__main__":
    try:
        run_main_for_day(int(sys.argv[1]))
    except (IndexError, ValueError):
        print("Use `python run_day.py n` to run the solution for day n (integer)")
        exit(0)
