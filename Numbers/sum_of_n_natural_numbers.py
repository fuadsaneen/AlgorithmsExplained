# Program : Find the sum of n natural numbers.
# Input : n = 18
# Output : 171
# Explanation : The sum of natural numbers upto 18 is 171.
# Language : Python3

# O(1) time | O(1) space
def sum_of_n_natural_numbers(n):

    # If the number is less than zero, then return error message.
    if n < 0:
        return "Number can't be negative."
    # Otherwise, calculate sum using its mathematical formula.    
    else:
        # Initialize sum as zero.
        sum = 0
        # Compute its value using formula.
        sum = (n*(n + 1))/2

    # Return the sum.
    return sum

# Main function.
if __name__ == '__main__':

    # Declare n.
    n = 18

    # Find the sum of n natural numbers and store the result in answer variable.
    answer = sum_of_n_natural_numbers(n)

    # Print answer.
    print(answer)