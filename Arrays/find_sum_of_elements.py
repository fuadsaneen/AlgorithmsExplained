# Program : Find the sum of elements in an array.
# Input : size = 5 and array = [1, 3, 5, 2, 4]
# Ouput : 15
# Language : Python3

# O(n) time | O(1) space
def find_sum(size, array):

    # Assume that sum is initialy zero.
    sum = 0

    # Do for all elements from position 0 to size-1
    for i in range(size):
        # Declare the current element.
        current_element = array[i]
        # Add current element to sum.
        sum = sum + current_element
        
    # Return the sum.
    return sum 

# Main function.
if __name__ == '__main__':

    # Declare the size and array.
    size = 5
    array = [1, 3, 5, 2, 4]

    # Find sum of elements and store it in answer variable.
    answer = find_sum(size, array)

    # Print answer.
    print(answer)