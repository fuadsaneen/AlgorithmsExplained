# Program : Find the reverse of a number.
# Input : number = 12345
# Output : 54321
# Explanation : The number is reversed.
# Language : Python3

# O(n) time | O(1) space
def reverse_a_number(number):

    # Intialize the reverse as zero.
    reverse = 0

    # Do till the number is greater than zero.
    while number > 0:
        # Find the last digit.
        last_digit = number % 10
        # Add the last digit to the reverse.
        reverse = (reverse*10) + last_digit
        # Divide the number by 10 to find the next last digit.
        number = number // 10   

    # Return the reverse.
    return reverse

# Main function.
if __name__ == '__main__':

    # Declare the number.
    number = 12345

    # Find the reverse of the number and store the result in the answer variable.
    answer = reverse_a_number(number)

    # Print the answer.
    print(answer)