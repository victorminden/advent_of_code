from functools import cache
from pathlib import Path


def main() -> None:
    current_dir = Path("/")
    dirs = {current_dir: []}

    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        for line in file:
            if line.startswith("$"):
                if "cd" in line:
                    next_dir = line.split()[-1]
                    if next_dir == "..":
                        current_dir = current_dir.parent
                    else:
                        current_dir = current_dir / next_dir
                else:
                    assert "ls" in line
                continue

            size, name = line.split()
            new_name = current_dir / name
            dirs[current_dir].append(new_name)
            if size == "dir":
                dirs[new_name] = dirs.get(new_name, [])
            else:
                dirs[new_name] = int(size)

    # Part 1
    @cache
    def size(key):
        if isinstance(dirs[key], int):
            return dirs[key]
        else:
            return sum(size(k) for k in dirs[key])

    sizes = {k : size(k) for k in dirs}
    solution = sum(v for (k, v) in sizes.items() if isinstance(dirs[k], list) and v < 100000)
    print(solution)

    # Part 2
    total_space = 70000000
    needed_space = 30000000
    used_space = sizes[Path("/")]
    solution = min(v for (k, v) in sizes.items() if isinstance(dirs[k], list) and total_space - used_space + v > needed_space)
    print(solution)


if __name__ == "__main__":
    main()
