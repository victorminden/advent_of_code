from collections import Counter
from itertools import product
from pathlib import Path
from typing import List, TypeAlias

from aoc.util import timing

Key: TypeAlias = List[int]
Image: TypeAlias = List[List[int]]


def apply_filter(key: Key, image: Image, repeat: int = 1) -> Image:
    # The original image is assumed to be padded with 0.
    # After applying the filter once, the original image is therefore padded
    # with key[0].  After applying the filter twice, it is padded with
    # key[key[0]] and so on.  This can either alternate 0-1-0-1-... or stay all
    # 0.
    pad_val = 0
    for _ in range(repeat):
        m = len(image)
        n = len(image[0])
        new_image = []
        for i in range(-1, m + 1):
            new_image.append([])
            for j in range(-1, n + 1):
                val = ""
                for (di, dj) in product((-1, 0, 1), (-1, 0, 1)):
                    if 0 <= (inew := i + di) < m and 0 <= (jnew := j + dj) < n:
                        val += str(image[inew][jnew])
                    else:
                        val += str(pad_val)
                new_image[-1].append(key[int(val, 2)])
        image = new_image
        pad_val = key[pad_val]
    return image


def show(image: Image) -> None:
    for row in image:
        s = ""
        for v in row:
            s += "#" if v == 1 else "."
        print(s)


def part1(key: Key, image: Image, repeat: int = 2) -> int:
    new_image = apply_filter(key, image, repeat)
    c = Counter()
    c.update([v for row in new_image for v in row])
    return c[1]


def part2(key: Key, image: Image) -> int:
    return part1(key, image, repeat=50)


def main() -> None:
    key: Key = []
    image: Image = []
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        key = list(map(lambda x: int(x == "#"), file.readline().strip()))
        file.readline()
        for line in file:
            image.append(list(map(lambda x: int(x == "#"), line.strip())))

    with timing("Part 1"):
        solution = part1(key, image)
    print(solution)

    with timing("Part 2"):
        solution = part2(key, image)
    print(solution)


if __name__ == "__main__":
    main()
