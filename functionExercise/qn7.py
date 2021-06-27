'''Q.No.7 Write a Python function that accepts a string and
calculate the number of upper case letters and lower case letters'''
def letters(string):
    x=0
    y=0
    for i in string:
        if i.islower():
            x = x + 1
        elif i.isupper():
            y = y + 1
    print(f"there are {x} lowercase letter and {y} uppercase letter in the string.")
string = str(input('enter a string: '))
print("the string is: ",string)
letters(string)
