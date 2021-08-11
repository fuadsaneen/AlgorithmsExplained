# Program : Find the length of the string.
# Input : string = "India"
# Output : 5
# Explanation : The string "India" has 5 characters in it.
# Language : Python3

# O(n) time | O(1) space
def length_of_string(number):

    # Initialize the length as zero.
    length = 0

    # Do for each character in the string.
    for ch in string:
        length = length + 1

    # Return the length.
    return length      

# Main function.
if __name__ == '__main__':

    # Declare the string.
    string = "India"

    # Find the length of the string and store the result in the answer variable.
    answer = length_of_string(string)

    # Print the answer.
    print(answer)