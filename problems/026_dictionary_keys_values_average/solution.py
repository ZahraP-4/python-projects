#This program prints keys, values, and averages from a dictionary.

# Initials
grade = {"A": 8, "D": 3, "B": 15, "F": 2, "C": 6}
total = 0
count = 0

# Processing / Output
# a. All the keys
print("All the keys:")
for key in grade.keys():
    print(key)
# b. All the values
print("\nAll the values:")
for value in grade.values():
    print(value)
# c. All key and value pairs
print("\nAll key and value pairs:")
for key, value in grade.items():
    print(key, value)
# d. All key and value pairs in key order
print("\nAll key and value pairs in key order:")
for key in sorted(grade.keys()):
    print(key, grade[key])
# e. The average value
for value in grade.values():
    total += value
    count += 1
average = total / count
print("\nAverage value:", average)
