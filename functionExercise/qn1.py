'''
Q.No.1 Write a Python function to find the Max of three numbers
'''
def max(a,b,c):
    if a > b and a > c :
        return a
    elif b > a and b > c :
        return b
    elif c > a and c > a :
        return c

print(max(1,2,3))






