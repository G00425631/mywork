#guess2.py

#This prompts the user to guess a number
# The program generates a random number for the user to guess between 0 to 100
# the program keeps prompting the user to 
# guess the number until the user gets the right one
# The program tells the user if the number is too high/low

# Authour: Dorina Agache
import random

numberToGuess = random.randint(0, 100) 
#I looked up W3 schools for this function:https://www.w3schools.com/python/module_random.asp

print ("A random number was generated, time to guess!")

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print ("The number you have guessed is too low!")
    else:
        print ("The number you have guessed is too high!")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was ", numberToGuess)