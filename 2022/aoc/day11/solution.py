from typing import Callable, List
import numpy as np

def make_monkeys():
    def make_test(mod, a, b):
        return lambda x: a if x % mod == 0 else b


    class Monkey:
        def __init__(self, items: List[int], op: Callable, mod: int, test: Callable):
            self.items = items
            self.op = op
            self.mod = mod
            self.test = test
            self.count = 0

        def inspect(self, x):
            self.count += 1
            return self.op(x)


    monkeys = []
    # Monkey 0:
    #   Starting items: 75, 75, 98, 97, 79, 97, 64
    #   Operation: new = old * 13
    #   Test: divisible by 19
    #     If true: throw to monkey 2
    #     If false: throw to monkey 7
    monkeys.append(
        Monkey([75, 75, 98, 97, 79, 97, 64], lambda old: old * 13, 19, make_test(19, 2, 7))
    )

    # Monkey 1:
    #   Starting items: 50, 99, 80, 84, 65, 95
    #   Operation: new = old + 2
    #   Test: divisible by 3
    #     If true: throw to monkey 4
    #     If false: throw to monkey 5
    monkeys.append(
        Monkey([50, 99, 80, 84, 65, 95], lambda old: old + 2, 3, make_test(3, 4, 5))
    )

    # Monkey 2:
    #   Starting items: 96, 74, 68, 96, 56, 71, 75, 53
    #   Operation: new = old + 1
    #   Test: divisible by 11
    #     If true: throw to monkey 7
    #     If false: throw to monkey 3
    monkeys.append(
        Monkey([96, 74, 68, 96, 56, 71, 75, 53], lambda old: old + 1, 11, make_test(11, 7, 3))
    )

    # Monkey 3:
    #   Starting items: 83, 96, 86, 58, 92
    #   Operation: new = old + 8
    #   Test: divisible by 17
    #     If true: throw to monkey 6
    #     If false: throw to monkey 1
    monkeys.append(
        Monkey([83, 96, 86, 58, 92], lambda old: old + 8, 17, make_test(17, 6, 1))
    )

    # Monkey 4:
    #   Starting items: 99
    #   Operation: new = old * old
    #   Test: divisible by 5
    #     If true: throw to monkey 0
    #     If false: throw to monkey 5
    monkeys.append(
        Monkey([99], lambda old: old * old, 5, make_test(5, 0, 5))
    )

    # Monkey 5:
    #   Starting items: 60, 54, 83
    #   Operation: new = old + 4
    #   Test: divisible by 2
    #     If true: throw to monkey 2
    #     If false: throw to monkey 0
    monkeys.append(
        Monkey([60, 54, 83], lambda old: old + 4, 2, make_test(2, 2, 0))
    )

    # Monkey 6:
    #   Starting items: 77, 67
    #   Operation: new = old * 17
    #   Test: divisible by 13
    #     If true: throw to monkey 4
    #     If false: throw to monkey 1
    monkeys.append(
        Monkey([77, 67], lambda old: old * 17, 13, make_test(13, 4, 1))
    )

    # Monkey 7:
    #   Starting items: 95, 65, 58, 76
    #   Operation: new = old + 5
    #   Test: divisible by 7
    #     If true: throw to monkey 3
    #     If false: throw to monkey 6
    monkeys.append(
        Monkey([95, 65, 58, 76], lambda old: old + 5, 7, make_test(7, 3, 6))
    )

    return monkeys


def main() -> None:
    # Part 1
    monkeys = make_monkeys()
    rounds = range(20)
    for _ in rounds:
        for monkey in monkeys:
            items = monkey.items.copy()
            monkey.items = []
            for item in items:
                worry = monkey.inspect(item) // 3
                target = monkey.test(worry)
                monkeys[target].items.append(worry)
    counts = sorted([monkey.count for monkey in monkeys])
    print(counts[-2] * counts[-1])


    # Part 2
    monkeys = make_monkeys()
    mod = np.prod([monkey.mod for monkey in monkeys])
    rounds = range(10000)
    for _ in rounds:
        for monkey in monkeys:
            items = monkey.items.copy()
            monkey.items = []
            for item in items:
                worry = monkey.inspect(item) % mod
                target = monkey.test(worry)
                monkeys[target].items.append(worry)
    counts = sorted([monkey.count for monkey in monkeys])
    print(counts[-2] * counts[-1])


if __name__ == "__main__":
    main()
