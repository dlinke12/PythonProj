import random
import sys
import pyperclip

print(random.randint(1,10))

pyperclip.copy('Hello All')
print(pyperclip.paste())


def hello(name):
    print('Hello ' + name)

hello('Bob')
hello('Sam')

def plusOne(number):
        return number + 1

print('New number:' +str(plusOne(2)))


def tGlobal():
    global valueT
    valueT=42

tGlobal()
print(valueT)

print('Hello')
sys.exit()
print('Goodbye')



