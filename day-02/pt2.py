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
        line_string = line_string.replace("X","lose")
        line_string = line_string.replace("Y","draw")
        line_string = line_string.replace("Z","win")
        ### Create an array of both numbers for comparing
        line_array = line_string.split()
        ### Create move variables for comparing later
        ### Specifically, my choice vs the opponent
        opponent_move = int(line_array[0])
        my_move = str(line_array[1])
        ### In the event of a draw, I always play what the opponent did
        if my_move == "draw":
            current_score = current_score + opponent_move + 3
            print("It's a draw! Your score is: " + str(current_score))
        ### In the event of a lose, I have to factor each possible number
        ### And it's inverse
        elif my_move == "lose":
            if opponent_move == 1:
                current_score = current_score + 3
                print("You Lose! Your score is: " + str(current_score))
            elif opponent_move == 2:
                current_score = current_score + 1
                print("You Lose! Your score is: " + str(current_score))
            else:
                current_score = current_score + 2
                print("You Lose! Your score is: " + str(current_score))
        ### Finally we cover winning, which always gives 6
        ### On top of whatever move I should have picked
        elif my_move == "win":
            if opponent_move == 1:
                current_score = current_score + 2 + 6
                print("You Win! Your score is: " + str(current_score))
            elif opponent_move == 2:
                current_score = current_score + 3 + 6
                print("You Win! Your score is: " + str(current_score))
            else:
                current_score = current_score + 1 + 6
                print("You Win! Your score is: " + str(current_score))

print("Game Over! Your score is: " + str(current_score))
