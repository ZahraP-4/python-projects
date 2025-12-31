#Program reverses a four-digit integer.

#input/data
number = int(input("Enter an integer: "))

#Calculations/Processing
digit_1 = (number %  10)
digit_2 = (number // 10) % 10
digit_3 = (number // 100) % 10
digit_4 = (number // 1000) % 10
 
#Output
print(digit_1)
print(digit_2)
print(digit_3)
print(digit_4)
