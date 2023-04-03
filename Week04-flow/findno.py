#findno.py
#This program uses a while loop to modify 1 so that it keeps prompting the
#user for a number until the user enters -1

#Author: Dorina Agache 

print("Your task is to find a certain number, let's start!")

numberToGuess = -1

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print ("The number you have guessed is too low!")
    else:
        print ("The number you have guessed is too high!")
    guess = int(input("Please guess again:"))

print ("CONGRATULATIONS! The number you were looking for is" , numberToGuess)