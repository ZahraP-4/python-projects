#User inputs wholesale prices and the program calculates retail prices.

#Initialize
markup = 2.5
again = "y"
valid = True

#Input
whole_cost = float(input("Enter the item’s wholesale cost: "))

#Calculations/Output:
while valid == True:
    if whole_cost < 0:
        print("ERROR: the cost cannot be negative")
        whole_cost = float(input("Enter the correct wholesale cost: "))
    else:
        retail_price = whole_cost * markup
        print("Retail price is $", format(retail_price, ".2f"), sep="")
        again = input("Do you have another item? (Enter y for yes): ")
        if again == "y" or again == "Y":
            whole_cost = float(input("Enter the item’s wholesale cost: "))
        else:
            valid = False
