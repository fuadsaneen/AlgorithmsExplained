# Program : Find the sum of elements in an array.
# Input : size = 5 and array = [1, 3, 5, 2, 4]
# Output : 15
# Explanation : The sum of elements in the array is 15.
# Language : Python3

# O(n) time | O(1) space
def find_sum(size, array):

    # Assume that sum is initialy zero.
    sum = 0

    # Do for each element in the array.
    for i in range(size):
        # Declare the current element.
        current_element = array[i]
        # Add the current element to sum.
        sum = sum + current_element
        
    # Return the sum.
    return sum 

# Main function.
if __name__ == '__main__':

    # Declare the size and array.
    size = 5
    array = [1, 3, 5, 2, 4]

    # Find the sum of elements and store the result in answer variable.
    answer = find_sum(size, array)

    # Print answer.
    print(answer)