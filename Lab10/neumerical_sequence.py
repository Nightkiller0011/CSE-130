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
    
    if seq_num == 1:
        answer = 2
    elif seq_num == 2:
        answer = 1
    elif seq_num <= 0:
        answer = "not found"
    else:
        num1 = 2
        num2 = 1
        for number in range(3,seq_num+1,1):
            answer = num1 + num2
            num1 = num2
            num2 = answer
    print(f"The number in the sequence you asked for was {answer}.")


# This is main, which asks to run test cases or not.
def main():
    test = input("Is this a test [y/n]: ")
    if test.lower() != "n":
        execute(-1)
        execute(0)
        execute(1)
        execute(2)
        execute(9)
        execute(100)
        execute(200)
    else:
        num = int(input("What number in the sequence: "))
        execute(num)

 # Runs main
main()