'''
  If name is less than 3 characters long- name must be at least 3 characters
  otherwise if it's more than 50 characters - name must be maximum of 50 characters
  otherwise - name looks good!
'''
name = input("enter your name: ")
if len(name)<3:
    print("the name must be at least 3 characters")
elif len(name)>50:
    print("the name must be maximum of 50 characters")
else:
    print("the name looks good!")

