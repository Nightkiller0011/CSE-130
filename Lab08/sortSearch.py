# 1. Name:
#      -Joshua ELlis-
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      -This program is supposed to demonstrate our knowledge of asserts and hwo they
#           are used, as well as sorting a set of information.-
# 4. What was the hardest part? Be as specific as possible.
#      -The hardest part of this assignment was the asserts. It is a different kind of 
#           debugging than I am used to so I am slightly thrown off by it.-
# 5. How long did it take for you to complete the assignment?
#      -This assignment took me 5 hours to complete.


import json
def main():

    #prompts to ask it it is a test
    test = input("Is this a test?(y/n) ")
    if test == "y":

        # Runs Test Cases
        program("Lab08.empty.json")
        cont = input("\nPress enter to continue. ")
        program("Lab08.trivial.json")
        cont = input("\nPress enter to continue. ")
        program("Lab08.languages.json")
        cont = input("\nPress enter to continue. ")
        program("Lab08.states.json")
        cont = input("\nPress enter to continue. ")
        program("Lab08.cities.json")
    else:

        # Prompt user for file name and word to search.
        file_name = input(f"What is the name of the file? ")
        assert type(file_name) == str

        # Runs Sort Program.
        program(file_name)



def program(file_name):

    # Load information into a list for use from Json file.
    found = False
    assert type(found) == bool
    objects = []
    assert type(objects) == list

    # Opens and runs file, inserts data into a list.
    with open(file_name) as file:
        data = json.load(file)
    objects = data['array']

    # Validate Pre-conditions
    assert len(objects) >= 0
    if __debug__:
        for elements in objects:
            assert type(elements) == str
            assert elements >= "!"
            assert elements <= "z"

    # Creates i_pivot as lenght of the list - 1.
    i_pivot = len(objects)-1
    assert type(i_pivot) == int

    # Runs loop to iterate through all objects in the list.
    for object in range(0,len(objects)):

        # Sets i_largest as default 0.
        i_largest = 0
        assert type(i_largest) == int

        # Compares i_largest against each object in the list at i_check.
        for i_check in range(0, i_pivot):
            assert type(i_check) == int
            if objects[i_check] >= objects[i_largest]:
                i_largest = i_check
        
        # Swaps items in i_largest if it is bigger than i_pivot.
        if objects[i_largest] > objects[i_pivot]:
            swap = objects[i_pivot]
            assert type(swap) == str
            objects[i_pivot] = objects[i_largest]
            objects[i_largest] = swap
        i_pivot-=1
    
    # Prints out if the File has no values or may be the incorrect format.
    if len(objects) == 0:
        print("\nThere are no items in this file to be sorted.")
        print("The format may be incorrect, or it may be empty.")

    # Print out a file with a single value.
    elif len(objects) == 1:
        print(f"\nThe value in {file_name} is: {objects[0]}")

    # Print the result of the sorted list.
    else:
        print(f"\n\nThe values in {file_name} are: ")
        for object in objects:
            print(object)



main()