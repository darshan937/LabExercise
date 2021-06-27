'''Q.No.6 Write a Python program to reverse a string. '''
def reverse(string):
    reversed_string=""
    for i in string:
        reversed_string= i + reversed_string
    print(f"the reveresed string is {reversed_string}")
string = str(input("enter a string: "))
print("the reverse string is : ",string)
reverse(string)