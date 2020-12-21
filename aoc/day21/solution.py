from typing import Dict, Set, Tuple
from pathlib import Path
from functools import reduce
import collections

from aoc.util import timing


Node = str
Edge = Tuple[Node, Node]


def allergen_free_ingredients(edges: Set[Edge], ingredients: Set[Node], allergens: Set[Node]) -> Set[Node]:
    return {a for a in ingredients if all((a, b) in edges for b in allergens)}


def part1(edges: Set[Edge], ingredients: Set[Node], allergens: Set[Node], raw_file: str) -> int:
    ingredient_counter = collections.Counter([
        ingredient
        for clean_line in [line.split('(')[0].strip().split() for line in raw_file.split('\n')]
        for ingredient in clean_line
    ])
    return sum(ingredient_counter[a] for a in allergen_free_ingredients(edges, ingredients, allergens))


def part2(edges: Set[Edge], ingredients: Set[Node], allergens: Set[Node]) -> str:
    translation = {}
    found_ingredients = allergen_free_ingredients(edges, ingredients, allergens)
    found_allergens = set()
    edges = [(a, b) for (a, b) in edges if a not in found_ingredients]
    while len(found_allergens) < len(allergens):
        for a in ingredients - found_ingredients:
            possible_allergens = [b for b in allergens if (a, b) not in edges and b not in found_allergens]
            if len(possible_allergens) == 1:
                b = possible_allergens[0]
                translation[a] = b
                found_ingredients.add(a)
                found_allergens.add(b)
                edges = [(a, b) for (a, b) in edges if a not in found_ingredients and b not in found_allergens]

    return ",".join((kv[0] for kv in sorted(translation.items(), key=lambda kv: kv[1])))


def main() -> None:
    all_ingredients = set()
    all_allergens = set()
    all_edges = set()

    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        for line in file:
            # First pass, just find the ingredients and allergens.
            ingredients, allergens = line.split('(')
            ingredients = ingredients.strip().split()
            allergens = allergens.strip().replace(',', '')[:-1].split()[1:]
            all_ingredients.update(ingredients)
            all_allergens.update(allergens)
        file.seek(0)
        for line in file:
            ingredients, allergens = line.split('(')
            ingredients = ingredients.strip().split()
            allergens = allergens.strip().replace(',', '')[:-1].split()[1:]
            # Invert the graph so a->b means "a is definitely not in b', i.e., A subset Bc
            for a in all_ingredients:
                if a in ingredients:
                    continue
                for b in allergens:
                    all_edges.add((a, b))
        file.seek(0)
        raw_file = file.read()

    with timing("Part 1"):
        solution = part1(all_edges, all_ingredients, all_allergens, raw_file)
    print(solution)

    with timing("Part 2"):
        solution = part2(all_edges, all_ingredients, all_allergens)
    print(solution)


if __name__ == "__main__":
    main()
