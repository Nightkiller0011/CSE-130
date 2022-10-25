# 1. Name:
#      -your name-
# 2. Assignment Name: Josh Ellis
#      Lab 06: Advanced Search
# 3. Assignment Description: 
#       -This is a program that finds a word in a list of items
# 4. Algorithmic Efficiency
#      -The efficiency of this program is O(n).
# 5. What was the hardest part? Be as specific as possible.
#      -The hardest part of this was keeping the names of variables and other objects organized.
# 6. How long did it take for you to complete the assignment?
#      -This took me 3 hours to complete.-

import json
def main():

    # Prompt user for file name and word to search.
    file_name = input(f"What is the name of the file? ")
    search_word = input(f"What word are we looking for? ")

    # Create variables and download file contents.
    found = False
    objects = []
    with open(file_name) as file:
        data = json.load(file)
    objects = data['array']

    # Create Start point, end point, and sorting point as variables
    end_point = len(objects)-1
    start_point = 0
    sort_point = (start_point + end_point)//2

    # Begin search loop.
    while start_point < end_point and found == False:
        if len(objects) == 1 and objects[sort_point] == search_word:
            found = True
        else:
            sort_point = (start_point + end_point)//2

        # Resets start_point as Middle (Sort Point)
        if search_word > objects[sort_point]:
            start_point = sort_point+1

        # Resets end_point as Middle (Sort Point)
        elif search_word < objects[sort_point]:
            end_point = sort_point-1

        #Handles finding the item
        else:
            found = True

    # Handles finding the item when there is only one item in the list.
    if len(objects) == 1 and objects[sort_point] == search_word:
        print(f"We found {search_word} in {file_name}.")

    # Handles empty files and displays output.
    elif (start_point == end_point or len(objects) == 0) and found != True:
        print(f"We could not find {search_word} in {file_name}.")

    # Displays a successful search and results.
    elif(found):
        print(f"We found {search_word} in {file_name}.")

    # Displays an unsuccessful search and results.
    else:
        print(f"We could not find {search_word} in {file_name}.")


main()