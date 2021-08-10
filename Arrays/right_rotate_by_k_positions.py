# Program : Right rotate the array by k positions.
# Input : size = 5, array = [1, 3, 5, 2, 4], k = 2
# Ouput : [2, 4, 1, 3, 5]
# Language : Python3

# O(n) time | O(1) space
def right_rotate_by_one(size, array):

    # Store last element.
    last_element = array[-1]

    # Do for each element from position size - 2 to 0 (ie, excluding last element).
    for i in reversed(range(size - 1)):
        # Copy current element to next element.
        array[i + 1] = array[i]

    # Copy last element to first position.
    array[0] = last_element   

# O(k) time | O(1) space
def right_rotate_by_k(size, array, k):

    # Do for k times.
    for i in range(k):
        # Right rotate the array by one position.
        right_rotate_by_one(size, array)

    # Return the updated array.
    return array    

# Main function.
if __name__ == '__main__':

    # Declare the size, array and k.
    size = 5
    array = [1, 3, 5, 2, 4]
    k = 2

    # right rotate the array by k positions and store it in answer variable.
    answer = right_rotate_by_k(size, array, k)

    # Print answer.
    print(answer)