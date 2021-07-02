'''4.	Write a Python program to construct the following pattern, using a nested for loop.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
for i in range(5):
    for j in range(i + 1):
        print("*", end=" ")
    print()
for K in range(5,0,-1):
    for L in range(K-1,0,-1):
        print("*",end=" ")
    print()