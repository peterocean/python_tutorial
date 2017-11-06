
#!/bin/python3
#-*- coding:utf-8 -*-

def ask_ok(prompt, retries = 4, reminder = 'Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n','no','nop','nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invaid user response')
        print(reminder)
ask_ok('Do you really want to quit?')
ask_ok('OK to overwrite the file?',2)
ask_ok('OK to overwrite the file?',2,'come on, only yes or no!')
