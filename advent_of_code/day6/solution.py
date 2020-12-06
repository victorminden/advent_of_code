from pathlib import Path


def main() -> None:
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        groups = [line.strip() for line in file.read().split('\n\n')]

    # Part 1
    print(sum(len(set(group.strip().replace('\n', ''))) for group in groups))
    # Part 2
    print(sum([len(set.intersection(*[set(person) for person in group.split('\n')])) for group in groups]))


if __name__ == "__main__":
    main()
