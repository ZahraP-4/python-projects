#The program calculates stock transactions using functions.

#Input\Date
def load() -> (str, int, float, float, float):
    """The user inputs stock name, shares, buy/sell price, and commission."""
    stock_name = input("Enter Stock name: ")
    shares = int(input("Enter Number of shares : "))
    purchase_price = float(input("Enter Purchase price : "))
    selling_price = float(input("Enter selling price : "))
    commission_percent = float(input("Enter Commission : "))
    print("\n")
    return stock_name, shares, purchase_price, selling_price, commission_percent


def calc(shares: int,
         purchase_price: float,
         selling_price: float,
         commission_percent: float) -> (float, float, float, float, float):
    """This function calculates paid/sold amounts, commissions, and profit."""
    rate = commission_percent / 100.0
    amount_paid = shares * purchase_price
    commission_bought = amount_paid * rate
    amount_sold = shares * selling_price
    commission_sold = amount_sold * rate
    profit = (amount_sold - commission_sold) - (amount_paid + commission_bought)
    return amount_paid, commission_bought, amount_sold, commission_sold, profit


def output(stock_name: str,
           amount_paid: float,
           commission_bought: float,
           amount_sold: float,
           commission_sold: float,
           profit: float) -> None:
    """This functions displays results"""
    print("Stock name : ",stock_name)
    print("Amount paid for the stock:          $", format(amount_paid, "13,.2f"))
    print("Commission paid on the purchase:    $", format(commission_bought, "13,.2f"))
    print("Amount the stock sold for:          $", format(amount_sold, "13,.2f"))
    print("Commission paid on the sale:        $", format(commission_sold, "13,.2f"))
    print("Profit (or loss if negative):       $", format(profit, "13,.2f"))
    print('\n')

    
def main():
    response = input("Enter your stock information? Type 'y' for yes, or 'n' for no: ")
    print()
    while response.lower() == 'y':
        stock_name, shares, purchase_price, selling_price, commission_percent = load()
        amount_paid, commission_bought, amount_sold, commission_sold, profit = calc(
            shares, purchase_price, selling_price, commission_percent
        )
        output(stock_name, amount_paid, commission_bought, amount_sold, commission_sold, profit)
        response = input("Enter your stock information? Type 'y' for yes, or 'n' for no: ")
        print()

        
if __name__ == "__main__":
    main()
