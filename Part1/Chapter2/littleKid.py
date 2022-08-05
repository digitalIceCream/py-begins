#!/usr/bin/python3

"""
Author:			John-Philipp Vogt
Date:			2022-08-05
Synopsis:		A basic script to illustrate if, else if (elif), and else conditionals.
Filename:		littleKid.py
"""

name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice!')
elif age < 12:
    print('You are not Alice, kidddo!')
else:
    print('You are neither Alice nor a little kid...')

