#This program calculates and displays the simple interest.

#data
def show_interest(rate = 0.01, period = 10, principal = 10000.00) -> None:
    '''The show_interest function calculates the simple interest.'''
    
    # Calculate
    interest = principal * rate * period

    # Output
    return interest


def main():
    interest = show_interest()
    print('The simple interest will be $', format(interest, ',.2f'), sep='')

    
if __name__ == "__main__":
    main()
