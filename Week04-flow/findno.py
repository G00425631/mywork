#findno.py
#This program uses a while loop to modify 1 so that it keeps prompting the
#user for a number until the user enters -1

#Author: Dorina Agache 

print("Your task is to find a cerain number, let's start!")

number = int(input("Please enter a number: "))


while number < -100 or number > 100:
    number = int(input("You are very far from the number you are looking for, try a two digit number:" ))
    
elif number < 100 or number > 0:
     print ("Try a negative number instead:") 
    

elif number > -100 or number <0:
     print("Close...it is a negative number we are looking for")
 

elif number >-10 or number <0:
     print("You are very close!")


else :
 print ("CONGRATULATIONS! The number you were looking for is -1")