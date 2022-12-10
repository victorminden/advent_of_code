from pathlib import Path
import numpy as np



def main() -> None:
    insts = []
    with open(Path(__file__).parent.joinpath("input.txt")) as file:
        for line in file:
            insts.append(line.strip())

    # Part 1
    val = 0
    def maybe_update_val(x, t):
        nonlocal val
        if t in {20, 60, 100, 140, 180, 220}:
            val += x * t

    x = 1
    t = 1
    for inst in insts:
        maybe_update_val(x, t)
        t += 1
        if inst == "noop": continue
        maybe_update_val(x, t)
        t += 1
        v = int(inst.split()[-1])
        x += v

    print(val)


    # Part 2
    pix = []
    def update_pix(x, t):
        nonlocal pix
        if t % 40 in {x, x + 1, x + 2}:
            pix.append("#")
        else:
            pix.append(".")

    x = 1
    t = 1
    for inst in insts:
        update_pix(x, t)
        t += 1
        if inst == "noop": continue
        update_pix(x, t)
        t += 1
        v = int(inst.split()[-1])
        x += v

    arr = np.array(pix).reshape((6, 40))
    for i in range(arr.shape[0]):
        print("".join(arr[i][j] for j in range(arr.shape[1])))


if __name__ == "__main__":
    main()
