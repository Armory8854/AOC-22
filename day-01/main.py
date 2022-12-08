import os

input = open("./input.txt", "r")
arr = []
counter = 0
#print(input.read())
for line in input:
    if line == "\n":
        counter = counter + 1
    else:
        array = "arr_" + str(counter)
        array.append(line)
        print("arr_" + counter[counter])
