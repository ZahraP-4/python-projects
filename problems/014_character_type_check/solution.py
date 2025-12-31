#The program checks whether a character is a number(0 to 9 only)or a uppercase or lowecase character.

#input/data
char = input("Enter any character : ")

#Calculations/Output
if char >= '0' and char <= '9':
    print("A number was entered")
elif char >= 'A' and char <= 'Z':
    print("Uppercase character was entered")
elif char >= 'a' and char <= 'z':
    print("Lowercase character was entered")
else:
    print("Invalid input")
