# Program : Check whether x is a factor of n.
# Input : n = 24, x = 3
# Output : True
# Explanation : 3 is a factor of 24.
# Language : Python3

# O(1) time | O(1) space
def is_x_a_factor_of_n(n, x):

    # If n is divisible by x, then x is a factor of n.
    if n % x == 0:
        return True
    # Otherwise, ie, if n is not divisible by x, then x is not a factor of n.    
    else:
        return False    

# Main function.
if __name__ == '__main__':

    # Declare n and x.
    n = 24
    x = 3

    # Check whether x is a factor of n and store the result in answer variable.
    answer = is_x_a_factor_of_n(n, x)

    # Print answer.
    print(answer)