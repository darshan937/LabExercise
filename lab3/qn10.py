'''10.	Write a Python program that accepts a string and
 calculate the number of digits and letters '''
string = str(input("enter a string: "))
countdigit = 0
countletter = 0
for i in string:
    if i.isnumeric() :
        countdigit +=1
    else:
        countletter += 1
print("number of digits",countdigit)
print("number of letters",countletter)

