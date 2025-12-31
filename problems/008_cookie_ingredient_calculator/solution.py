#Program calculates ingredient amounts for any number of cookies.

#input/data
num_cookies = float(input("Enter the number of cookies:"))
print('')

#Calculations/Processing
sugar = (1.5 / 48) * num_cookies
butter = (1 / 48) * num_cookies
flour = (2.75 / 48) * num_cookies

#Output
print("To make", format(num_cookies,'.1f'),"cookies, you will need:") 
print(format(sugar, '.2f'),"cups of sugar")
print(format(butter, '.2f'),"cups of butter") 
print(format(flour, '.2f'),"cups of flour")
