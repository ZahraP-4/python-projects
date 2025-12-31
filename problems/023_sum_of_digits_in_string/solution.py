#This program asks the user to enter a sequence of single-digit numbers and then calculates their sum.

#Calculation
def string_total(number_string: str) -> int:
    '''The function receives a string of digits, 
    converts them into an integer, and calculates 
    the total sum of all digits.'''
    total = 0
    for char in number_string:
        total += int(char)
    return total


#Input/Output
def main():
    # Get a string of numbers as input from the user.
    number_string = input('Enter a sequence of digits with nothing separating them: ')

    # Call string_total function, and store the total.
    total = string_total(number_string)

    # Display the total.
    print('The total of the digits in the string you entered is', total)

    
if __name__ == "__main__":
    main()
