#!/usr/bin/python3

"""
Author:			John-Philipp Vogt
Date:			2022-08-05
Synopsis:		A simple script illustrating the use of the break statement, and the while True: construct.
Filename:		yourName2.py
"""

while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

