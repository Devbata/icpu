# -*- coding: utf-8 -*-
#Problem Statement: Let s be a string that contains a sequence of 
#decimal numbers separated by commas, e.g.,s = '1.23,2.4,3.123'. 
#Write a program that prints the sum of the numbers in s. 

s = '2.020, 1.1, 3.002'
slist = s.split(',')
total = 0
for i in slist:
    total += float(i)
print(total)

#print(sum([float(x) for x in "1.2, 1.12, 1.002".split(',')]))
#David's 1 liner code
