#guess2.py

#This prompts the user to guess a number
# the program keeps prompting the user to 
#guess the number until the user gets the right one
# The program tells the user if the numebr is too high/low

# Authour: Dorina Agache

numberToGuess = 30

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print ("The number you have guessed is too low!")
    else:
        print ("The number you have guessed is too high!")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was ", numberToGuess)