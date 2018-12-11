#!/usr/bin/env python3

from functools import reduce
from datetime import datetime

serial = None
with open("input", "r") as puzzle:
    serial = int(puzzle.read().strip())

def get_power_level(cx, cy, serial):
    rack_id = cx + 10
    power_level = rack_id * cy
    power_level = power_level + serial
    power_level = power_level * rack_id
    hundreds = int(list(str(power_level))[-3])
    return hundreds - 5

cells = dict()
for y in range(300):
    cy = y + 1
    row = cells[cy] = dict()
    for x in range(300):
        cx = x + 1
        row[cx] = get_power_level(cx, cy, serial)

def solve_square(cells, square):
    max_power = 0
    max_power_point = ["0", "0"]
    for i in range(300 * 300):
        cx = (i % 300) + 1
        cy = (i // 300) + 1
        if 300 - cx < square - 1 or 300 - cy < square - 1:
            continue
        power = 0
        for y in range(square):
            sy = cy + y
            row = cells[sy]
            for x in range(square):
                sx = cx + x
                col = row[sx]
                power = power + col
        if power > max_power:
            max_power = power
            max_power_point = str(cx), str(cy)
    return max_power, max_power_point

power3, point3 = solve_square(cells, 3)

max_square = 0
max_square_point = ["0", "0", "0"]
for s in range(300):
    start = datetime.now().timestamp()
    sq = s + 1
    power, point = solve_square(cells, sq)
    end = datetime.now().timestamp()
    if power > max_square:
        max_square = power
        max_square_point = list(point) + [str(sq)]
    else:
        break

print("Part 1: ", ",".join(point3))
print("Part 2: ", ",".join(max_square_point))
