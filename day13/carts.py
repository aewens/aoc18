#!/usr/bin/env python3

from re import sub, finditer

lines = None
with open("input", "r") as puzzle:
    lines = list(map(lambda p: p.rstrip("\n"), puzzle.readlines()))

tracks = list()
for line in lines:
    tracks.append(sub(r"\^|v", "|", sub(r"<|>", "-", line)))

carts = list()
for l, line in enumerate(lines):
    for cart in finditer(r"[<>v\^]", line):
        carts.append([l, cart.start(), cart.group(0), 0])

mapto = {
    "\\/": {
        ">\\": "v",
        "<\\": "^",
        "^\\": "<",
        "v\\": ">",
        ">/": "^",
        "</": "v",
        "^/": ">",
        "v/": "<"
    },
    "+": {
        ">0": "^",
        ">1": ">",
        ">2": "v",
        "<0": "v",
        "<1": "<",
        "<2": "^",
        "^0": "<",
        "^1": "^",
        "^2": ">",
        "v0": ">",
        "v1": "v",
        "v2": "<"
    }
}

running = True
display = lambda x: ",".join(list(map(str, x)))
first = False
while running:
    crash = set()
    for c, cart in enumerate(carts):
        y, x, to, turn = cart
        if (x, y) in crash:
            continue
        nat = None
        if to == ">":
            nat = (x + 1, y)
        elif to == "<":
            nat = (x - 1, y)
        elif to == "^":
            nat = (x, y - 1)
        elif to == "v":
            nat = (x, y + 1)
        nx, ny = nat
        if any(cy == ny and cx == nx for cy, cx, cd, ct in carts):
            if not first:
                dnat = display(nat)
                first = True
                print("Part 1:", dnat)
            crash.add(nat)
        track = tracks[ny][nx]
        if track in "\\/":
            to = mapto["\\/"][to + track]
        elif track == "+":
            to = mapto["+"][to + str(turn)]
            turn = (turn + 1) % 3
        carts[c] = ny, nx, to, turn
    else:
        carts = [c for c in carts if (c[1], c[0]) not in crash]
        if len(carts) == 1:
            cart = carts[0]
            at = cart[1], cart[0]
            dat = display(at)
            print("Part 2:", dat)
            running = False
            break
        carts.sort()