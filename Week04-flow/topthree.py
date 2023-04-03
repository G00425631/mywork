#topthree.py

#This program generates 10 random numbers (0-100)& prints them
#then prints out the top three

#Authour: Dorina Agache

import random

howMany = 10
topHowMany = 3
rangeFrom = 0
rangeTo = 100

numbers = []

for i in range(0,howMany):
    numbers.append(random.randint(rangeFrom,rangeTo))
print (f"{howMany} random numbers\t {numbers}")


topOnes = numbers.copy()

topOnes.sort(reverse = True)
print (f"the top {topHowMany} are \t\t {topOnes[0:topHowMany]}")
