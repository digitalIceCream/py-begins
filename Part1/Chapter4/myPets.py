#!/usr/bin/python3

"""
Author:			John-Philipp Vogt
Date:			2022-08-05
Synopsis:		A script using 'in' and 'not in' keywords.
Filename:		myPets.py
"""

myPets = ['Zophie','Pooka','Fat-Tail']
print('Enter a pet name:')
name = input()

if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet, yes.')

