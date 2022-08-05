#!/usr/bin/python3

"""
Author:			John-Philipp Vogt
Date:			2022-08-05
Synopsis:		A small script illustrating the use of the for-loop and a while loop.
Filename:		fiveTimes.py
"""

print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')
    
################################################

print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1



"""
NB: The range function makes the pythons for loop act like 'traditional for loops, like the one I know
from C and Java.
"""
