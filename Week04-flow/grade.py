#grade.py
#This program reads in a student’s percentage mark and prints out 
#corresponding grade:
# Under 40% => Fail
# Between 40% and 49% => Pass
# Between 50% and 59% => Merit 2
# Between 60% and 69% => Merit 1
#Over 70% => Distinction

#Author: Dorina Agache 

percentage = int(input("Please enter the precentage: "))
print(f"The student's precentage is {percentage}")

if percentage < 0 or percentage > 100:
    print ("Please enter a nuber between 0 and 100")

elif percentage < 40:
     print ("Fail")
    
elif percentage < 50:
     print("Pass")

elif percentage < 60:
     print("Merit 2")

elif percentage < 70:
     print("Merit 1")

else:
     print("Distinction")