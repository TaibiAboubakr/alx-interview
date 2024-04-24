#!/usr/bin/python3
""" min operations """


def minOperations(n: int) -> int:
    """min operations  """
    if n <= 1:
        return 0
    if n == 2:
        return 2
    countOp = 2
    nbrH = 2
    oldnbrH = 2
    while nbrH < n:
        if n % nbrH == 0:
            oldnbrH = nbrH
            nbrH *= 2
            countOp += 2
        else:
            tmp = nbrH
            nbrH += oldnbrH
            oldnbrH = tmp
            countOp += 1
    return countOp
