'''5. A school decided to replace the desks in three classrooms. Each desk sits two students.
 Given the number of students in each class, print the smallest possible number of desks that
  can be purchased.
The program should read three integers: the number of students in each of the three
 classes, a, b and c respectively.
In the first test there are three groups. The first group has 20 students and
 thus needs 10 desks. The second group has 21 students, so they can get by with
 no fewer than 11 desks. 11 desks are also enough for the third group of 22 students.
 So, we need 32 desks in total.'''
class1 = int(input("enter number of students in 1st class: "))
class2 = int(input("enter number of students in 2nd class: "))
class3 = int(input("enter number of students in 3rd class: "))

deskclass1 = class1//2
remainstudents1 = class1%2
print(f"the number of desk needed in 1st class is {deskclass1 + remainstudents1 }")
deskclass2 = class2//2
remainstudents2 = class2%2
print(f"the number of desk needed in 2nd class is {deskclass2 + remainstudents2}")
deskclass3 = class3//2
remainstudents3 = class3%2
print(f"the number of desk needed in 3rd class is {deskclass3 + remainstudents3}")

