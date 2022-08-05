#!/usr/bin/python3

"""
Author:			John-Philipp Vogt
Date:			2022-08-04
Synopsis:		A script illustrating call stack.
Filename:		abcdCallStack.py
"""

def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()
