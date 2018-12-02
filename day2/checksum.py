#!/usr/bin/env python3

from functools import reduce

repeats = list()
box_ids = list()
with open("input", "r") as puzzle:
    box_ids = [p.strip() for p in puzzle.readlines()]

for box_id in box_ids:
    letters = list(box_id)
    tracker = dict()
    has = [0, 0]
    for letter in letters:
        value = tracker.get(letter, 0)
        tracker[letter] = value + 1
    for char, occur in tracker.items():
        if occur == 2:
            has[0] = 1
        elif occur == 3:
            has[1] = 1
    repeats.append(has)

reduced = reduce(lambda a, b: (a[0] + b[0], a[1] + b[1]), repeats)
checksum = reduced[0] * reduced[1]
print(reduced)
print("Part 1: ", checksum)
