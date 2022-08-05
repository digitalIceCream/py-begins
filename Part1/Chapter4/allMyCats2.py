#!/usr/bin/python3

"""
Author:			John-Philipp Vogt
Date:			2022-08-05
Synopsis:	
Filename:		allMyCats2.py
"""

catNames = []

while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + 
     ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print('The cat names are:')
for name in catNames:
    print(' ' + name)
