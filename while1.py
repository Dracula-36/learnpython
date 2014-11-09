#!/usr/bin/python3
#Filename:while1.py
number=23
while True:
    guess=int(input('Enter an integer:'))
    if guess==number:
        print('Congratulations,you guessed it.')
        break
    elif guess<number:
        print('No,it is a little higher than that.')
    else:
         print('No,it is a little lower than that.')
print('The while loop is over.')
print('Down')

