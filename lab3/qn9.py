'''9.	Write a program to find the factorial of a number. '''
num = int(input("enter a number: "))
a = 1
for i in range(1,num+1):
    a *= i
print(f"factorial of the {num} is {a}")
