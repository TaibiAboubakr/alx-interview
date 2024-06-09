#!/usr/bin/python3
"""
Making change
"""


def makeChange(coins, total):
    """ makechange function """
    if total <= 0:
        return 0
    coins_sorted = sorted(coins, reverse=True)
    count = 0
    i = 0
    lenght = len(coins)
    while (total > 0 and i < lenght):
        while (total >= coins_sorted[i]):
            count += 1
            total -= coins_sorted[i]
        i += 1
    if total == 0:
        return count
    return -1
