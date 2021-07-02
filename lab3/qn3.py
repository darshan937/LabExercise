'''3.	Write a Python program to guess a number between 1 to 9.
  Note : User is prompted to enter a guess. If the user guesses wrong then
   the prompt appears again until the guess is correct, on successful guess,
   user will get a "Well guessed!" message, and the program will exit.
'''
import random
x = random.randint(1,9)
for i in range(1,10):
    while i == x  :
        a = int(input("enter a guess number from 1 to 9: "))
        if a == x:
            print("well guessed!!")
            break
        elif a>9:
            print("you cannot guess more than 9 ")
        else:
            print("sorry, your guess is wrong!")


