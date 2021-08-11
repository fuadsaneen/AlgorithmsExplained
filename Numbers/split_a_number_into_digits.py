# Program : Split the number into digits.
# Input : number = 12345
# Output : [5, 4, 3, 2, 1]
# Explanation : The number is splitted into seperate digits.
# Language : Python3

# O(n) time | O(1) space
def split_number_into_digits(number):

    # Intialize a list to store the digits.
    digits = []

    # Till the number is greater than zero.
    while number > 0:
        # Find the last digit and append it to list.
        last_digit = number % 10
        digits.append(last_digit)
        # Divide the number by 10 to find the next last digit.
        number = number // 10   

    # Return the digits.
    return digits    

# Main function.
if __name__ == '__main__':

    # Declare the number.
    number = 12345

    # Split the number into digits and store the result in answer variable.
    answer = split_number_into_digits(number)

    # Print answer.
    print(answer)