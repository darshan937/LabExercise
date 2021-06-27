'''8. Given a three-digit number. Find the sum of its digits.'''
num = str(input("enter a three digit number: "))
a = 0
for i in (num):
    a = int(i) + a
print(f"sum of its digit is {a}")

