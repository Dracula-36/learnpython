#!/usr/bin/python3
#Fiename:lambda.py
def make_repeater(n):
    return lambda s:s*n
twice=make_repeater(2)
print(twice('world'))
print(twice(5))
