# example of a dictionary

briony_car = {
    "colour": "blue",
    "company": "Suzuki",
    "model": "Swift",
    "year": "2016",
    "wheels": 4,
    "is_working": True,
    "condition_of_wheels": ["good", "okay", "bad"], # this is still a key value pair, with a list data type
    "current_location": {
        "lat": 12.2323,
        "long": 63.222,
    } # this is a nested dictionary
}

# how to grab a property value

car_colour = briony_car["colour"]
print("Car colour: ", car_colour)

bad_tyre = briony_car["condition_of_wheels"][2] # this calls the index in the list
print(bad_tyre)

latitude = briony_car["current_location"]["lat"] # this targets the specific value in the dictionary
print(latitude)

# to add another key and value

briony_car["is_happy"] = True
print(briony_car)




# another example

briony = {
    "age": 30,
    "eye_colour": "blue",
    "hair_colour": "ginger",
    "fave_food": "ramen",
    "location": "London",
}

briony_age = briony["age"]
print("Briony's age: ", briony_age)



# list of dictionaries - this functions like a loop

fruits = [
    {"name": "apple", "colour": "red", "price": 0.12},
    {"name": "banana", "colour": "yellow", "price": 0.2},
    {"name": "pear", "colour": "green", "price": 0.19},
]

total_cost = 0
for fruit in fruits: # naming convention for looping a list - for singular in plural
    total_cost += fruit["price"]

print("Total fruits cost: £", total_cost)