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

## Create the lowercase & uppercase alphabet string to
## append as score_letters 1-26
all_lower_case = string.ascii_lowercase
all_upper_case = string.ascii_uppercase
all_cases_string = list(all_lower_case + all_upper_case)

## Create the number ranges that correspond to the above strings
rank = 0

## Total rank is here
total_rank = 0
## Finally, combine & append them to the score ranks
for letter in all_cases_string:
    rank = rank + 1
    char_scores[letter] = rank

print(char_scores)
with open(input_file) as ff:
    ## Then, declare a for each line loop
    for line in open(input_file):
        ### First, turn the line insto a string
        line_string = str(line)
        full_string_len = len(line_string)
        half_string_len = int(full_string_len / 2)
        first_half = line_string[0:half_string_len]
        second_half = line_string[half_string_len:full_string_len]
        print(first_half)
        print(second_half)
        for char in second_half:
            if char in first_half:
                common_chars.append(char)
                print(f"Found a match! it's: {common_chars}")
                total_rank = total_rank + char_scores[char]
                common_chars = []
                break
            else:
#                print("No matches my friend")
                common_chars = []

print(total_rank)
