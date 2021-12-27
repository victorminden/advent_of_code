# Idea for running things backwards was cribbed from
# https://gist.github.com/jkseppan/1e36172ad4f924a8f86a920e4b1dc1b1

from typing import List, Set

from aoc.util import timing


# The fifth (sixth, sixteenth) input instruction varies across the 14 stages.
# Put the varying constant value for the corresponding instruction here.
fives = [1, 1, 1, 26, 1, 1, 1, 26, 1, 26, 26, 26, 26, 26]
sixes = [10, 12, 15, -9, 15, 10, 14, -5, 14, -7, -12, -10, -1, -11]
sixteens = [15, 8, 2, 6, 13, 4, 1, 9, 5, 13, 9, 6, 2, 2]


def run(w: int, z_in: int, stage_index: int) -> int:
    assert stage_index < 14
    assert z_in >= 0

    t = z_in // fives[stage_index]

    if w == (z_in % 26) + sixes[stage_index]:
        # In special cases, w satisfies the expected relation.
        z_out = t
        return z_out

    # In most cases, w does not have any special relationship with z_in.
    z_out = 26 * t + w + sixteens[stage_index]
    return z_out


def run_backwards(w: int, z_out: int, stage_index: int) -> List[int]:
    assert stage_index < 14
    assert z_out >= 0

    z_ins = []

    if z_out % 26 == w + sixteens[stage_index]:
        # If the remainder is right, there is an integral t that could have
        # generated z_out.
        t = (z_out - w - sixteens[stage_index]) // 26
        # This t could have been generateed by many different z_ins.
        for i in range(fives[stage_index]):
            z_in = t * fives[stage_index] + i

            if w == (z_in % 26) + sixes[stage_index]:
                # This isn't a possible z_in because it hits the special case in
                # the forward stage.
                continue

            assert run(w, z_in, stage_index) == z_out, z_in
            z_ins.append(z_in)

    if 0 <= (remainder := w - sixes[stage_index]) < 26:
        # For this w there is a single z_in that could have satisfied the
        # relation to hit the special case in the forward stage.
        z_in = remainder + z_out * fives[stage_index]
        assert run(w, z_in, stage_index) == z_out
        z_ins.append(z_in)

    return z_ins


def find_valid_zs() -> List[Set[int]]:
    """Returns a map from stage_index to input zs that seem valid.

    A z input seems valid for stage i if it generates a z output that seems
    valid for stage i + 1 for some input w.

    The only valid output for the final stage is 0.  Technically this is also
    the only valid input for the first stage, but we ignore that here.
    """
    valid_zs: List[Set[int]] = [set() for _ in range(14)]
    valid_zs.append({ 0 })
    for stage_index in reversed(range(14)):
        for z_out in valid_zs[stage_index + 1]:
            for w in (1,2,3,4,5,6,7,8,9):
                z_ins = run_backwards(w, z_out, stage_index)
                valid_zs[stage_index].update(z_ins)

    return valid_zs


def part1(find_biggest: bool = True) -> int:
    ws = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    if find_biggest:
        ws = (9, 8, 7, 6, 5, 4, 3, 2, 1)
    model_number = []
    valid_zs = find_valid_zs()
    z = 0
    for stage_index in range(14):
        for w in ws:
            if (z_out := run(w, z, stage_index)) in valid_zs[stage_index + 1]:
                z = z_out
                model_number.append(w)
                break
        else:
            raise RuntimeError("Oopsies.")
    return int("".join(str(c) for c in model_number))


def part2() -> int:
    return part1(find_biggest=False)


def main() -> None:
    with timing("Part 1"):
        solution = part1()
    print(solution)

    with timing("Part 2"):
        solution = part2()
    print(solution)


if __name__ == "__main__":
    main()
