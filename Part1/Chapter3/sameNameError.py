#!/usr/bin/python3

"""
Author:			John-Philipp Vogt
Date:			2022-08-05
Synopsis:		A script producing a deliberate error by wrong use of variable.
Filename:		sameNameError.py
"""

def spam():
    print(eggs) #ERROR
    eggs = 'spam local'

eggs = 'global'
spam()
