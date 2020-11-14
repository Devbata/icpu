# -*- coding: utf-8 -*-
#Write a prgoram that asks the user to enter an integer and prints 2 integers,
#root and pwr, such that 1 < pwr < 6 and root^pwr is equal to the integer
#entered by the user.
#If no such pair of integers exists, it should print a message to that effect.
x = int(input('Please enter an integer of your liking: '))

root = 0
pwr = 2

while pwr < 6: 
    while root**pwr < abs(x):
        root = root + 1
    if root**pwr == abs(x):
        break
    else:
        root = 1
        pwr = pwr + 1
    
if root**pwr != abs(x):
    print("Your number " + str(x) + " has no root")
elif x < 0 and pwr%2 == 1:
    root = -root
    print('Dev is the smartest guy ever. Also your root is ' + str(root) + ' and your power is ' + str(pwr))
else:
    print('Dev is the smartest guy ever. Also your root is ' + str(root) + ' and your power is ' + str(pwr))