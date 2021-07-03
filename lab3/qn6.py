'''6.	Write a Python program to count the number of even
and odd numbers from a series of numbers. '''
a = []
size = int(input("enter the size of the list: "))
for i in range(size):
    num = int(input("enter number: "))
    a.append(num)
counteven = 0
countodd = 0
for j in range(size):
    if (a[i]%2==0):
        counteven += 1
    else:
        countodd += 1
print(f"there are {counteven} even numbers and \n {countodd} odd numbers in the list. ")
