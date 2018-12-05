#!/usr/bin/env python3

from functools import reduce

def solver(polymers, pairs):
    reacting = True
    while reacting:
        size = len(polymers)
        for pair in pairs:
            polymers = "".join(polymers.split(pair))
        if len(polymers) == size:
            reacting = False
    return len(polymers)

polymers = None
with open("input", "r") as puzzle:
    polymers = puzzle.read().strip()

alphabet = "abcdefghijklmnopqrstuvwxyz"
pair1 = list(map(lambda _: _ + _.upper(), alphabet))
pair2 = list(map(lambda _: _.upper() + _, alphabet))
pairs = pair1 + pair2

solved = solver(polymers, pairs)
shortest = len(polymers)
remove_letter = lambda _: _ != letter and _ != letter.upper()
for letter in alphabet:
    polys = "".join(list(filter(remove_letter, list(polymers))))
    shortest = min(shortest, solver(polys, pairs))

print("Part 1: ", solved)
print("Part 2: ", shortest)