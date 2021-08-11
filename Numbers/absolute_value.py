# Program : Find the absolute value of the number.
# Input : number = -3
# Output : 3
# Explanation : The absolute value of a number is the distance to that number from origin, so here it is 3.
# Language : Python3

# O(1) time | O(1) space
def absolute_value(number):

    # If the number is less than zero, then its absolute value is -(number).
    if number < 0:
        return -(number)
    # Otherwise, if the number is greater than or equal to zero, then its absolute value is the number itself.    
    else:
        return number     

# Main function.
if __name__ == '__main__':

    # Declare the number.
    number = -3

    # Find the absolute value of the number and store the result in the answer variable.
    answer = absolute_value(number)

    # Print the answer.
    print(answer)