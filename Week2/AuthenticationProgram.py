# 1. Name:
#      -Josh Ellis-
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      -This program is meant to check a username against a password.-
# 4. What was the hardest part? Be as specific as possible.
#      -The hardest part of this assignment was trying to understand how to 
#       read the json object. The other most difficult part that I had was\
#       trying to compare-
# 5. How long did it take for you to complete the assignment?
#      -This program took me about 2 hours.-
import json



# Opens the Json File with usernames and passwords

def main():
    passwords = []
    usernames = []
    with open("Week2\Lab02.json") as file:
        data = json.load(file)

    # Puts information into Username and Password Lists.
    for i in data["username"]:
        usernames.append(i)
    for i in data["password"]:
        passwords.append(i)
    # Asking user for Username and Password.
    enter_user = input("Username: ")    
    enter_pass = input("Password: ")
    # Compare Username index with Password Index.
    try:
        user_comp = usernames.index(enter_user)
        pass_comp = passwords.index(enter_pass)
    # Grant or restrict Access.
        if user_comp == pass_comp:
            print("You are Authenticated!")
        else:
            print("You are not authorized to use the system.")
    except:
        print("You are not authorized to use the system.")

# Call Main function.
main()