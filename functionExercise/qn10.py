'''Q.No.10 Write a program to find the factorial of a number using functions. '''
def factorial(x):
    fac = 1
    while x>0:
        fac = fac * x
        x = x - 1
    print(f"factorial of the given number is {fac} ")
x = int(input("enter a number: "))
factorial(x)


