#!/usr/bin/python3

"""
Author:			John-Philipp Vogt
Date:			2022-08-05
Synopsis:		A short script illustrating the passign of arguments by reference (pointers?).
Filename:		passingReference.py
"""

def eggs(someParameter):
    someParameter.append('Henloo')

spam = [1,2,3]
eggs(spam)
print(spam)

