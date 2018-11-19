"""
----------------------------------------------------
q4.py
Tests food_table.
----------------------------------------------------
Author: Qadeer Assan
ID: 160257370
Email: assa7370@mylaurier.ca
_updated_="2018-01-18"
----------------------------------------------------
"""
from food_utilities import food_table, read_foods
from food import Food
file_variable = open(file = "food.txt", mode = "r")
foods = read_foods(file_variable)

food_table(foods)

file_variable.close()