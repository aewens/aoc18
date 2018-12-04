#!/usr/bin/env python3

from functools import reduce

events = None
ordered = list()
with open("input", "r") as puzzle:
    events = list(map(lambda p: p.strip(), puzzle.readlines()))
    ordered = sorted(events)

guard = None
total = dict()
sleeps = dict()
previous = None
triggers = {
    "guard": "Guard #",
    "sleeps": "falls asleep",
    "wakes": "wakes up"
}
for event in ordered:
    timeframe, details = event.split("[", 1)[1].split("] ", 1)
    day, clock = timeframe.split(" ", 1)
    minutes = int(clock.split(":", 1)[1])
    
    if details[:7] == triggers["guard"]:
        guard = details.split(triggers["guard"], 1)[1].split(" ", 1)[0]
        if sleeps.get(guard, None) is None:
            sleeps[guard] = list()
            total[guard] = 0
    elif details == triggers["sleeps"]:
        previous = guard, minutes
    elif details == triggers["wakes"]:
        if previous is None:
            continue
        prev_guard, prev_minutes = previous
        elapse = minutes - prev_minutes
        total[guard] = total[guard] + elapse
        for e in range(elapse):
            sleeps[prev_guard].append(prev_minutes + e)

most_slept, most_slept_minutes = None, 0
for guard_id, minutes_slept in total.items():
    most_slept_minutes = max(most_slept_minutes, minutes_slept)
    if most_slept_minutes == minutes_slept:
        most_slept = guard_id

repeats = dict()
max_minute, max_minute_repeat = 0, 0
for minute in sleeps[most_slept]:
    if repeats.get(minute, None) is None:
        repeats[minute] = 0
    repeats[minute] = repeats[minute] + 1
    max_minute_repeat = max(max_minute_repeat, repeats[minute])
    if max_minute_repeat == repeats[minute]:
        max_minute = minute

min_repeats = dict()
sleeper, most_slept_minute, minute_freq = None, 0, 0
for guard_id, minutes_slept in sleeps.items():
    for minute in minutes_slept:
        if min_repeats.get(minute, None) is None:
            min_repeats[minute] = dict()
        if min_repeats[minute].get(guard_id, None) is None:
            min_repeats[minute][guard_id] = 0
        min_repeats[minute][guard_id] = min_repeats[minute][guard_id] + 1
        minute_freq = max(minute_freq, min_repeats[minute][guard_id])
        if minute_freq == min_repeats[minute][guard_id]:
            sleeper = guard_id
            most_slept_minute = minute

print("Part 1: ", int(most_slept) * max_minute)
print("Part 2: ", int(sleeper) * most_slept_minute)
