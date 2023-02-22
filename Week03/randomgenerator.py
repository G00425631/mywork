#randomgenerator.py
#This program prints out a random number between 2 inputted numbers
#Author: Dorina Agache

import random
x= int(input("Enter lower number: "))
y= int(input("Enter higher number: "))

number= random.randint(x,y)
print("Here is a random number {}" .format(number))

#consulted chat GPT as noted error appeared if number not inputted as lower and higher respectively