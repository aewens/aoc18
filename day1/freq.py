#!/usr/bin/env python3

curr_frequency = 0
changes = list()
with open("input", "r") as puzzle:
    changes = [int(p.strip()) for p in puzzle.readlines()]

for change in changes:
    curr_frequency = curr_frequency + change

print(curr_frequency)