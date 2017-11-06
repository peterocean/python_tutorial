#/usr/bin python3
#-*- coding:utf-8 -*-

fruits = ['orange', 'apple', 'pear', 'banana', 'apple', 'banana']

print(fruits.count('apple'))
print(fruits.count('banana'))

print(fruits.index('banana'))

print(fruits.index('banana',4))

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.pop(3)
print(fruits)

fruits.pop()
print(fruits)


