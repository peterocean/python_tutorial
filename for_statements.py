#!/bin/python3
#-*- coding:utf-8 -*-

#program for keyword 'for' statement test
import math

words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w,len(w))

nations = ['china', "USA", 'England']


for var in nations:
    print(var,len(var))

for w in words[:]:
    if len(w) > 6:
        words.insert(0,w)

#interate over a sequence of numbers
for i in range(5):
    print(i)

for num in range(2,10):
    if num % 2 == 0:
        print("Found an even number",num)
        continue
    print("Found a number",num)
