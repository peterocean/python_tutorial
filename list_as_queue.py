#!/usr/bin python3
#-*- coding:utf-8 -*-

from collections import deque

fruits = ['orange', 'apple', 'pear', 'banana', 'apple', 'banan']
queue = deque(["Eric", "John", "Michael"])
print(queue);

queue.append("Terry")
print(queue)

queue.append("Graham")
print(queue)

queue.popleft()
print(queue)
