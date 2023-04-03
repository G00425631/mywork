#guess1.py

#This prompts the user to guess a number
# the program keeps prompting the user to 
#guess the number until the user gets the right one

# Authour: Dorina Agache

numbertoguess = 30

guess = int (input("Please guess the number:"))

while guess != numbertoguess:
    print ("Wrong answer :-( ")
    guess = int (input("Please guess again:"))

print ("Well done! Yes, the number was ", numbertoguess)