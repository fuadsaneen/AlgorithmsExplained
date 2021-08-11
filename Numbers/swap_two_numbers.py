# Program : Swap two numbers.
# Input : a = 8, b = 16
# Output : a = 16, b = 8
# Explanation : The values of both a and b are interchanged.
# Language : Python3

# O(1) time | O(1) space
def swap_two_numbers(a, b):

    # Store the value of a in a temporary variable.
    temp = a

    # Copy the value of b to a.
    a = b

    # Copy the value of temporary variable to b.
    b = temp

    # Return the values of a and b.
    return a, b  

# Main function.
if __name__ == '__main__':

    # Declare a and b.
    a = 8
    b = 16

    # Swap the two numbers and store the result in answer variable.
    answer = swap_two_numbers(a, b)

    # Print answer.
    print(answer)