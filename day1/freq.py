#!/usr/bin/env python3

curr_frequency = 0
changes = list()
with open("input", "r") as puzzle:
    changes = [int(p.strip()) for p in puzzle.readlines()]

for change in changes:
    curr_frequency = curr_frequency + change

print("Part 1:", curr_frequency)

curr_frequency = 0
found = list()
repeated = None
iteration = 0

while repeated is None:
    for change in changes:
        iteration = iteration + 1
        curr_frequency = curr_frequency + change
        # print("%s\t%s\t%s" % (
        #     curr_frequency in found, curr_frequency, iteration))
        if curr_frequency in found:
            repeated = curr_frequency
            break
        else:
            found.append(curr_frequency)

print("Part 2:", repeated)


