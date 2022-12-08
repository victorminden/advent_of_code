from itertools import product
from pathlib import Path
import numpy as np


def main() -> None:
    size = 99
    trees = np.zeros(shape=(size, size), dtype=np.int64)

    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        for i, line in enumerate(file):
            for j, c in enumerate(line[:-1]):
                trees[i][j] = int(c)

    # Part 1
    solution = 0
    for i, j in product(range(size), range(size)):
        visible = [True, True, True, True]
        for k in range(1, size):
            if  i - k >= 0 and trees[i - k][j] >= trees[i][j]:
                visible[0] = False
            if  j - k >= 0 and trees[i][j - k] >= trees[i][j]:
                visible[1] = False
            if  i + k < size and trees[i + k][j] >= trees[i][j]:
                visible[2] = False
            if  j + k < size and trees[i][j + k] >= trees[i][j]:
                visible[3] = False
        solution += any(visible)

    print(solution)

    # Part 2
    for i, j in product(range(size), range(size)):
        visible = [0, 0, 0, 0]

        for k in range(1, size):
            if  i - k >= 0 and trees[i - k][j] >= trees[i][j]:
                visible[0] = k
                break
            visible[0] = i

        for k in range(1, size):
            if  j - k >= 0 and trees[i][j - k] >= trees[i][j]:
                visible[1] = k
                break
            visible[1] = j

        for k in range(1, size):
            if  i + k < size and trees[i + k][j] >= trees[i][j]:
                visible[2] = k
                break
            visible[2] = size - i - 1

        for k in range(1, size):
            if  j + k < size and trees[i][j + k] >= trees[i][j]:
                visible[3] = k
                break
            visible[3] = size - j - 1

        solution = max(solution, np.prod(visible))

    print(solution)


if __name__ == "__main__":
    main()
