# challenge - include two inputs, a list, a for loop over this list, a function combined with input

my_name = input("What is your name? ") # input 1

print(f"Welcome, {my_name}")


fave_food = ["Pizza", "Tacos", "Ramen"] # list
print("My favourite foods are:")
for item in fave_food: # for loop
    print(item)


my_fave_food = input("What is your favourite food? ") # input 2


def food_taste(): # function combined with input
    print(f"{my_fave_food}, wow that sounds delicious!")
    print(f"You have great taste in food, {my_name}!")

food_taste()