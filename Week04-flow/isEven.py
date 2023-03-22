#isEven.py
#This program will tell the user if a number is even or odd
#Author: Dorina Agache

number= int(input("Please enter an integer:"))

if (number % 2) == 0:
    print (f"{number} is an even number")
else:
    print (f"{number} is an odd number")