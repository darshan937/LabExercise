'''8.	Write a Python program to get the Fibonacci series between 0 to 50.
    Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it
'''
a = 0
b = 1
c = 0
while c <= 50:
    print(c,end=" ")
    a = b
    b = c
    c = a + b
print("these are the required fibonacci sequence. ")


