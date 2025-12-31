#Program calculates Earth's gravity on a person

#input/data
mass_E =  5.9742 * 10**24
radius_E =  6378 * 10**3
universal_grav =  6.67300 * 10** -11
mass_U = float(input("Enter a mass in kg: "))
print('')

#Calculations/Processing
acc_gravity = ((universal_grav * mass_E * mass_U)/ radius_E ** 2) / mass_U
 
#Output
print("The resulting value of g is", format(acc_gravity, '.4f'), "which is close to the earth’s gravitational force")
