#!/usr/bin/env python3

from functools import reduce

lines = None
with open("input", "r") as puzzle:
    lines = list(map(lambda p: p.strip(), puzzle.readlines()))

rules = dict()
pots = list()
for line in lines:
    if len(line) == 0:
        continue
    elif line[0] == "i":
        pots = list(line.split("initial state: ", 1)[1])
    else:
        rule, action = line.split(" => ", 1)
        if action == list(rule)[2]:
            continue
        rules[rule] = action

def get_score(pots, offset):
    score = 0
    for p, pot in enumerate(pots):
        if pot == "#":
            score = score + p + offset
    return score

def solver(generations, rules, pots):
    rule_size = 5
    states = list()
    pots = list("....") + pots + list("....")
    states.append(pots[:])
    display = lambda d: "".join(d)
    offset = -4
    pots_size = len(pots)
    keys = list(rules.keys())
    scores = list()
    scores.append(get_score(pots, offset))
    prev_diff = None
    for generation in range(generations):
        state = states[-1]
        for p in range(pots_size):
            search = list()
            o = -2
            for r in range(rule_size):
                index = p + r + o
                if index >= pots_size or index <= 0:
                    search.append(".")
                else:
                    search.append(state[index])
            rule = display(search)
            action = rules.get(rule, None)
            if action is not None:
                pots[p] = action
        if "#" in pots[:5] or "#" in pots[-5:]:
            pots = list("....") + pots + list("....")
            offset = offset - 4
            pots_size = pots_size + 8
        states.append(pots[:])
        scores.append(get_score(pots, offset))
        diff = scores[-1] - scores[-2]
        if diff == prev_diff:
            return scores[-1] + diff * (generations - generation - 1)
        prev_diff = diff
    pots = list(states[-1])
    return get_score(pots, offset)

score1 = solver(20, rules, pots[:])
print("Part 1:", score1)
score2 = solver(50000000000, rules, pots[:])
print("Part 2:", score2)