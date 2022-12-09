from pathlib import Path
from typing import List, Tuple
import numpy as np

DIRS = {
    "U": np.array((0, 1)),
    "D": np.array((0, -1)),
    "R": np.array((1, 0)),
    "L": np.array((-1, 0)),
    }


def move(movements: List[Tuple[str, int]], n_segments: int) -> int:
    pos = [np.array((0, 0)) for _ in range(n_segments)]
    seen = {tuple(pos[-1])}
    for dir, c in movements:
        for _ in range(c):
            pos[0] += DIRS[dir]
            for j in range(1, n_segments):
                if np.max(np.abs(pos[j] - pos[j-1])) <= 1:
                    break
                elif pos[j][0] == pos[j - 1][0]:
                    pos[j][1] += np.sign(pos[j - 1][1] - pos[j][1])
                elif pos[j][1] == pos[j - 1][1]:
                    pos[j][0] += np.sign(pos[j - 1][0] - pos[j][0])
                else:
                    pos[j] += np.sign(pos[j-1] - pos[j])

            seen.add(tuple(pos[-1]))

    return len(seen)


def main() -> None:
    movements = []
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        for line in file:
            dir, c = line.strip().split()
            movements.append((dir, int(c)))

    # Part 1
    print(move(movements, 2))

    # Part 2
    print(move(movements, 10))


if __name__ == "__main__":
    main()
