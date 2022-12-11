# Define Variables
## Current score here
current_score = 0 

## File To Read
input_file = "./input.txt"

# Main program
## First, open the file to read
with open(input_file) as ff:
    ## Then, declare a for each line loop
    for line in open(input_file):
        ### First, turn the line insto a string
        line_string = str(line)
        ### Then, replace each letter with a number
        ### This is very bad code, but I did it to conceptualize
        ### What I'm even doing
        line_string = line_string.replace("A","1")
        line_string = line_string.replace("B","2")
        line_string = line_string.replace("C","3")
        line_string = line_string.replace("X","1")
        line_string = line_string.replace("Y","2")
        line_string = line_string.replace("Z","3")
        ### Create an array of both numbers for comparing
        line_array = line_string.split()
        ### Create move variables for comparing later
        ### Specifically, my choice vs the opponent
        opponent_move = int(line_array[0])
        my_move = int(line_array[1])
        ### Finally, we figure out the score of this turn
        ### The easiest check will come first - a tie
        #### In the event of a tie, my score is 3 + whatever number my move is
        if opponent_move == my_move:
            current_score = current_score + my_move + 3
            print("It's a draw! Your score is: " + str(current_score))
        #### If that's not the case, we check standard combinations
        #### First, we'll cover Rock (1) which beats scissors (2)
        elif opponent_move == 1:
            if my_move == 3:
                current_score = current_score + my_move
                print("You Lose! Your score is: " + str(current_score))
            #### If it loses to paper (2), I win and get 6 points
            elif my_move == 2:
                current_score = current_score + my_move + 6
                print("You Win! Your score is: " + str(current_score))
        #### Next we cover paper (2) which beats rock (1)
        elif opponent_move == 2:
            if my_move == 1:
                current_score = current_score + my_move
                print("You Lose! Your score is: " + str(current_score))
            else:
                current_score = current_score + my_move + 6
                print("You Win! Your score is: " + str(current_score))
        #### Finally, we cover scissors (3) which beats paper (2)
        elif opponent_move == 3:
            if my_move == 2:
                current_score = current_score + my_move
                print("You Lose! Your score is: " + str(current_score))
            else:
                current_score = current_score + my_move + 6
                print("You Win! Your score is: " + str(current_score))

print("Game Over! Your score is: " + str(current_score))
