#The program calculates the property tax.

#initialize
tax_factor = 0.0065

#input/data
print("Enter the property lot number or enter -999 to end")
lot_num = int(input("Enter the lot number : "))

#Calculations/Output
while lot_num != -999:
    property_value = float(input("Enter property value: "))
    property_tax = property_value * tax_factor
    print("Property tax : $",format(property_tax,".2f"),sep="")
    print("\nEnter the property lot number or enter -999 to end")
    lot_num = int(input("Enter the lot number : "))
