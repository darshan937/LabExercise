'''10. Write a Python program to sum of three given integers.
 However, if two values are equal sum will be zero.'''
a = int(input("enter first number: "))
b = int(input("enter second number : "))
c = int(input("enter the third number: "))
sum = a + b + c
if a == b :
    print("sum will be zero ")
elif b == c :
    print("sum will be zero ")
elif c == a :
    print("sum will be zero ")
else:
    print(f"sum of three number is {sum}")