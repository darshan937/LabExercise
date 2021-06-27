import random
secretnum = random.randint(1,10)
guess = int(input("enter your guess number: "))
attempt = 0

while attempt < 3:
 attempt += 1
if secretnum != guess:
    guess = int(input("guess again: "))
 elif secretnum == guess:\
     print("congratulation! your guess is correct and you won")




