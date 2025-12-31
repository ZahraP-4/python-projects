#Program Calculates company profit based on 24% of total sales. 

#input/data
total_sale = float(input("Enter the projected total sales : "))

#Calculations/Processing
profit = total_sale * 0.24

#Output
print("The profit made from this amount :" ,format(profit, '.2f'))
