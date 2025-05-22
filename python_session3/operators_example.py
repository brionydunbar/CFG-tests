"""
Booleans (bool) in Python have two values: True and False
Comparison operators always create boolean results
Logical operators include "and", "or" and "not"
"""

# simple true/false values with comparison operators
light_colour = "green"

if light_colour == "green": #light_colour is the variable, use == (comparison operator)
    print("Go")

if light_colour == "red":
    print("Stop")


# temp example to show comparative operators
temperature = 26

print(temperature > 30) # will print false as 26 is less than 30

# go to the beach example to show logical operators

is_sunny = True # must use capital T

go_to_the_beach = (temperature > 25) and is_sunny # the logical operator evaluates the bools
# but better to use with if condition

print("Should I go to the beach: ", go_to_the_beach)

