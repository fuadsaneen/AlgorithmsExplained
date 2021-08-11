# Program : Check whether the number is prime or not.
# Input : number = 7
# Output : True
# Explanation : 7 has only 1 and 7 as its factors.
# Language : Python3

# O(n) time | O(1) space
def prime_or_not(number):

    # Do for each element from 2 to number - 1
    for i in range(2, number - 1):
        # If the number is divisible by current element, then it is not prime.
        if number % i == 0:
            return False

    # Otherwise, ie, if the number is not divisible by any element other than 1 and the number itself, then it is a prime.
    return True        

# Main function.
if __name__ == '__main__':

    # Declare the number.
    number = 7

    # Check whether the number is prime or not and store the result in answer variable.
    answer = prime_or_not(number)

    # Print answer.
    print(answer)