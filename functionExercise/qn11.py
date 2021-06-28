'''Write a python program to check whether the number is Armstrong number or not using function:
[Hint: 153 - 1*1*1 + 5*5*5 + 3*3*3]'''
def armstrong(num):
    a = num
    z = 0
    digits = len(str(num))
    while a != 0 :
        x = a%10
        y = x ** digits
        z += y
        a//=10
    if num == z:
        print("the given number is armstrong")
    else:
        print("the given number is not armstrong")
num = int(input("enter a number : "))
armstrong(num)












