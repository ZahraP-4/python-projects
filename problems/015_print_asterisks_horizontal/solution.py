#The program prints the given number of asterisks horizontally.

#input/data
stars = int(input("How many stars you want? : "))

#Calculations/Output
num = 0
while num < stars:
    print("*", end="")
    num += 1
