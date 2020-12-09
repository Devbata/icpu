x = float(input('Please pick a positive number you want to find the square root of: '))

epsilon = 1*10**(-3)
BiNumGuesses = 0
low = 0.0
high = max(1.0, abs(x))
ans = (high + low)/2.0
while abs(ans**2 - abs(x)) >= epsilon:
    #print('low =', low, 'high =', high, 'ans =', ans)
    BiNumGuesses += 1
    if ans**2 < abs(x):
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
if x < 0:
    ans = str(ans)+'i'
print('BiNumGuesses =', BiNumGuesses)
print(ans, 'is hella close- to the square root of', x)

guess = x/2.0
NRnumGuesses = 0
while abs(guess*guess - x) >= epsilon:
    NRnumGuesses += 1
    guess = guess - (((guess**2) - x)/(2*guess))
print('Square root of', x, 'is about', guess)
print('It took', NRnumGuesses, 'iterations to get', guess)

if NRnumGuesses < BiNumGuesses:
  print('The Newton-Raphson method found the answer to be', guess, 'with', 
        NRnumGuesses, 'iterations, while the bisection method found the answer with',
        BiNumGuesses, 'iterations')
else:
    print('You have defeated science by picking x=4')
