#!/usr/bin/env python3

from functools import reduce

coordinates = None
with open("input", "r") as puzzle:
    parse = lambda p: list(map(int, p.strip().split(", ", 1)))
    coordinates = list(map(parse, puzzle.readlines()))
    

coords = dict()
distance = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])
sums = dict()
width, height = 0, 0
for c, coord in enumerate(coordinates):
    x, y = coord
    width = max(x, width)
    height = max(y, height)
    row = coords.get(y, None)
    if row is None:
        coords[y] = dict()
    coords[y][x] = c
    csum = 0
    for cc, ccoord in enumerate(coordinates):
        if c == cc:
            continue
        csum = csum + distance(coord, ccoord)
    sums[c] = csum

safe = 0
areas = dict()
infinites = set()
for y in range(height + 1):
    row = coords.get(y, dict())
    for x in range(width + 1):
        col = row.get(x, None)
        if col is not None:
            area = areas.get(col, 0)
            areas[col] = area + 1
            if sums[col] < 10000:
                safe = safe + 1
        else:
            here = [x, y]
            dists = list()
            repeats = list()
            winner = None
            min_dist = width * height
            hsum = 0
            for c, coord in enumerate(coordinates):
                dist = distance(here, coord)
                hsum = hsum + dist
                if dist in dists and dist not in repeats:
                    repeats.append(dist)
                dists.append(dist)
                if dist <= min_dist:
                    min_dist = dist
                    if dist in repeats:
                        winner = None
                    else:
                        winner = c
            if hsum < 10000:
                safe = safe + 1
            if winner is not None:
                if x == 0 or x == width or y == 0 or y == height:
                    infinites.add(winner)
                area = areas.get(winner, 0)
                areas[winner] = area + 1
            col = winner if winner is not None else "."
max_area = 0
for coord, area in areas.items():
    if coord in infinites:
        continue
    max_area = max(area, max_area)

print("Part 1: ", max_area)
print("Part 2: ", safe)