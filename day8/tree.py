#!/usr/bin/env python3

from functools import reduce

nodes = None
with open("input", "r") as puzzle:
    nodes = puzzle.read().strip().split(" ")

sum = lambda l: reduce(lambda a, b: a + b, l)
def parser(nodes, metadata, tree, index):
    header = nodes[:2]
    children, entries = map(int, header)
    nodes = nodes[2:]
    if children == 0:
        data = list(map(int, nodes[:entries]))
        metadata.extend(data)
        tree.update({index: sum(data)})
        return nodes[entries:], metadata, tree, index
    for child in range(children):
        cindex = str(child + 1)
        result = parser(nodes, metadata, tree, index + cindex)
        nodes, metadata = result[0], result[1]
    data = list(map(int, nodes[:entries]))
    metadata.extend(data)
    value = 0
    for d in data:
        if d <= children:
            value = value + tree[index + str(d)]
    tree.update({index: value})
    return nodes[entries:], metadata, tree, index

tree = dict()
result = parser(nodes, list(), tree, "0")
nodes, metadata = result[0], result[1]

print("Part 1:", sum(metadata))
print("Part 2:", tree["0"])