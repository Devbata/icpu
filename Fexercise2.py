#This code will have someone insert 10 numbers and then for the program to find the max odd number within the set if possible

#a, b, c, d, e, f, g, h, j, k = input('Please input 10 random numbers: ').split()

#a = int(a)
#b = int(b)
#c = int(c)
#d = int(d)
#e = int(e)
#f = int(f)
#g = int(g)
#h = int(h)
#j = int(j)
#k = int(k)

#Set1 = {a, b, c, d, e, f, g, h, j, k}

Input1 = input('Enter 10 numbers: ').split()

Input1 = [int(x) for x in Input1] #List comprehension google it 

Set1 = set()
Set1.update(Input1)

print('You have chose the following numbers: ', Set1)

#Set1.remove(max(Set1))

#print(Set1)

while len(Set1) > 0 and max(Set1)%2==0:
    Set1.remove(max(Set1))

if len(Set1) == 0:
    print('The set containts only even numbers')
else:
    print('The largest odd number within the set is: ', max(Set1))