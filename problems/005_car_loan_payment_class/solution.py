#This program calculates monthly and total payments for a car loan.

#Processing/Output
class Loan:
    """Loan class that stores loan data and computes payments."""
    def __init__(self, annualInterestRate=2.5, numberOfYears=1,
                 loanAmount=1000, borrower=" "):
        self.__annualInterestRate = annualInterestRate
        self.__numberOfYears = numberOfYears
        self.__loanAmount = loanAmount
        self.__borrower = borrower
        
    def getAnnualInterestRate(self):
        """Return the annual interest rate."""
        return self.__annualInterestRate

    def getNumberOfYears(self):
        """Return the loan term in years."""
        return self.__numberOfYears

    def getLoanAmount(self):
        """Return the current loan principal amount."""
        return self.__loanAmount

    def getBorrower(self):
        """Return the borrower's full name."""
        return self.__borrower

    def setAnnualInterestRate(self, rate):
        """Update the annual interest rate."""
        self.__annualInterestRate = rate

    def setNumberOfYears(self, years):
        """Update the number of years for the loan."""
        self.__numberOfYears = years

    def setLoanAmount(self, amount):
        """Update the loan principal amount."""
        self.__loanAmount = amount

    def setBorrower(self, borrower):
        """Update the borrower's name."""
        self.__borrower = borrower

    def getMonthlyPayment(self):
        """Compute and return the monthly payment."""
        monthlyInterestRate = self.__annualInterestRate / 1200
        monthlyPayment = (self.__loanAmount * monthlyInterestRate) / \
            (1 - (1 / (1 + monthlyInterestRate) ** (self.__numberOfYears * 12)))
        return monthlyPayment

    def getTotalPayment(self):
        """Compute and return the total payment across the full loan term."""
        total = self.getMonthlyPayment() * self.__numberOfYears * 12
        return total
    
def main():
    annualRate = float(input("Enter yearly interest rate: "))
    years = int(input("Enter number of years as an integer: "))
    amount = float(input("Enter loan amount: "))
    name = input("Enter a borrower's name: ")
    loan = Loan(annualRate, years, amount, name)

    print("The loan is for", loan.getBorrower())
    print("The monthly payment is", format(loan.getMonthlyPayment(), ".2f"))
    print("The total payment is", format(loan.getTotalPayment(), ",.2f"))

    choice = input("Do you want to change the loan amount? "
                   "Y for yes or enter to quit ")
    while choice == "Y" or choice == "y":
        newAmount = float(input("Enter new loan amount "))
        loan.setLoanAmount(newAmount)

        print("The loan is for", loan.getBorrower())
        print("The monthly payment is", format(loan.getMonthlyPayment(), ".2f"))
        print("The total payment is", format(loan.getTotalPayment(), ",.2f"))

        choice = input("Do you want to change the loan amount? "
                       "Y for yes or enter to quit ")

main()
