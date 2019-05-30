#!/usr/bin/python3

"""
2019.05.19 Daily Coding Problem: Problem #1 [Easy]

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def canSumTo(k, X):
	lookup = {}
	for x in X:
		if x in lookup: return True
		lookup[ k - x ] = x
	return False


assert (True == canSumTo(17, [10,15,3,7]))
assert (False == canSumTo(7, [10,15,3,7]))
assert (False == canSumTo(0, []))

