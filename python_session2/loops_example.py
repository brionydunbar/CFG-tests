# looping characters
for char in "Briony":
    print(char)

# looping lists
for person in ["Sam", "Sally", "Bob", "Jess"]:
    print(person)

# looping ranges
for num in range(4):
    print(num)

for num in range(2+8): # can do arithmetic here too
    print(num)


# create own favourite food list and loop over it
# e.g. fav_food = ["Pizza", "Cheese", "Fish"]

fav_food = ["Pizza", "Ramen", "Tacos"]
for item in fav_food:
    print(f"My favourite food: ", item) # item is a placeholder variable

print(f"My favourite food: ")
for item in fav_food:
    print(item) # this indentation is the scope of the loop
    print("Delicious!") # so this is included in the scope
print("So delicious!") # and this is outside of the scope




store_capacity = 10 # people

while store_capacity > 0:
    print("Please come in. Spaces available: " + str(store_capacity))
    store_capacity = store_capacity - 1

print("Please wait for someone to exit the store")