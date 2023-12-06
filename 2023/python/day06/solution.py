ts = [44707080]
ds = [283113411341491]

s = 1
for (t,d) in zip(ts,ds):
    c = 0
    for i in range(0, t + 1):
        if (t - i) * i > d:
            c += 1
    s *= c
print(s)

