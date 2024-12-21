# number guessing game make a variable winning game and assign any no to it ask user to guess a no
#if guessed correctly print you win if not than give hint as too low or too high

import random
random_no=random.randint(1,100) ##this generates any random number for this we have to import it
winning_num=random_no
#winning_num=70
guess_number=int(input("guess a number: ")) 
if winning_num==guess_number: 
        print("YOU WIN")
else: #nested if else
        if guess_number<winning_num:
            print("Too Low")
        else:
            print("Too High")
while (guess_number!=winning_num):
    guess_number=int(input("guess a number again: "))
    if winning_num==guess_number: 
        print("YOU WIN")
    else: #nested if else
        if guess_number<winning_num:
            print("Too Low")
        else:
            print("Too High")
print(random_no)