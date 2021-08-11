# Program : Find the sum of digits in a number.
# Input : number = 12345
# Output : 15
# Explanation : The number is splitted into seperate digits and the sum is calculated.
# Language : Python3

# O(n) time | O(1) space
def sum_of_digits(number):

    # Intialize sum as zero.
    sum = 0

    # Till the number is greater than zero.
    while number > 0:
        # Calculate last digit.
        last_digit = number % 10
        # Add the last digit to sum.
        sum = sum + last_digit
        # Divide the number by 10 to find next last digit.
        number = number // 10   

    # Return the sum.
    return sum

# Main function.
if __name__ == '__main__':

    # Declare the number.
    number = 12345

    # Find the sum of digits in a number and store the result in answer variable.
    answer = sum_of_digits(number)

    # Print answer.
    print(answer)