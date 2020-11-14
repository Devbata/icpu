#This program will attemp to do the finger exercise problem on pg. 18 in 'Intro to computation and programming using python'.

#The problem is: Write a program that examines three variables - x, y, and z - and prints the largest odd number among them. If non of them are odd it should print a message to that effect.

x = int(input('Please choose a value for x: '))
y = int(input('Please choose a value for y: '))
z = int(input('Please choose a value for z: '))

if x%2 == 1 or y%2 == 1 or z%2 == 1: #Checks each value mod 1, to find the odd number... if at lease 1 input is odd, then the following will run
    if x%2 == 1 and x > y and x > z: #Checks if x is odd, then if it is also larger than y and z.
        print(x, 'is the largest odd number.') #Prints the value of x, then the following
    elif y%2==1 and y>z: #Checks if y is odd and if y is greater than z.
        print(y, 'is the largest odd number.') #Prints the value of y, then the following.
    elif z%2==1: #Checks if z is odd.
        print(z, 'is the largest odd number.') #Prints the value of z, then the following.
else: #if x,y, and z are all equal to 0 mod 2, then they are all even. 
    print('All values are even.') 
