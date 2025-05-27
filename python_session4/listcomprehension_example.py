"""
Basically what this means is:
[WHAT_TO_KEEP for item in OLD_LIST if MEETS_THIS_CONDITION]
"""

numbers = [1, 2, 3, 4, 5, 6, "A"]

new_list = [x * 10 for x in numbers if x != "A"]

print("Old List", numbers)
print("New_list", numbers)