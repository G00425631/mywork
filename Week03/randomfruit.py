#randomfruit.py
#This program prints out a random fruit
#Author: Dorina Agache

import random

fruits= ['Raspberries', 'Watermelon', 'Apricots', 'Peaches']

index= random.randint(0, len(fruits)-1)
#Consulted chatGPT to understand this time of code and explanation is below:
#The first argument is the lower bound of the range of values we want to generate. We set it to 0 because the first index in a Python list is 0.
#The second argument is the upper bound of the range of values we want to generate. We set it to len(fruits)-1 because the last index in a Python list is always one less than the length of the list (since Python lists are zero-indexed).

fruit= fruits[index]
print("A random fruit Milady: {}".format(fruit))