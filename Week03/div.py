#div.py
#This program reads in two numbers and outputs the integer answer and remainder
#Author: Dorina Agache

x= int(input('Enter your chosen number:'))
y= int(input('Enter the number you want to divide by:'))
answer= int(x//y)
remainder= x%y

print('{} divided by {} is {} with remainder {}'. format(x, y, answer, remainder))