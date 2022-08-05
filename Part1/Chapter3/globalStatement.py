#!/usr/bin/python3

"""
Author:			John-Philipp Vogt
Date:			2022-08-04
Synopsis:		A script illustrating global statements.
Filename:		globalStatement.py
"""

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)

