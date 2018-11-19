"""
----------------------------------------------------
q3.py
Tests calories_by_origin.
----------------------------------------------------
Author: Qadeer Assan
ID: 160257370
Email: assa7370@mylaurier.ca
_updated_="2018-01-18"
----------------------------------------------------
"""
from food_utilities import calories_by_origin, read_foods
from food import Food
file_variable = open(file = "food.txt", mode = "r")
foods = read_foods(file_variable)

print(Food.origins())
origin = int(input("Input an integer for the origin: "))
avg = calories_by_origin(foods, origin)
print("Average calories of {} origin: {}".format(Food.ORIGIN[origin], avg))

file_variable.close()