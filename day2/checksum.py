#!/usr/bin/env python3

from functools import reduce
from sys import exit

repeats = list()
box_ids = list()
similar = None
with open("input", "r") as puzzle:
    box_ids = [p.strip() for p in puzzle.readlines()]

for bi, box_id in enumerate(box_ids):
    letters = list(box_id)
    tracker = dict()
    has = [0, 0]
    for l, letter in enumerate(letters):
        value = tracker.get(letter, 0)
        tracker[letter] = value + 1
    if similar is not None:
        continue
    for bbi, bbox_id in enumerate(box_ids):
        if bi == bbi:
            continue
        other_letters = list(bbox_id)
        matches = list()
        match_letters = list()
        for i in range(len(letters)):
            matches.append(1 if letters[i] == other_letters[i] else 0)
            if matches[-1] == 1:
                match_letters.append(letters[i])
        length = len(matches)
        score = length - reduce(lambda a, b: a + b, matches)
        if score == 1:
            similar = "".join(match_letters)
    for char, occur in tracker.items():
        if occur == 2:
            has[0] = 1
        elif occur == 3:
            has[1] = 1
    repeats.append(has)

reduced = reduce(lambda a, b: (a[0] + b[0], a[1] + b[1]), repeats)
checksum = reduced[0] * reduced[1]
print("Part 1: ", checksum)
print("Part 2: ", similar)

