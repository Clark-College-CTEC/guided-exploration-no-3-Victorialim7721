# Guided Exploration No. 3
# Victoria Limwanich

# Importing Python random library to use random functions
import random
# Setting an empty list to append names to it
possible_names = []
# Opens a new file to store names
outputFile = open('rap-names-output.txt', 'w')
# Opens file rap-names.txt to use
with open('rap-names.txt', 'r') as dataFile:
    # Go through each line in file
    for name in dataFile:
        # Adds each name to the empty list set earlier (while also getting rid of extra line space at the end)
        possible_names.append(name.rstrip())
# Getting how many times to go through loop
count = int(input('How many rap names would you like to create? '))
# Getting length of each name
parts = int(input('How many parts should the name contain? '))
# Looping through what the user entered as how many names they would like to create
for i in range(count):
    # Setting an empty list to make names in
    name_parts = []
    # Looping through however many parts the user wanted
    for j in range(parts):
        # Going through the list of possible names created earlier, choosing a random number, and appending corresponding string to the name list
        name_parts.append(possible_names[random.randint(0, len(possible_names)-1)])
    # Joining each part with a space
    outputFile.write(f"{' '.join(name_parts)}\n")
    # Printing each name
    print(f"{' '.join(name_parts)}")

# Close file
outputFile.close()