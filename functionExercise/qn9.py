'''Q.No.9 Write a Python function that checks whether a passed string is palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward,
 e.g., madam or nurses run.
'''
def palindrome(string):
    reversed_string = ""
    for i in string:
        reversed_string = i + reversed_string
    if string == reversed_string :
        print("the string is palindrome")
    else :
        print("the string is not a palindrome")
string = str(input("enter a string: "))
palindrome(string)


