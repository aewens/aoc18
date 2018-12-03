#!/usr/bin/env python3

from functools import reduce

def extract(line):
    group1 = line.strip().split("#", 1)[1].split(" @ ")
    claim_id = group1[0]
    group2 = group1[1].split(": ", 1)
    offx, offy = group2[0].split(",", 1)
    width, height = group2[1].split("x", 1)
    return claim_id, int(offx), int(offy), int(width), int(height)

claims = list()
fabric = dict()
with open("input", "r") as puzzle:
    claims = list(map(extract, puzzle.readlines()))

fwidth, fheight = 1000, 1000
overlaps = 0
cache = dict()
for claim in claims:
    claim_id, offx, offy, width, height = claim
    for y in range(height):
        row = offy + y
        frow = fabric.get(row, None)
        if frow is None:
            fabric[row] = dict()
        for x in range(width):
            col = offx + x
            fcol = fabric[row].get(col, None)
            if fcol is None:
                fabric[row][col] = list()
            index = row * fwidth + col
            fabric[row][col].append(claim_id)
            if len(fabric[row][col]) > 1 and cache.get(index, None) is None:
                cache[index] = True
                overlaps = overlaps + 1
                
print("Part 1: ", overlaps)


"""
0 1 2 3
4 5 6 7
8 9 A B
C D E F

_ = (x,y,a,b,w,h,W,H)
9 = (1,2,0,0,4,4,4,4) = y * W + x
A = (1,1,1,1,2,2,4,4) = (y + b) * W + (x + a)
"""