#!/bin/python3
#-*-coding = utf-8 -*-

x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('signle')
else:
    print('More')
