#avarage.py

#This program  keeps reading numbers until the user
# enters a 0. 
#The program should then print out each of the 
#numbers entered and the average of them

# Authour: Dorina Agache

numbers = []

# first number then we check if it is 0 in the while loop

number = int(input ("Enter number (0 to quit):"))

while number !=0:
    numbers.append(number) 

    # read the next number and check if 0
    number = int(input("Enter anotehr number (0 to quit):"))

for value in numbers:
    print (value)

#avarage of the numbers entered will be a float
avarage= float(sum(numbers)) / len(numbers)

print ("The avarage is " , avarage)