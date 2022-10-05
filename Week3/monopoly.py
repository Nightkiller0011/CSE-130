# 1. Name:
#      -Josh Ellis-
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      -This program deducts for the user whether or not they can place a hotel on Pennsylvania avenue in monopoly-
# 4. What was the hardest part? Be as specific as possible.
#      -The hardest part of this assignment was Ensuring that all of the questions were in order and that they execute correctly.
#       trying to compare-
# 5. How long did it take for you to complete the assignment?
#      -This program took me about 4 hours.-

# Main function contents
def main():
# Prompt for Color Ownership.
    color = input("Do you own all the green properties? (y/n) ")
    if color.lower() == "y":
    # Prompt for what is on PA.
        pa_count = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
        if pa_count < 5 and pa_count >= 0:
        # Prompt for what is on PC.
            pc_count = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
            if pc_count < 5 and pc_count >= 0:
            # Prompt for what is on NC.
                nc_count = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
                if nc_count < 5 and nc_count >= 0:
                #  Prompt for total amount of hotels available.
                    hotel_count = int(input("How many hotels are there to purchase? "))
                    if hotel_count > 0:
                    # Prompt for total amount of houses available.
                        house_count = int(input("How many houses are there to purchase? "))
                        if house_count >= 10:
                        # Prompt for total amount of cash owned.
                            cash_count = int(input("How much cash do you have to spend? "))
                            if cash_count >= 1000:
                                print()
                            else:
                                print("You do not have sufficient funds to purchase a hotel at this time.")
                        else:
                            print("There are not enough houses available for purchase at this time.")
                    else:
                        print("There are not enough hotels available for purchase at this time.")
                else:
                    print("Swap North Carolina's hotel with Pennsylvania's 4 houses.")  
            else:
                print("Swap Pacific's hotel with Pennsylvania's 4 houses.")
        else:
            print("You cannot purchase a hotel if the property already has one.")
    else:
        print("You cannot purchase a hotel until you own all the properties of a given color group.")


# Call Main function.
main()