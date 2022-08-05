#!/usr/bin/python3

"""
Author:			John-Philipp Vogt
Date:			2022-08-04
Synopsis:		A script tackling the issue of similar names of local and global variables.
Filename:		p1ch3.5.py
"""
def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs) # prints 'bacon local'

eggs = 'global'
bacon()
print(eggs) # prints 'global'

