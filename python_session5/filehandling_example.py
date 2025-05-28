from pprint import pp as pp

# adding the file path
file = open("/Users/brionydunbar/Documents/CFGdegree/CFG-tests/python_session5/pokemon.txt", "r")

# assign a second variable for content
contents = file.read()
print(contents)

pp(contents)

file.close()


# hold option button after ctrl click in a folder
# file = open("/Users/brionydunbar/Downloads/Certificate - Briony Dunbar.pdf", "r")