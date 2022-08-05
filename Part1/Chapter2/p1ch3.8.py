#!/usr/bin/python3

"""
Author:			John-Philipp Vogt
Date:			2022-08-04
Synopsis:		A script illustrating error handling.
Filename:		p1ch3.8.py
"""
"""
def spam(divideBy):
    return 42/divideBy
"""

def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('ERROR: Invalid argument')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

"""
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('ERROR: Invalid argument')

    
