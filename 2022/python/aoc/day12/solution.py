from pathlib import Path
from collections import deque


def visit(start, end, grid):
    if isinstance(start, tuple):
        to_visit = deque([(0, start)])
    else:
        to_visit = deque([(0, pos) for pos in start])

    seen = set()
    while to_visit:
        path_length, node = to_visit.popleft()
        if node == end:
            return path_length

        for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            new_node = node[0] + i, node[1] + j

            if new_node in seen: continue
            if new_node not in grid: continue
            if ord(grid[new_node]) - ord(grid[node]) > 1: continue

            to_visit.append((path_length + 1, new_node))
            seen.add(new_node)


def main() -> None:
    grid = {}
    start = None
    end = None
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        for i, line in enumerate(file):
            for j, c in enumerate(line.strip()):
                if c == 'S': start, c = (i, j), 'a'
                if c == 'E': end, c = (i, j), 'z'
                grid[(i, j)] = c

    # Part 1
    print(visit(start, end, grid))

    # Part 2
    print(visit({pos for pos in grid if grid[pos] == 'a'}, end, grid))


if __name__ == "__main__":
    main()
