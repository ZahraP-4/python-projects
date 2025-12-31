#The program converts speeds from 60kph through 130kph to mph.

#Initialize
con_factor = 0.6214
print("KPH\t MPH")
print("-------------------------------")

#Calculations/Output
for speed_kph in range(60, 131, 10):
    speed_mph = speed_kph * con_factor
    print(speed_kph, "\t", format(speed_mph, ".1f"))
