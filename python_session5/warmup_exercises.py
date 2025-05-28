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



"""
This program is supposed to read data about trees from a file to find the shortest tree. 
Complete the program adding code to open 'trees.csv'.

The trees.csv file included with your student guides. 
Save the csv file in the same folder as your Python program!
"""

# spreadsheet = # Add code to open the csv file
#
# heights = []
#
# for row in spreadsheet:
#     tree_height = row['height']
#     heights.append(tree_height)
#
# shortest_height = min(heights)
# print(shortest_height)




"""
Write a Python programme to count the occurrences of a word in a text file
Your program will take a word from the user and count the number of occurrences of that word in a file

1. Take the file name and the word to be counted from the user
2. Read each line from the file and split the line to form a list of words
3. Check if the word provided by the user and any of the words in the list are equal and if they are, then increment the word count
4. Exit
"""

file_name = input("Enter file name: ")
word_input = input("Which word would you like to be counted? ").lower()

count = 0

with open("/Users/brionydunbar/Documents/CFGdegree/CFG-tests/python_session5/5.3_example_one.txt", "r+") as text:
    for line in text:
        line = line.strip() # removes the leading spaces and newline character
        line = line.lower() # converts the characters in line to lowercase to avoid case mismatch
        words = line.split() # splits the line into words
        for word in words:
            if (word == word_input):
                count += 1
print(f"{word_input} appeared {count} times.")

file.close()