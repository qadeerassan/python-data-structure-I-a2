"""
----------------------------------------------------
q5.py
Tests food_search.
----------------------------------------------------
Author: Qadeer Assan
ID: 160257370
Email: assa7370@mylaurier.ca
_updated_="2018-01-18"
----------------------------------------------------
"""
from food_utilities import food_search, read_foods
from food import Food
file_variable = open(file = "food.txt", mode = "r")
foods = read_foods(file_variable)

origin = int(input("Integer for origin (-1 if N/A): "))
max_cals = int(input("Maximum calories (0 if N/A): "))
is_veg = bool(input("Vegetarian (True/False if N/A): "))

results = food_search(foods, origin, max_cals, is_veg)
for i in results:
    print(i)
    
file_variable.close()