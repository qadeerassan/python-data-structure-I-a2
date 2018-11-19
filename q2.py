"""
----------------------------------------------------
q2.py
Tests average_calories.
----------------------------------------------------
Author: Qadeer Assan
ID: 160257370
Email: assa7370@mylaurier.ca
_updated_="2018-01-18"
----------------------------------------------------
"""
from food_utilities import average_calories, read_foods
from food import Food
file_variable = open(file = "food.txt", mode = "r")
foods = read_foods(file_variable)

avg = average_calories(foods)
print("Average calories:", avg)

file_variable.close()