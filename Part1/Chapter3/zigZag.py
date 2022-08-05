#!/usr/bin/python3

"""
Author:			John-Philipp Vogt
Date:			2022-08-04
Synopsis:		A little animation script.
Filename:		zigZag.py
"""

import time, sys

indent = 0 # How many space to indent.
indentIncreasing = True # Wheter the indentation is increasing or not.

try:
    while True: # The main program loop.
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second

        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction
                indentIncreasing = False

        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction again
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()

