# Program : Check whether the number is armstrong or not.
# Input : number = 153
# Output : True
# Explanation : Sum of cubes of the digits is equal to the number, ie, (1*1*1) + (5*5*5) + (3*3*3) = 153.
# Language : Python3

# O(n) time | O(1) space
def armstrong_or_not(number):

    # Copy the number into a temporary variable.
    temp = number

    # Intialize sum as zero.
    sum = 0

    # Do till the number is greater than zero.
    while number > 0:
        # Find the last digit.
        last_digit = number % 10
        # Add the last digit's cube to sum.
        sum = sum + (last_digit * last_digit * last_digit)
        # Divide the number by 10 to find the next last digit.
        number = number // 10   

    # If sum is equal to the temp, then the number is an armstrong number.
    if sum == temp:
        return True
    # Otherwise, ie, if the sum is not equal to the temp, then the number is not an armstrong number.
    else:
        return False 

# Main function.
if __name__ == '__main__':

    # Declare the number.
    number = 153

    # Check whether the number is armstrong or not and store the result in the answer variable.
    answer = armstrong_or_not(number)

    # Print the answer.
    print(answer)