#!/usr/bin/python3
""" method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False """


def canUnlockAll(boxes):
    """  method that determines if all the boxes can be opened"""
    keys = [0]
    visited_keys = set()
    visited_keys.add(0)
    while keys:
        key = keys.pop()
        if key >= len(boxes):
            continue
        for box_num in boxes[key]:
            if box_num not in visited_keys:
                keys.append(box_num)
                if box_num < len(boxes):
                    visited_keys.add(box_num)
    return len(visited_keys) == len(boxes)
