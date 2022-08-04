#!/usr/bin/python3

"""
Author:			John-Philipp Vogt
Date:	        2022-08-04	
Synopsis:		A simple script introduction basics of python3.
Filename:		p1ch1.py
"""

print('Hello, World!')
print('What is your name?')
myName=input()
print('It is good to meet you, ' + myName + '!')
print(len(myName))
print('Your name is ' + str(len(myName)) + ' letters long!')
print('What is your age?')
myAge=input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

