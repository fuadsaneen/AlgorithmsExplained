# Program : Find the maximum element in an array.
# Input : size = 5 and array = [1, 3, 5, 2, 4]
# Ouput : 5
# Language : Python3

# O(n) time | O(1) space
def find_max(array, size):

    # Assume that 1st element is the maximum in the array.
    max_element = array[0]

    # Do for all elements from position 1 to size-1
    for i in range(1, size):
        # Declare the current element.
        current_element = array[i]
        # Compare current_element with max_element and choose the maximum as max_element.
        max_element = max(max_element, current_element)

    # Return the max_element.
    return max_element 

# Main function.
if __name__ == '__main__':

    # Declare the size and array.
    size = 5
    array = [1, 3, 5, 2, 4]

    # Find maximum element and store it in answer variable.
    answer = find_max(array, size)

    # Print answer.
    print(answer)