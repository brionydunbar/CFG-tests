"""
Write a function named 'recap' that:
1. Takes one argument called "aNumber"
2. loops from 0 until and including the argument "aNumber"
3. if it finds the value 42, it prints out "Found the meaning of life!"
4. If not value 42 was found it prints "Did not find 42 - sadface" only once
Prompt the user for a number and pass it into the function "recap"
"""

def recap(aNumber):
    found = False
    for num in range(0, aNumber + 1):
        if num == 42:
            print("Found the meaning of life!")
            found = True
            break
    if not found:
        print("Did not find 42 - sadface")

aNumber = int(input("Please enter a number: "))
recap(aNumber)