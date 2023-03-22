#hotandcold.py
#This program uses a while loop to modify 1 so that it keeps prompting the
#user for a number until the user enters -1

#Author: Dorina Agache 

print("Your task is to find a cerain number, let's start!")
number = int(input("Please enter a number: "))

while number != -1 :
    print ("You are very far from our number")
    number = int (input("Enter a different number (hint: less than 10): "))
else :
 print ("CONGRATULATIONS! The number you were looking for is -1")
         
