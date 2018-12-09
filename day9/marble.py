#!/usr/bin/env python3

from functools import reduce

game = None
with open("input", "r") as puzzle:
    game = puzzle.read().strip()

parts = game.split(" players; last marble is worth ", 1)
players = int(parts[0])
amount = int(parts[1].split(" points", 1)[0])

class Marble:
    def __init__(self, value):
        self.value = int(value)
        self.prev = None
        self.next = None

def solver(players, marbles):
    turn = 0
    high_score = 0
    scores = dict()
    first = Marble(marbles.pop())
    second = Marble(marbles.pop())
    first.next = second
    first.prev = second
    second.next = first
    second.prev = first
    current = second
    playing = True

    while playing:
        marble = Marble(marbles.pop())
        if marble.value % 23 == 0:
            for i in range(7):
                current = current.prev
            if scores.get(turn, None) is None:
                scores[turn] = 0
            scores[turn] = scores[turn] + marble.value + current.value
            high_score = max(high_score, scores[turn])
            before = current.prev
            after = current.next
            before.next = after
            after.prev = before
            current = after
        else:
            current = current.next
            after = current.next
            current.next = marble
            marble.prev = current
            marble.next = after
            after.prev = marble
            current = marble
        # print("[%s] %s" % (turn, " ".join(list(map(str, circle)))))
        turn = (turn + 1) % players
        if len(marbles) == 0:
            playing = False
        else:
            print(len(marbles))
    
    return high_score

# print("Part 1:", solver(players, [i for i in range(amount)][::-1]))
print("Part 2:", solver(players, [i for i in range(amount * 100)][::-1]))