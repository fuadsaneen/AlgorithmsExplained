# Program : Check whether the number is even or odd.
# Input : number = 5
# Output : Odd
# Explanation : 5 is not divisible by 2, so it is an odd number.
# Language : Python3

# O(1) time | O(1) space
def even_or_odd(number):
    
    # If the number is divisible by two, then it is an even number.
    if number % 2 == 0:
        return "Even"
    # Otherwise, ie, if the number is not divisible by two, then it is an odd number.    
    else:
        return "Odd"    

# Main function.
if __name__ == '__main__':

    # Declare the number.
    number = 5

    # Check whether the number is even or odd and store the result in answer variable.
    answer = even_or_odd(number)

    # Print the answer.
    print(answer)