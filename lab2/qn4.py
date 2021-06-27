'''4. Given three integers, print the smallest one. (Three integers should be user input)'''
x = int(input("enter the first integer: "))
y = int(input("enter the second integer: "))
z = int(input("enter the third integer: "))
if x < y and x < z :
    print(x)
elif y < x and y < z :
    print(y)
elif z < x and z < y :
    print(z)