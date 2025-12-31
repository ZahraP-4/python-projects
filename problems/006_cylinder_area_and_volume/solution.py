#Program reads radius and length of a cylinder, then computes base area and volume. 

#input/data
radius = float(input("Enter the radius of a cylinder: "))
length = float(input("Enter the length of a cylinder: "))

#Calculations/Processing
PI = 3.141
base_area = radius * radius * PI 
volume = base_area * length 

#Output
print("The base area is ", base_area)
print("The volume of cylinder is ", volume)
