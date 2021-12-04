import sys
import importlib


def run_main_for_day(day: int) -> None:
    try:
        solution = importlib.import_module(f"aoc.day{day:02}.solution")
        solution.main()
    except ImportError:
        raise NotImplementedError(f"No solution found for day {day}")


if __name__ == "__main__":
    try:
        day = int(sys.argv[1])
    except (IndexError, ValueError):
        print("Use `python run_day.py day` to run the solution for day `day` (integer)")
        exit(0)

    run_main_for_day(day)
