#If Else Random Number
#Random Generation
import random

secret_number = random.randint(1, 10)

#User Inputs
guess1 = input("Guess a number between 1 and 10: ")
guess = int(guess1)

if guess == secret_number:
    print("Correct!")

elif guess > secret_number:
    print("Too High!")

else:
    print("Too Low!")