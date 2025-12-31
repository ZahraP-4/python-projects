#The program uses a for loop to calculate the sum of numbers.

#Initialize
total = 0

#Input
count = int(input("How many numbers do you want to add? "))
            
#Calculations/Output:
for times in range(count):
    print("Enter number",times +1 ,": ", end="")
    num = float(input())
    total += num
                  
print("The total is", format(total, ".1f"))
