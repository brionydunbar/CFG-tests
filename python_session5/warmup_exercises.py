"""
Create a to-do list program that writes user input to a file

The program should:

Ask the user to input a new to-do item
Read the contents of the existing to-do items
Add the new to do item to the existing to-do items
Save the updated to-do items

NB: You will need to manually create a new file called todo.txt in the same folder as your program before you start.
"""

file = open("/Users/brionydunbar/Documents/CFGdegree/CFG-tests/python_session5/todo.txt", "r+")
contents = file.read()
print(contents)

new_item = input("Add new to do item: ")

file = open("/Users/brionydunbar/Documents/CFGdegree/CFG-tests/python_session5/todo.txt", "a")

file.write("\n" + new_item)

file = open("/Users/brionydunbar/Documents/CFGdegree/CFG-tests/python_session5/todo.txt", "r")
contents = file.read()
print(contents)

file.close()