#!/usr/bin/python3

"""
Module for isWinner.
"""


def isWinner(x, nums):
    """ Prime numbers game. """
    if x < 0 or nums[-1] < 1:
        return None
    Maria_score = 0
    Ben_score = 0
    prime = [False] * 100001
    primes = []
    for i in range(2, 100001):
        if not prime[i]:
            primes.append(i)
            for j in range(i, 100001, i):
                prime[j] = True

    l = 0
    for a0 in range(x):
        n = nums[l]
        # your code goes here
        num = 0
        for i in range(100001):
            if i >= len(primes) or primes[i] > n:
                break
            num += 1
        l += 1
        if (['Maria', 'Ben'][(num % 2) ^ 1]) == "Maria":
            Maria_score += 1
        else:
            Ben_score += 1
    if Maria_score > Ben_score:
        return "Maria"
    else:
        return "Ben"
