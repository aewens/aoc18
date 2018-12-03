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
overlap_ids = dict()
all_ids = list()
cache = dict()
for claim in claims:
    claim_id, offx, offy, width, height = claim
    all_ids.append(claim_id)
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
            if len(fabric[row][col]) > 1:
                if cache.get(index, None) is None:
                    cache[index] = True
                    overlaps = overlaps + 1
                for fid in fabric[row][col]:
                    overlap_ids[fid] = True

print("Part 1: ", overlaps)
for cid in all_ids:
    if overlap_ids.get(cid, None) is None:
        print("Part 2: ", cid)