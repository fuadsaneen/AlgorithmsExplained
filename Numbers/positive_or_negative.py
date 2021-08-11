# Program : Check whether the given number is positve or negative.
# Input : number = -3
# Output : Negative
# Explanation : -3 is less than zero, so it is a negative number.
# Language : Python3

# O(1) time | O(1) space
def positive_or_negative(number):

    # If the number is equal to zero, then it is neither positive nor negative.
    if number == 0:
        return "Neither positve nor negative"
    # If the number is greater than zero, then it is positive.    
    elif number > 0:
        return "Positve"
    # Otherwise, ie, if the number is less than zero, then it is negative    
    else:
        return "Negative"        

# Main function.
if __name__ == '__main__':

    # Declare the number.
    number = -3

    # Check whether the given number is positive or negative and store the result in answer variable.
    answer = positive_or_negative(number)

    # Print answer.
    print(answer)