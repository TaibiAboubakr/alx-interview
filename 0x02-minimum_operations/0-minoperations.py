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
    oldnbrH = 1
    while nbrH < n:
        if n % nbrH == 0:
            oldnbrH = nbrH
            nbrH *= 2
            countOp += 2
            while nbrH < n:
                if n % nbrH == 0:
                    oldnbrH = nbrH
                    nbrH *= 2
                    countOp += 2
                else:
                    nbrH += oldnbrH
                    countOp += 1
        else:
            nbrH += 1
            countOp += 1
    return countOp
