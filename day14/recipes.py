#!/usr/bin/env python3

from functools import reduce

num_of_recipes = None
with open("input", "r") as puzzle:
    num_of_recipes = int(puzzle.read().strip())

display = lambda x: "".join(list(map(str, x)))
def iterate(elves, recipes, search=None):
    # print(elves, recipes)
    found = False
    selected = [recipes[elves[0]], recipes[elves[1]]]
    summed = list(str(reduce(lambda a, b: a + b, selected)))
    adding = list(map(int, summed))
    recipes.extend(adding)
    if search is not None:
        backtrack = len(adding) + len(search) * 2
        haystack = display(recipes[-backtrack:])
        found = search in haystack
    size = len(recipes)
    print(size)
    for s, select in enumerate(selected):
        current = elves[s]
        score = recipes[current]
        elves[s] = (current + score + 1) % size
    if search is None:
        return elves, recipes
    return elves, recipes, found
elves = [0, 1]
recipes = [3, 7, 1, 0]
while len(recipes) < num_of_recipes + 10:
    elves, recipes = iterate(elves, recipes)
part1 = display(recipes[num_of_recipes:num_of_recipes+10])
print("Part 1:", part1)

needle = str(num_of_recipes)
haystack = display(recipes)
if needle in haystack:
    part2 = len(haystack.split(needle, 1)[0])
    print("Part 2:", part2)
else:
    running = True
    while running:
        elves, recipes, found = iterate(elves, recipes, needle)
        running = not found
    haystack = display(recipes)
    part2 = len(haystack.split(needle, 1)[0])
    print("Part 2:", part2)