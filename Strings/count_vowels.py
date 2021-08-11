# Program : Find the number of vowels in the string.
# Input : string = "Nature"
# Output : 3
# Explanation : The string "Nature" has 3 vowels in it, ie, 'a', 'u' and 'e'.
# Language : Python3

# O(n) time | O(1) space
def length_of_string(number):

    # Initialize the vowel list.
    vowels = ["a", "e", "i", "o", "u"]

    # Intialize the count as zero.
    count = 0

    # Do for each character in the string.
    for ch in string:
        # If the current character is in the vowel list, then increment the count by 1.
        if ch in vowels:
            count = count + 1   

    # Return the count.
    return count      

# Main function.
if __name__ == '__main__':

    # Declare the string.
    string = "Nature"

    # Find the count of vowels in the string and store the result in the answer variable.
    answer = length_of_string(string)

    # Print the answer.
    print(answer)