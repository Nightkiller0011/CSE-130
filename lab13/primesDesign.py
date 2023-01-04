# 1. Name:
#      -Josh Ellis-
# 2. Assignment Name:
#      Lab 13: Prime Numbers
# 3. Assignment Description:
#      -This program is meant to find the Prime Numbers up to a certain point-
# 4. What was the hardest part? Be as specific as possible.
#      -The hardest part of this project was finishing the design. I struggled with the 
#           pseudocode so I was a bit behind on the full understanding.-
# 5. How long did it take for you to complete the assignment?
#      -This program took about 6 hours.-
import math

def main():

    # Decide which test cases to run.
    test = input(f"Is this a test (y/n): ")

    # Perform test cases.
    if test == "y":
        test_case(-1)
        test_case(0)
        test_case(1)
        test_case(2)
        test_case(10)
        test_case(53)
        test_case(100)
        test_case(200)

    # Run manuel test cases
    else:
        search_number = int(input(f"This program will find all the prime numbers at or below N. Select that N: "))
        test_case(search_number)

# Function to run program tests.
def test_case(search_number):

    # Ensure search number is an interger.
    assert type(search_number) == int
    if search_number > 2:

        # Create a Boolean array
        number_array =  [True for i in range(search_number+1)]
        count = len(number_array)

        # Set 0 and 1 to False
        number_array[0] = False
        number_array[1] = False

        # Loop through each number from 2 until the Sqrt of the search Number.
        for factor in range(int(math.sqrt(search_number))+1):

            # Does not bother if factor is already false.
            if number_array[factor]:

                # Final loop which filters out.
                for multiple in range(factor*2,search_number+1, factor):
                    number_array[multiple] = False

        # Print the answer.
        answer = "The prime numbers at or below " + str(search_number) + " are:\t"

        # Add any Primes to answer variable.
        i=0
        for number in number_array:
            if number == True:
                answer += str(i) + ", "
            i+=1
        print(answer)
        


    # Print result if search number is 2.    
    elif search_number == 2:
        print(f"The only prime number up to 2 is 2.")
    
    # Print result if search number is 2.
    else:
        print("Next time, Please Pick a number higher than or equal to 2.")

# Execute program.
main()
