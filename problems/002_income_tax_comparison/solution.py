#The program calculates and compares the old and new income tax based on the user’s taxble income.

#Input
income = int(input("Enter income as an integer with no commas: "))
             
#Calculations
while income >= 0:
#New income tax brackets (2018 and newer)
    if income <= 9525:
        tax_2018 = income * 0.10
    elif 9525 < income and income <= 38700:
        tax_2018 = ((9525 * 0.10) +
                    (income - 9525) * 0.12)
    elif 38700 < income and income <= 82500:
        tax_2018 = ((9525 * 0.10) +
                    (38700 - 9525) * 0.12 +
                    (income - 38700) * 0.22)
    elif 82500 < income and income <= 157500:
        tax_2018 = ((9525 * 0.10) +
                    (38700 - 9525) * 0.12 +
                    (82500 - 38700) * 0.22 +
                    (income - 82500) * 0.24)
    elif 157500 < income and income <= 200000:
        tax_2018 = ((9525 * 0.10) +
                    (38700 - 9525) * 0.12 +
                    (82500 - 38700) * 0.22 +
                    (157500 - 82500) * 0.24 +
                    (income - 157500) * 0.32)
    elif 200000 < income and income <= 500000:
        tax_2018 = ((9525 * 0.10) +
                    (38700 - 9525) * 0.12 +
                    (82500 - 38700) * 0.22 +
                    (157500 - 82500) * 0.24 +
                    (200000 - 157500) * 0.32 +
                    (income - 200000) * 0.35)
    elif income > 500000:
        tax_2018 = ((9525 * 0.10) +
                    (38700 - 9525) * 0.12 +
                    (82500 - 38700) * 0.22 +
                    (157500 - 82500) * 0.24 +
                    (200000 - 157500) * 0.32 +
                    (500000 - 200000) * 0.35 +
                    (income - 500000) * 0.37)
#Old income tax brackets (2017 and older)
    if income <= 9325:
        tax_2017 = income * 0.10
    elif 9325 < income and income <= 37950:
        tax_2017 = ((9325 * 0.10) +
                    (income - 9325) * 0.15)
    elif 37950 < income and income <= 91900:
        tax_2017 = ((9325 * 0.10) +
                    (37950 - 9325) * 0.15 +
                    (income - 37950) * 0.25)
    elif 91900 < income and income <= 191650:
        tax_2017 = ((9325 * 0.10) +
                    (37950 - 9325) * 0.15 +
                    (91900 - 37950) * 0.25 +
                    (income - 91900) * 0.28)
    elif 191650 < income and income <= 416700:
        tax_2017 = ((9325 * 0.10) +
                    (37950 - 9325) * 0.15 +
                    (91900 - 37950) * 0.25 +
                    (191650 - 91900) * 0.28 +
                    (income - 191650) * 0.33)
    elif 416700 < income and income <= 418400:
        tax_2017 = ((9325 * 0.10) +
                    (37950 - 9325) * 0.15 +
                    (91900 - 37950) * 0.25 +
                    (191650 - 91900) * 0.28 +
                    (416700 - 191650) * 0.33 +
                    (income - 416700) * 0.35)
    elif income > 418400:
        tax_2017 = ((9325 * 0.10) +
                    (37950 - 9325) * 0.15 +
                    (91900 - 37950) * 0.25 +
                    (191650 - 91900) * 0.28 +
                    (416700 - 191650) * 0.33 +
                    (418400 - 416700) * 0.35 +
                    (income - 418400) * 0.396)
    tax_diff = tax_2018 - tax_2017
    if tax_2017 == 0 :
       tax_diff_perc = 0.00
    else:
         tax_diff_perc = (tax_diff / tax_2017) * 100
         if tax_diff_perc < 0:
            tax_diff_perc *= -1   
    print("Income:", income)
    print("2017 tax:", format(tax_2017, ".2f"))
    print("2018 tax:", format(tax_2018, ".2f"))
    print("Difference:", format(tax_diff, ".2f"))
    print("Difference (percent):", format(tax_diff_perc, ".2f"))
    income = int(input("\nEnter income as an integer with no commas: "))

