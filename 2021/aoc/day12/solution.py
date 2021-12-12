from pathlib import Path
from typing import Callable, Dict, List, Tuple, TypeAlias

from aoc.util import timing

Cave: TypeAlias = str
AdjList: TypeAlias = Dict[Cave, List[Cave]]
CavePath: TypeAlias = Tuple[Cave, ...]


def count_paths(
    nodes: AdjList,
    path: CavePath,
    can_append: Callable[[CavePath, Cave], bool],
) -> int:
    if path[-1] == "end":
        return 1
    count = 0
    for node in nodes[path[-1]]:
        if not can_append(path, node):
            continue
        count += count_paths(nodes, path + (node,), can_append)
    return count


def part1(nodes: AdjList) -> int:
    def can_append(path: CavePath, node: Cave) -> bool:
        """Returns True if the node can be appended to the path, else False.

        An uppercase node can always be oppended, but other nodes can be visited
        at most once.
        """
        return node.isupper() or node not in path

    return count_paths(nodes, ("start",), can_append)


def part2(nodes: AdjList) -> int:
    def can_append(path: CavePath, node: Cave) -> bool:
        """Returns True if the node can be appended to the path, else False.

        An uppercase node can always be appended.   The starting node can never
        be appended.  Otherwise, a path can contain a unique lowercase node that
        is visited twice, and all other lowercase nodes can be visited at most
        once.
        """
        if node.isupper():
            return True
        if node == "start":
            return False
        times_visited = path.count(node)
        if times_visited == 0:
            return True
        if times_visited > 1:
            return False
        # Repeatedly converting things to a set is not great for timing, but is
        # an easy way to check that everything lowercase in the path is unique.
        lowers = list(filter(lambda x: x.islower(), path))
        return len(lowers) == len(set(lowers))

    return count_paths(nodes, ("start",), can_append)


def main() -> None:
    nodes = {}
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        for line in file:
            a, b = line.strip().split("-")
            nodes[a] = nodes.get(a, []) + [b]
            nodes[b] = nodes.get(b, []) + [a]

    with timing("Part 1"):
        solution = part1(nodes)
    print(solution)

    with timing("Part 2"):
        solution = part2(nodes)
    print(solution)


if __name__ == "__main__":
    main()
