#This program reads a sequence of string values into a list and finds the largest number

#input/data
def readValues() -> list:
    ''' The function reads a series of string values from the user 
    and stores them in a list.'''
    values = []
    print('Please enter values, Q to quit:')
    entry = input()
    while entry.upper() != 'Q':
        values.append(entry)
        entry = input()
    return values


def findLargest(values: list) -> float:
    '''The function finds the largest number in a list.'''
    if len(values) > 0:
        largest = float(values[0])
        for val in values:
            if float(val) > largest:
                largest = float(val)
    else:
        largest = 0
    return largest


def display(values: list, largest: float) -> None:
    '''The function prints each value from the list and
    highlight the largest number.'''
    if len(values) > 0:
        print('\nHere are the numbers in the list')
        for val in values:
            if float(val) == largest:
                print(val, '<== this is the largest number')
            else:
                print(val)


def main():
    numbers = readValues()
    largest_value = findLargest(numbers)
    display(numbers, largest_value)

    
if __name__ == "__main__":
    main()
