#!/usr/bin/env python3

from functools import reduce
from sys import maxsize

plots = None
with open("input", "r") as puzzle:
    plots = list(map(lambda p: p.strip(), puzzle.readlines()))

# position=< 21456,  53293> velocity=<-2, -5>
points = list()
for plot in plots:
    divide1 = plot.split("position=<", 1)
    divide2 = divide1[1].split(", ", 1)
    divide3 = divide2[1].split("> velocity=<", 1)
    divide4 = divide3[1].split(", ", 1)
    divide5 = divide4[1].split(">", 1)
    xpoint = int(divide2[0].strip())
    ypoint = int(divide3[0].strip())
    xvector = int(divide4[0].strip())
    yvector = int(divide5[0].strip())
    points.append([xpoint, ypoint, xvector, yvector])

running = True
coordinates = None
offset = None
width, height = 0, 0
last_diff = maxsize
count = 0
while running:
    xmin, ymin = maxsize, maxsize
    xmax, ymax = -maxsize - 1, -maxsize - 1
    coords = dict()
    for p, point in enumerate(points):
        px, py, vx, vy = point
        nx, ny = px + vx, py + vy
        points[p] = nx, ny, vx, vy
        if coords.get(ny, None) is None:
            coords[ny] = dict()
        coords[ny][nx] = True
        xmin = min(xmin, nx)
        xmax = max(xmax, nx)
        ymin = min(ymin, ny)
        ymax = max(ymax, ny)
    ydiff = ymax - ymin
    # print(ydiff)
    if ymax - ymin <= 10:
        # print(xmax - xmin, xmin, xmax)
        # print(ymax - ymin, ymin, ymax)
        coordinates = coords
        offset = [0 - xmin, 0 - ymin]
        width, height = xmax - xmin, ymax - ymin
        running = False
    count = count + 1

print("Part 1: ")
ox, oy = offset
for y in range(height + 1):
    row = coordinates.get(y - oy, None)
    if row is None:
        print("." * width)
        continue
    line = ""
    for x in range(width + 1):
        col = row.get(x - ox, None)
        char = "." if col is None else "#"
        line = line + char
    print(line)

print("Part 2: ", count)