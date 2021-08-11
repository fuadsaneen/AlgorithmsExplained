# Program : Check whether x is a factor of the number.
# Input : number = 24, x = 3
# Output : True
# Explanation : 3 is a factor of 24.
# Language : Python3

# O(1) time | O(1) space
def is_x_a_factor_of_number(number, x):

    # If the number is divisible by x, then x is a factor of the number.
    if number % x == 0:
        return True
    # Otherwise, ie, if the number is not divisible by x, then x is not a factor of the number.    
    else:
        return False    

# Main function.
if __name__ == '__main__':

    # Declare n and x.
    number = 24
    x = 3

    # Check whether x is a factor of the number and store the result in answer variable.
    answer = is_x_a_factor_of_number(number, x)

    # Print answer.
    print(answer)