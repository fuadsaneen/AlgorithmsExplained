# Program : Determine whether a number is even or odd.
# Input : number = 5
# Output : Odd
# Explanation : 5 is not divisible by 2, so it is an odd number.
# Language : Python3

def even_or_odd(number):
    
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"    

# Main function.
if __name__ == '__main__':

    # Declare the number.
    number = 5

    # Find whether the given number is even or odd and store the result in answer variable.
    answer = even_or_odd(number)

    # Print answer.
    print(answer)