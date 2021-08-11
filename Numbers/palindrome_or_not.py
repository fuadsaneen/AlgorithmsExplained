# Program : Check whether the number is palindrome or not.
# Input : number = 565
# Output : True
# Explanation : The number and its reverse are same, so it is a palindrome number.
# Language : Python3

# O(n) time | O(1) space
def palindrome_or_not(number):

    # Copy nuumber to a temporary variable.
    temp = number

    # Intialize reverse as zero.
    reverse = 0

    # Till the number is greater than zero.
    while number > 0:
        # Calculate last digit.
        last_digit = number % 10
        # Add the last digit to reverse.
        reverse = (reverse*10) + last_digit
        # Divide the number by 10 to find next last digit.
        number = number // 10   

    # if reverse is equal to the temp, then the number is palindrome.
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

    # Print answer.
    print(answer)