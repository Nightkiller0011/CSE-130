# 1. Name:
#      -Josh ELlis-
# 2. Assignment Name:
#      Lab 10: Numeric Sequence
# 3. Assignment Description:
#      -This program is meant to find the correct Francois sequence number.-
# 4. What was the hardest part? Be as specific as possible.
#      -The hardest part of this code was the efficiency-
# 5. How long did it take for you to complete the assignment?
#      -This took about 1 hours-



# This executes the code to find the francois sequence number.
def execute(seq_num):
    answer = 0
    assert type(seq_num) == int

    # These first two if, else statements are for the first two numbers.
    if seq_num == 1:
        answer = 2
    elif seq_num == 2:
        answer = 1

    # This elif statement returns that answer is not found if the passed number is less than or equal to 0.
    elif seq_num <= 0:
        answer = "not found"
    
    # This else statement runs the program for all letters after the 2nd letter.
    else:
        num1 = 2
        num2 = 1

        # This for loop goes through each number and calculates the answer, and replaces the num1 and num2 
        # accordingly to continue the program.
        for number in range(3,seq_num+1,1):
            answer = num1 + num2
            assert answer > num1 and answer > num2
            num1 = num2
            num2 = answer
    print(f"The number in the sequence you asked for was {answer}.")


# This is main, which asks to run test cases or not.
def main():
    test = input("Is this a test [y/n]: ")

    # This runs test cases.
    if test.lower() != "n":
        execute(-1)
        execute(0)
        execute(1)
        execute(2)
        execute(9)
        execute(100)
        execute(200)
    else:

        # This runs custom cases.
        num = int(input("What number in the sequence: "))
        execute(num)

 # Runs main
main()