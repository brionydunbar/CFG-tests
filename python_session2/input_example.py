# creating an input function to ask name
my_name = input("What is your name? ")

print(my_name)

# creating an input function to ask age and do math
# my_age = input("What is your age? ")
# my_age = int(input("What is your age? ")) - this is one way to convert to an int
my_age = int(input("What is your age? "))
my_age = my_age + 5 # this is another way

print(my_age)

# creating an input function which will output a message plus the birth year
my_birth_year = int(input("What year were you born? "))

print(f"Your birth year is {my_birth_year}")
