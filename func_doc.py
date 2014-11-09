#!/usr/bin/python3
#Filename:func_doc.py
def printMax(x,y):
   ''' Prints the maximum of two numbers.
   The two values must be integgers.'''
   x=int(x)
   y=int(y)
   if x>y:
    print(x,'is maximum')
   else:
    print(y,'is maximum')
printMax(3,5)
print(printMax.__doc__)
