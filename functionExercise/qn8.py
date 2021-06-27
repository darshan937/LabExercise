'''Q.No.8 Write a Python function that takes a number as a parameter and
check the number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1
and that has no positive divisors other than 1 and itself.
'''
def prime(x):
    if x>1 and (x%2 == 0 or x%3 == 0):
        print(f"{x} is not a prime number.")
    elif x>1 and (x%2 != 0 or x%3 != 0):
        print(f"{x} is a prime number.")
x = int(input("enter a number: "))
prime(x)

