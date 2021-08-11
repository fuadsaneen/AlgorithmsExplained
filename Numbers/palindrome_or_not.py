# Program : Check whether the number is palindrome or not.
# Input : number = 565
# Output : True
# Explanation : 565 and its reverse are the same, so 565 is a palindrome number.
# Language : Python3

# O(n) time | O(1) space
def palindrome_or_not(number):

    # Copy the number into a temporary variable.
    temp = number

    # Intialize reverse as zero.
    reverse = 0

    # Do till the number is greater than zero.
    while number > 0:
        # Find the last digit.
        last_digit = number % 10
        # Add the last digit to reverse.
        reverse = (reverse*10) + last_digit
        # Divide the number by 10 to find the next last digit.
        number = number // 10   

    # If the reverse is equal to the temp, then the number is palindrome.
    if reverse == temp:
        return True
    # Otherwise, ie, if the reverse is not equal to the temp, then the number is not palindrome.
    else:
        return False    

# Main function.
if __name__ == '__main__':

    # Declare the number.
    number = 565

    # Check whether the number is palindrome or not and store the result in answer variable.
    answer = palindrome_or_not(number)

    # Print the answer.
    print(answer)