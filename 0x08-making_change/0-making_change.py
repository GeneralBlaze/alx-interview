#!/usr/bin/python3

""" Given a pile of coins of different values, determine the
 fewest number of coins needed to meet a given amount total. """

def makeChange(coins, total):
    if total <= 0:
        return 0
    else:
        coins.sort(reverse=True)
        count = 0
        for coin in coins:
            count += total // coin
            total = total % coin
        if total != 0:
            return -1
        return count