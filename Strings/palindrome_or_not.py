# Program : Check whether the string is palindrome or not.
# Input : string = "MADAM"
# Output : True
# Explanation : String "MADAM" and its reverse are the same, so "MADAM" is a palindrome.
# Language : Python3

# O(n) time | O(1) space
def palindrome_or_not(string):

    # Initialize left to the start of the string.
    left = 0
    # Initialize right to the end of the string.
    right = len(string) - 1

    # Do till left is less than right.
    while left < right:
        # Declare current left and right element.
        left_element = string[left]
        right_element = string[right]

        # If left element is not equal to right element, then the string is not palindrome.
        if left_element != right_element:
            return False
        # Otherwise, if the left element and right element are equal, then increment left pointer and decrement right pointer.    
        else:
            left = left + 1
            right = right - 1    

    # If no mismatch is found, then the string is palindrome.
    return True           

# Main function.
if __name__ == '__main__':

    # Declare the string.
    string = "MADAM"

    # Check whether the string is palindrome or not and store the result in the answer variable.
    answer = palindrome_or_not(string)

    # Print the answer.
    print(answer)