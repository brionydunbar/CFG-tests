
# creating a function
def say_hello_cheese():
    print("Hello nice to meet you! I like cheese! Do you like cheese?")
    print("Yes I do! Thank you.")


say_hello_cheese()


# creating own function example
def say_hello_cake():
    print("Hello, nice to meet you! I like cake! Do you like cake?")
    print("Yes I do! I love cake!")


say_hello_cake()



# creating own useful function
def say_hello(your_name): # your_name is the argument, this is a placeholder
    print(f"Hello! Nice to meet you {your_name}") #use an f string

say_hello("Briony") # the function has accepted the argument
say_hello("Jess")
say_hello("Sanaa")



# adding to the argument

def say_hello(your_name, your_location): # name is the argument, this is a placeholder
    print(f"Hello! Nice to meet you {your_name} from {your_location}.") #use an f string

say_hello("Briony", "London") # the function has accepted the argument
say_hello("Jess", "Wales")
say_hello("Sanaa", "London")



# return value

def say_hello(your_name):
    return f"Hello! Nice to meet you {your_name}" # adds a return value

# can use print(say_hello("Briony"))
saying_hello = say_hello("Briony")
print(saying_hello)


# using functions for arithmetic

def adder(num1, num2): # adder is the function, num1 and num2 are placeholders
    return num1 + num2

add_2_2 = adder(2, 2) # the function is being called with adder()
print(add_2_2) # the return of 2 + 2 for the add_2_2 variable is then printed