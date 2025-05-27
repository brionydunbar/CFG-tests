# writing to a file

file = open("demotowrite.txt", "w")

file.write("I am writing to a new file")

file.close()

# appending to a file

file = open("demotowrite.txt", "a+")

file.write("\nI am adding more text")

file.close()

# adding more than one line to a file

file = open("demotowrite2.txt", "w")

pokemon_lyrics = [
    "\nI wanna be the very best",
    "\nThat no one ever was",
    "\nTo catch them is my real test"
    ]

file.writelines(pokemon_lyrics)

file.close()

file = open("demotowrite2.txt", "a")

file.write("\nTo train them is my cause")

file.close()