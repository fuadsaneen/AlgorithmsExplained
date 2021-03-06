# Program : Find the maximum element in an array.
# Input : size = 5 and array = [1, 3, 5, 2, 4]
# Output : 5
# Explanation : The maximum element in the array is 5.
# Language : Python3

# O(n) time | O(1) space
def find_max_element(size, array):

    # Assume that first element is the maximum element in the array.
    max_element = array[0]

    # Do for elements starting from position 1 to size-1 in the array.
    for i in range(1, size):
        # Declare the current element.
        current_element = array[i]
        # If the current_element is greater than the max_element, then update max_element.
        if current_element > max_element:
            max_element = current_element

    # Return the max_element.
    return max_element 

# Main function.
if __name__ == '__main__':

    # Declare the size and array.
    size = 5
    array = [1, 3, 5, 2, 4]

    # Find the maximum element and store the result in the answer variable.
    answer = find_max_element(size, array)

    # Print the answer.
    print(answer)