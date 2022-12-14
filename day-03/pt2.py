# Needed to generate lower, and uppercase, alphabet strings
import string

# Create variables
input_file = "./input.txt"

## Create dicts / arrays here
common_chars = []

## Needed to gauge the rank of the results
char_scores = {}
score_letters = []
score_numbers = []
triplet_set = []
## Create the lowercase & uppercase alphabet string to
## append as score_letters 1-26
all_lower_case = string.ascii_lowercase
all_upper_case = string.ascii_uppercase
all_cases_string = list(all_lower_case + all_upper_case)

## Create the number ranges that correspond to the above strings
counter = 0

rank = 0
## Total rank is here
total_rank = 0
## Finally, combine & append them to the score ranks
for letter in all_cases_string:
    rank = rank + 1
    char_scores[letter] = rank

with open(input_file) as ff:
    print(ff.read())
    ## Then, declare a for each line loop
    for line in open(input_file):
        ### First, turn the line insto a string
        line_string = str(line)
        if counter < 3:
            triplet_set.append(line)
            counter = counter + 1
            print(counter)
#            continue
        elif counter == 3:
            pack_1 = str(triplet_set[0])
            pack_2 = str(triplet_set[1])
            pack_3 = str(triplet_set[2])
            triplet_set = []
            for char in pack_3:
                if char in pack_2:
                    if char in pack_1:
                        common_chars.append(char)
                        print(f"Found a match! it's: {common_chars}")
                        total_rank = total_rank + char_scores[char]
                        common_chars = []
                        break
            print(line_string)
            triplet_set.append(line)
            counter = 1
            
print(total_rank)
                        
