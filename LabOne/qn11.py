'''10. Write a Python program to convert seconds to day, hour, minutes and seconds.'''
sec = int(input("enter the time in second: "))
minutes = sec / 60
hours = minutes / 60
day = hours / 24
print(f"the given second time is {minutes} minutes, {hours} hours and {day} days ")