#The stock program tracks and reports 3 stocks on its costs and profit or loss.

#Data_STOCK 1

stock_name_1 = input("Enter Stock Name in Uppercase : ")
Num_shares_1 = int(input("Enter Number of Shares : "))
Purch_price_1 = float(input("Enter Purchase Price : "))
sell_price_1 = float(input("Enter Selling Price : "))
commisson_1 = float(input("Enter Commission (in percent): "))
print("\n")

#Processing_STOCK 1
amount_paid_1 = Num_shares_1 * Purch_price_1
commisson_per_1 = commisson_1 / 100.0
commission_bought_1 = amount_paid_1 * commisson_per_1
amount_sold_1 = Num_shares_1 * sell_price_1
commission_sold_1 = amount_sold_1 * commisson_per_1
profit_1 = (amount_sold_1 - commission_sold_1) - (amount_paid_1 + commission_bought_1)

#Output_STOCK 1
print("*"*33)
print("* Enter Information for Stock 1 *")
print("*"*33)
print("-"*60)
print(stock_name_1)
print("")
print("Amount paid for the stock:          $",format(amount_paid_1, "13,.2f"))
print("Commission paid on the purchase:    $",format(commission_bought_1, "13,.2f"))
print("Amount the stock sold for:          $",format(amount_sold_1, "13,.2f"))
print("Commission paid on the sale:        $",format(commission_sold_1, "13,.2f"))
print("Profit (or loss if negative):       $",format(profit_1, "13,.2f"))
print("")
print("-"*60)
print("\n")

#Data_STOCK 2
print("*"*33)
print("* Enter Information for Stock 2 *")
print("*"*33)
stock_name_2 = input("Enter Stock Name in Uppercase : ")
Num_shares_2 = int(input("Enter Number of Shares : "))
Purch_price_2 = float(input("Enter Purchase Price : "))
sell_price_2 = float(input("Enter Selling Price : "))
commisson_2 = float(input("Enter Commission (in percent) : "))
print("\n")

#Processing_STOCK 2
amount_paid_2 = Num_shares_2 * Purch_price_2
commisson_per_2 = commisson_2 / 100.0
commission_bought_2 = amount_paid_2 * commisson_per_2
amount_sold_2 = Num_shares_2 * sell_price_2
commission_sold_2 = amount_sold_2 * commisson_per_2
profit_2 = (amount_sold_2 - commission_sold_2) - (amount_paid_2 + commission_bought_2)

#Output_STOCK 2
print("-"*60)
print(stock_name_2)
print("")
print("Amount paid for the stock:          $",format(amount_paid_2, "13,.2f"))
print("Commission paid on the purchase:    $",format(commission_bought_2, "13,.2f"))
print("Amount the stock sold for:          $",format(amount_sold_2, "13,.2f"))
print("Commission paid on the sale:        $",format(commission_sold_2, "13,.2f"))
print("Profit (or loss if negative):       $",format(profit_2, "13,.2f"))
print("")
print("-"*60)
print("\n")

#Data_STOCK 3
print("*"*33)
print("* Enter Information for Stock 3 *")
print("*"*33)
stock_name_3 = input("Enter Stock Name in Uppercase : ")
Num_shares_3 = int(input("Enter Number of Shares : "))
Purch_price_3 = float(input("Enter Purchase Price : "))
sell_price_3 = float(input("Enter Selling Price : "))
commisson_3 = float(input("Enter Commission (in percent): "))
print("\n")

#Processing_STOCK 3
amount_paid_3 = Num_shares_3 * Purch_price_3
commisson_per_3 = commisson_3 / 100.0
commission_bought_3 = amount_paid_3 * commisson_per_3
amount_sold_3 = Num_shares_3 * sell_price_3
commission_sold_3 = amount_sold_3 * commisson_per_3
profit_3 = (amount_sold_3 - commission_sold_3) - (amount_paid_3 + commission_bought_3)

#Output_STOCK 3
print("-"*60)
print(stock_name_3)
print("")
print("Amount paid for the stock:          $",format(amount_paid_3, "13,.2f"))
print("Commission paid on the purchase:    $",format(commission_bought_3, "13,.2f"))
print("Amount the stock sold for:          $",format(amount_sold_3, "13,.2f"))
print("Commission paid on the sale:        $",format(commission_sold_3, "13,.2f"))
print("Profit (or loss if negative):       $",format(profit_3, "13,.2f"))
print("")
print("-"*60)
print("\n")
