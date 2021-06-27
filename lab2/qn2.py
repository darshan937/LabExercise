'''2. WAP which accepts marks of four subjects and display total marks, percentage and grade.
 Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass,
 less than 40% –> fail'''
sub1 = int(input("enter your mark in first subject: "))
sub2 = int(input("enter your mark in second subject: "))
sub3 = int(input("enter your mark in third subject: "))
sub4 = int(input("enter your mark in fourth subject: "))
total_marks = sub1 + sub2 + sub3 + sub4
percent = (total_marks / 400) * 100
if percent > 70:
    print ("you got distinction")
elif percent > 40:
    print("you got pass")
else :
    print("you got fail")




