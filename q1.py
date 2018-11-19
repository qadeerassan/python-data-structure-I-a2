"""
----------------------------------------------------
q1.py
Tests by_origin in food_utilities.
----------------------------------------------------
Author: Qadeer Assan
ID: 160257370
Email: assa7370@mylaurier.ca
_updated_="2018-01-18"
----------------------------------------------------
"""
from food_utilities import by_origin, read_foods
from food import Food
file_variable = open(file = "food.txt", mode = "r")
foods = read_foods(file_variable)

print(Food.origins())
origin = int(input("Input an integer for the origin: "))
origins = by_origin(foods, origin)

for i in origins:
    print(i)
    
file_variable.close()