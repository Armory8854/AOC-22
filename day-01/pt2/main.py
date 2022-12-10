import os
from collections import Counter
# First, create an empty dict to store the elves
elf_list = {}
# Create an empty array for appending the calories in later
calories = []
# Refer to the input file as an object
input_file = "./input.txt"
# Finally, create 2 'counters' for later use
## First, one for iterating elves
elf_counter = 0
## Then, one for totaling calories
calories_total = 0
# Open the file in a with statement
with open(input_file) as ff:
    # Count every blank new line to assaign as elves
    elves_count = sum(not line.strip() for line in ff)
    # Assign the individal elves here
    # If my numbers are right, this is 255
    elves = range(elves_count)
    # Finally create the for loop
    for line in open(input_file):
#        if not line.strip():
        if line.strip():
            calories_total = calories_total + int(line)
            elf_list[elf_counter] = calories_total
#            print(elf_list[elf_counter])
        else:
            elf_counter = elf_counter + 1
            calories_total = 0

k = Counter(elf_list)
high = k.most_common(3)
calories_top_3 = 0
for i in high:
    calories_top_3 = calories_top_3 + i[1]

print(calories_top_3)
