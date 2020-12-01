# Day 1: Use naive solution (double / triple for loop) because the input is small.
import time

with open("input.txt") as f:
    numbers = [int(line) for line in f]

# Part 1
t1 = time.time()
for i, a in enumerate(numbers):
    for b in numbers[i:]:
        if a + b == 2020:
            print(a * b)
print("Total time: %s seconds" % (time.time() - t1))
      
# Part 2
t2 = time.time()
for i, a in enumerate(numbers):
    for j, b in enumerate(numbers[i:]):
        for c in numbers[i:][j:]:
            if a + b + c == 2020:
                print(a * b * c)
print("Total time: %s seconds" % (time.time() - t2))
