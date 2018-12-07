#!/usr/bin/env python3

from functools import reduce

instructions = None
with open("input", "r") as puzzle:
    instructions = list(map(lambda p: p.strip(), puzzle.readlines()))

deps = dict()
needs = dict()
children = list()
steps = set()
for entry in instructions:
    parts = entry.split("Step ", 1)[1].split(" must", 1)
    parent = parts[0]
    child = parts[1].split("step ", 1)[1].split(" can", 1)[0]
    dep = deps.get(parent, None)
    need = needs.get(child, None)
    if dep is None:
        deps[parent] = list()
    if need is None:
        needs[child] = list()
    deps[parent].append(child)
    needs[child].append(parent)
    children.append(child)
    steps.add(parent)
    steps.add(child)

steps = sorted(steps)
roots = set()
for step in steps:
    if step in children:
        continue
    roots.add(step)
start = sorted(roots)[:]
order = list()
search = True
while search:
    roots = sorted(roots)
    next_roots = set(roots[:])
    for root in roots:
        if root in order:
            continue
        if root in needs:
            skip = False
            for need in needs[root]:
                if need not in order:
                    skip = True
                    break
            if skip:
                continue
        order.append(root)
        next_roots.remove(root)
        if root in deps:
            for child in deps[root]:
                next_roots.add(child)
        break
    if len(next_roots) == 0:
        search = False
        break
    roots = next_roots

workers = 5#2
offset = 60#0
queue = dict()
done = list()
timer = lambda x, o: ord(x) - 64 + o
working = True
elapsed = 0
roots = start
for i in range(workers):
    queue[i] = None
while working:
    roots = sorted(roots)
    next_roots = set(roots[:])
    for root in roots:
        if root in done:
            continue
        if root in needs:
            skip = False
            for need in needs[root]:
                if need not in done:
                    skip = True
                    break
            if skip:
                continue
        for worker, job in queue.items():
            if job is None:
                queue[worker] = [root, timer(root, offset)]
                next_roots.remove(root)
                break
    queueing = 0
    for worker, job in queue.items():
        if job is None:
            continue
        step, count = job
        print(step, count)
        count = count - 1
        if count != 0:
            queue[worker] = [step, count]
            queueing = queueing + 1
        else:
            done.append(step)
            queue[worker] = None
            if step in deps:
                for child in deps[step]:
                    next_roots.add(child)
    elapsed = elapsed + 1
    if len(next_roots) == 0 and queueing == 0:
        working = False
        break
    roots = next_roots

print("Part 1:", "".join(order))
print("Part 2:", elapsed)