#This is finger exercise 3.5.1 stating : Add some code to the impelementation of Newton-Raphson that keeps track of the number of iterations used to find the root.
#Use that code as part of program that compares the efficiency of NR and bisection search.

#NR for square root
#Find x such that x**2-24 within epsilon of 0
epsilon = 0.01
k = 24.0
guess = k/2.0
numGuesses = 0
while abs(guess*guess - k) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2) - k)/(2*guess))
print('Square root of', k, 'is about', guess)
print('It took', numGuesses, 'iterations to get', guess)
