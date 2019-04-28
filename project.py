import string
import random

def chk():
    try:
        n=int(input('Please Enter the number: '))

    except(ValueError):
        print('\nError!!! Please input numbers...')
        chk()
        
    return n


try:
    n=int(input('Enter a number: '))
except:
    n=chk()



characters ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+}{|:>?<'


password = ""

for x in range(n):
    char = random.choice(characters)
    password = password + char

print (password)
input('\n')

