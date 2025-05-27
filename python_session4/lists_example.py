
fave_food = ["Pizza", "Cheese", "Apple", "Cheesecake"]

# give the second item in the list

print(fave_food[1])


numbers = [10, 40, 23, 3, 36]

print(len(numbers)) # 5
print(max(numbers)) # 40
print(min(numbers)) # 3
print(sorted(numbers)) # 3, 10, 23, 36, 40
print(reversed(numbers)) # will produce a memory location - list reverse iterator - convert to a list
print(list(reversed(numbers)))

print(sorted(list(reversed(numbers)))) # can wrap the functions


"""
I want to work out how much money I've spent on lunch this week.
I've created a list of what I spent each day.
Write a program that uses a for loop to calculate total cost.
"""

# costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
# total_cost = 0

costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = 0

for cost in costs: # why for loop - cleaner than while loop
    total_cost += cost # each time, for each item in the loop it adds to the total until it runs out of items

print(round(total_cost,2)) # the round method round(value,number of dp) will round it