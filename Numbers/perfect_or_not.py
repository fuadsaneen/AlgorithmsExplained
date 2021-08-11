# Program : Check whether the number is perfect or not.
# Input : number = 6
# Output : True
# Explanation : The factors of 6, excluding 6 are 1, 2, 3 and their sum is 1 + 2 + 3 = 6, so 6 is a perfect number.
# Language : Python3

# O(n) time | O(1) space
def perfect_or_not(number):

    # Intialize the sum as 1.
    sum = 1

    # Do for each element starting from 2 to sqrt(number).
    for i in range(2, int((number ** 0.5) + 1)):    
        if number % i == 0:
            if number / i == i:
                sum = sum + i
            else:
                sum = sum + i + (number/i)

    # If the sum is equal to the number, then it is a perfect number.
    if sum == number:
        return True
    # Otherwise, ie, if the sum is not equal to the number, then it is not a perfect number.
    else:
        return False                   

# Main function.
if __name__ == '__main__':

    # Declare the number.
    number = 6

    # Check whether the number is perfect or not and store the result in answer variable.
    answer = perfect_or_not(number)

    # Print the answer.
    print(answer)