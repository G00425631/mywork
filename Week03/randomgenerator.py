#randomgenerator.py
#This program prints out a random number between 2 inputted numbers
#Author: Dorina Agache

import random
x= int(input("Enter first number: "))
y= int(input("Enter second number: "))

number= random.randint(x,y)
print("Here is a random number {}" .format(number))