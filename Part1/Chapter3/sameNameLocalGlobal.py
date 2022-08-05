#!/usr/bin/python3

"""
Author:			John-Philipp Vogt
Date:			2022-08-05
Synopsis:		A script illustrating more use of global variables.
Filename:		sameNameLocalGlobal.py
"""

def spam():
    global eggs
    eggs = 'bacon' # this is global

def bacon():
    eggs = 'bacon' # this is local

def ham():
    print(eggs) # this is global

eggs = 42 # global again
spam()
print(eggs)
