#!/usr/bin/python3

"""
Author:			John-Philipp Vogt
Date:			2022-08-05
Synopsis:		A script illustrating error handling.
Filename:		zeroDivide.py
"""

def spam(divideBy):
    return 42 / divideBy

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

