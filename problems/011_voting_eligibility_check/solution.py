#The program determines whether a person is eligible (18 years old) to vote or not.

#input/data
age= int(input("Enter the age : "))

#Calculations/Output
if age >= 18:
         print("You are eligible to cast your vote.")
else:
    dif_age = 18 - age
    print("You have to wait for another",dif_age ,"years to cast your vote")
