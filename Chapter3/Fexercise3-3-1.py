# -*- coding: utf-8 -*-
#Bisecting to find appproximate square root.

x = float(input('Please pick a number you want to find the square root of: '))
epsilon = 1*10**(-3)
NumGuesses = 0
low = 0.0
high = max(1.0, abs(x))
ans = (high + low)/2.0
while abs(ans**2 - abs(x)) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    NumGuesses += 1
    if ans**2 < abs(x):
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
if x < 0:
    ans = str(ans)+'i'
print('NumGuesses =', NumGuesses)
print(ans, 'is hella close- to the square root of', x)